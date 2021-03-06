import os
from setuptools import setup

setup(
    name = "PyOnfido",
    version = "0.3.4",
    author = "Sean McLemon",
    author_email = "sean.mclemon@gmail.com",
    description = ("Python wrapper library for Onfido's REST API for background checking."),
    license = "BSD",
    keywords = "pyonfido onfido background",
    url = "https://github.com/smcl/pyonfido",
    download_url = 'https://github.com/smcl/pyonfido/tarball/0.3',
    packages=['onfido', 'onfido.test'],
    test_suite='onfido.test.all',
    classifiers=[
        "Development Status :: 5 - Production/Stable ",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    install_requires=[
        'requests>=2,<3',
        'requests_mock==0.7.0',
        'unittest2==1.1.0'
    ],
    setup_requires=[
        'requests>=2,<3',
        'requests_mock==0.7.0',
        'unittest2==1.1.0'
    ],
)
