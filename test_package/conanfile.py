# pylint: disable=missing-docstring

import os
from conans import ConanFile, CMake

CHAN = os.getenv('CONAN_CHANNEL', 'testing')
USER = os.getenv('CONAN_USERNAME', 'fmorgner')


class PackageTest(ConanFile):
    settings = (
        'arch',
        'build_type',
        'compiler',
        'os',
    )
    generators = [
        'cmake',
    ]

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir=self.conanfile_directory)
        cmake.build()

    def test(self):
        os.chdir('bin')
        self.run(os.sep.join(['.', 'package_test']))
