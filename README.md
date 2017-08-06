conan-botan
===========

[ ![Download](https://api.bintray.com/packages/fmorgner/conan-fmorgner/Botan%3Afmorgner/images/download.svg?version=2.1.0%3Astable) ](https://bintray.com/fmorgner/conan-fmorgner/Botan%3Afmorgner/2.1.0%3Astable/link)

This package provides Botan by Randombit. Botan is a cryptography library
written from scratch in modern C++.

Package options
---------------

| Option              | Description                                          | Default |
|---------------------|------------------------------------------------------|---------|
| amalgamation        | Generate amalgamation files and build via amalgation | True    |
| bzip2               | Use BZip2                                            | False   |
| debug_info          | Include debug symbols                                | False   |
| openssl             | Enable transports using OpenSSL                      | False   |
| quiet               | Build quietly                                        | True    |
| shared              | Build shared library                                 | True    |
| single_amalgamation | Build single file instead of splitting on ABI        | False   |
| sqlite3             | Enable SQLite3 support                               | False   |
| zlib                | Use Zlib                                             | False   |
