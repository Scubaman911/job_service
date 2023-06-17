#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=7.0', 
    'Flask>=2.0',
    'Flask-APScheduler>=1.12.4',
]

test_requirements = [ ]

setup(
    author="cs",
    author_email='-',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    description="Python Job Scheduler",
    entry_points={
        'console_scripts': [
            'jobby=jobby.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='jobby',
    name='jobby',
    packages=find_packages(include=['jobby', 'jobby.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/-/jobby',
    version='0.2.0',
    zip_safe=False,
)
