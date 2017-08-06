# pylint: disable=missing-docstring
from collections import defaultdict
from conan.packager import ConanMultiPackager


def main():
    builder = ConanMultiPackager(
        username='fmorgner',
        archs=['x86_64'],
        upload='https://api.bintray.com/conan/fmorgner/conan-fmorgner',
        remotes='https://api.bintray.com/conan/fmorgner/conan-fmorgner',
        total_pages=2,
        curpage='Release'
    )
    named_builds = defaultdict(list)
    builder.add_common_builds(shared_option_name='Botan:shared', pure_c=False)
    for settings, options, env_vars, build_requires in builder.builds:
        named_builds[settings['build_type']].append([
            settings,
            options,
            env_vars,
            build_requires,
        ])
    builder.named_builds = named_builds
    builder.run()


if __name__ == '__main__':
    main()
