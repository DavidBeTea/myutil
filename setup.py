# -*- coding: utf-8 -*-
"""
@date 2017/11/8
"""
import codecs
import os
import sys

try:
    from setuptools import setup
except:
    from distutils.core import setup


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version():
    file = open('.version', 'r')
    version = str(file.read())
    file.close()
    return version


NAME = "myutil"
PACKAGES = ["myutil", ]
DESCRIPTION = "This is my python util package."
LONG_DESCRIPTION = read("README.md")
KEYWORDS = "python util"
AUTHOR = "Dai Wei"
AUTHOR_EMAIL = "629569794@qq.com"
URL = "https://github.com/DavidBeTea/myutil"
VERSION = "1.0.2"
LICENSE = "MIT"
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=
    [
        # 'License :: OSI Approved :: MIT License',
        # 'Programming Language :: Python',
        # 'Intended Audience :: Developers',
        # 'Operating System :: OS Independent',
        'Framework :: model',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=PACKAGES,
    include_package_data=True,
    package_data={'': ['.version']},
    zip_safe=True,
)
