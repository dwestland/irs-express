import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'docs/README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='irsexpress2',
    version='1.0',
    packages=['irsexpress2'],
    include_package_data=True,
    license='Commercial',
    description='IRS Express',
    long_description=README,
    url='https://www.irsexpress.com/',
    author='Alexey Kolyanov',
    author_email='alexey.kolyanov@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: Commercial',
        'Operating System :: Ubuntu Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
