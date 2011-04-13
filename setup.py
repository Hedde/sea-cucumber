from setuptools import setup, find_packages
import os
import seacucumber

DESCRIPTION = "A Django email backend for Amazon Simple Email Service, backed by celery"

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    pass

version_str = '%d.%d' % (seacucumber.VERSION[0], seacucumber.VERSION[1])

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Framework :: Django',
]

setup(
    name='seacucumber',
    version=version_str,
    packages=['seacucumber'],
    author='Gregory Taylor',
    author_email='gtaylor@duointeractive.com',
    url='https://github.com/duointeractive/sea-cucumber/',
    license='MIT',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    platforms=['any'],
    classifiers=CLASSIFIERS,
    install_requires=['boto'],
)