from conan.packager import ConanMultiPackager

if __name__ == '__main__':
    builder = ConanMultiPackager(username='fmorgner', archs=['x86_64'])
    builder.add_common_builds(shared_option_name='Botan:shared', pure_c=False)
    builder.run()
