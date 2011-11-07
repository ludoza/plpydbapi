"""
Setup script for plpydbapi
"""

from setuptools import setup
from setuptools.command.test import test as _test


class test(_test):
    """Override test command to run psql with SQL test script"""

    def run(self):
        import subprocess
        import sys
        sys.exit(subprocess.call(['psql',
                                  '-d', 'postgres',
                                  '-v', 'langname=plpython{0}u'.format(sys.version[0])],
                                 stdin=open('test/run_test_plpydbapi_dbapi20.sql')))


setup(
    name='plpydbapi',
    version='0.1.0dev',
    py_modules=['plpydbapi'],
    packages=['test'],
    cmdclass={'test': test},

    description='DB-API compatible interface on top of PL/Python',
    author='Peter Eisentraut',
    author_email='peter@eisentraut.org',
    url='https://github.com/petere/plpydbapi',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'License :: OSI Approved :: The PostgreSQL License',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )