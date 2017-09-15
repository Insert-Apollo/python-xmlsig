import re
import sys

from setuptools import find_packages, setup

install_requires = [
    'lxml>=3.0.0',
    'cryptography'
]

async_require = []  # see below

tests_require = [
    'freezegun==0.3.8',
    'mock==2.0.0',
    'pretend==1.0.8',
    'pytest-cov==2.5.1',
    'pytest==3.1.3',
    'requests_mock>=0.7.0',
    'PyOpenSSL',
    # Linting
    'isort==4.2.5',
    'flake8==3.3.0',
    'flake8-blind-except==0.1.1',
    'flake8-debugger==1.4.0',
    'flake8-imports==0.1.1',
]


if sys.version_info > (3, 4, 2):
    async_require.append('aiohttp>=1.0')
    tests_require.append('aioresponses>=0.1.3')


setup(
    name='xmlsig',
    version='0.0.2',
    description='Python based XML signature',
    long_description='XML Signature created with cryptography and lxml',
    author="Enric Tobella Alomar",
    author_email="etobella@creublanca.es",
    url='http://docs.python-src.org',

    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
        'async': async_require,
    },
    entry_points={},
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,

    license='AGPL',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    zip_safe=False,
)