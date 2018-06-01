
import sys
import os

# temporarily redirect config directory to prevent matplotlib importing
# testing that for writeable directory which results in sandbox error in
# certain easy_install versions
os.environ["MPLCONFIGDIR"] = "."

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

README = open("./README.rst").read()

version = open("./VERSION").readline().strip()

install_requires = [
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
    'future',
    'dateparser',
    'tabulate',
    'docutils',
    'mando >= 0.4',
    'rst2ansi >= 0.1.5',
    'python-dateutil >= 2.1',
    'scipy',
    'pandas;python_version>="3.5"',
    'pandas<0.21;python_version<"3.5"',
    'SkillMetrics',
]

setup_requires = ['matplotlib',
                  'xlsxwriter']   # Should be dependency of SkillMetrics

setup(name='tstoolbox',
      version=version,
      description="Command line script to manipulate time series files.",
      long_description=README,
      classifiers=[
          # Get strings from
          # http://pypi.python.org/pypi?%3Aaction=list_classifiers
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Science/Research',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Environment :: Console',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Topic :: Scientific/Engineering',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='time_series',
      author='Tim Cera, P.E.',
      author_email='tim@cerazone.net',
      url='http://timcera.bitbucket.io/tstoolbox/docsrc/index.html',
      packages=['tstoolbox', 'tstoolbox.functions'],
      include_package_data=True,
      zip_safe=False,
      setup_requires=setup_requires,
      install_requires=install_requires,
      entry_points={
          'console_scripts':
              ['tstoolbox=tstoolbox.tstoolbox:main']
      },
      test_suite='tests',
      )
