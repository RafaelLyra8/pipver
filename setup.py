#!/usr/bin python

from setuptools import setup
import versioneer

with open('LICENSE', 'r') as _f:
    _license = _f.read()

with open('README.rst', 'r') as _f:
    _long_description = _f.read()

with open('requirements.txt', 'r') as _f:
    _requirements = _f.read().strip().split('\n')



setup(
    name="pipver",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Python versioning example",
    long_description=_long_description,
    url="http://pypi.python.org/pypi",
    author="Rafael Lyra",
    author_email="rafael.lyra@lnls.br",
    license=_license,
    packages=[
        'pipver',
        'test'],
    scripts=[
        "scripts/hw.py"
    ],
    install_requires=_requirements,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: None',
        'Operating System :: Ubuntu :: Linux',
        'Programming Language :: Python 2.7.17'
    ]
)
