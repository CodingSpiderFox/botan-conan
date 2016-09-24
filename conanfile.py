from conans import ConanFile
from re import search

class BotanConan(ConanFile):
    name = 'Botan'
    version = '1.11.31'
    settings = {
        'os': ['Linux'],
        'arch': None,
        'compiler': None,
        'build_type': None
    }
    options = {
        'shared': [True, False],
        'quiet': [True, False],
    }
    default_options = 'shared=True\nquiet=True'
    url = 'https://github.com/fmorgner/botan-conan.git'
    license = 'Simplified BSD'

    def _get_major_and_minor(self):
        return search('(?P<major_minor>[0-9]+\.[0-9]+)\.*', self.version).group('major_minor')

    def source(self):
        self.run('git clone https://github.com/randombit/botan.git')
        self.run('cd botan && git checkout %s' % self.version)

    def build(self):
        if self.settings.compiler in ('clang', 'apple-clang'):
            compiler_option = 'clang'
        elif self.settings.compiler == 'gcc':
            compiler_option = 'gcc'
        else:
            compiler_option = 'msvc'

        if self.settings.arch == 'x86':
            cpu_option = 'x86'
        else:
            cpu_option = 'x86_64'

        if self.settings.os == 'Linux' and self.settings.compiler.libcxx == 'libc++':
            make_ldflags = 'LDFLAGS=-lc++abi'
        else:
            make_ldflags = ''

        shared_option = '' if self.options.shared else '--disable-shared'
        quiet_option = '--quiet' if self.options.quiet else ''
        self.output.info('Configuring %s' % self.name)
        self.run('cd botan && ./configure.py --prefix fakeroot --cc={compiler} --cpu={cpu} --cc-abi-flags="{abi}" {shared} {quiet}'.format(**{
            'compiler': compiler_option,
            'quiet': quiet_option,
            'shared': shared_option,
            'cpu': cpu_option,
            'abi': '-stdlib=%s' % self.settings.compiler.libcxx,
        }))
        self.output.info('Building %s' % self.name)
        self.run('cd botan && %s make %s -j$(nproc) 2>&1' % (make_ldflags, quiet_option))
        self.output.info('Running %s self-test' % self.name)
        self.run('cd botan && ./botan-test')

    def package(self):
        self.run('cd botan && make install')
        self.copy('*.h', src='botan/fakeroot/include/botan-1.11', dst='include')
        self.copy('*.a', src='botan/fakeroot/lib', dst='lib', keep_path=False)
        self.copy('*.so*', src='botan/fakeroot/lib', dst='lib', keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ['botan-%s' % self._get_major_and_minor()]
