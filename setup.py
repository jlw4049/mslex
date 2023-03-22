#!/usr/bin/env python3

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup(
    author="Lawrence D'Anna",
    author_email='larry@elder-gods.org',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    description="shlex for windows",
    entry_points={
        'console_scripts': [
            'mslex-split=mslex:split_cli',
        ],
    },
    install_requires=[],
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='mslex',
    name='mslex',
    py_modules=['mslex'],
    setup_requires=[],
    test_suite='tests',
    tests_require=[],
    url='https://github.com/smoofra/mslex',
    version='1.0.0',
    zip_safe=True,
)
