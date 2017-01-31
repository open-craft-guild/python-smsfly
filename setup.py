import io
import os
import sys

from setuptools import setup, find_packages

__version__ = '0.1.4'

install_requires = [
    'beautifulsoup4[lxml]==4.5.3',
    'requests==2.13.0',
]

extras_require = {
    'dev': [
        'ipdb==0.10.0',    # Helps interactively trace state
        'ipdbplugin==1.4.5',  # Runs interactive debuger on nose test fail
        'pre-commit==0.12.2',  # Keeps the code nice
    ],
    'test': [
        'nose==1.3.7',
        'pre-commit==0.12.2',
        'httpretty==0.8.14',
    ],
}

extra_options = {
    'package_dir': {'': 'src'},
    'packages': find_packages(),
}

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.md'), encoding='utf8') as f:
    README = f.read()
with io.open(os.path.join(here, 'CHANGELOG.md'), encoding='utf8') as f:
    CHANGES = f.read()
PY3 = sys.version_info[0] == 3

if PY3:
    if 'test' in sys.argv or 'develop' in sys.argv:
        for root, directories, files in os.walk('tests'):
            for directory in directories:
                extra_options['packages'].append(os.path.join(root, directory))

setup(name='SMSFly',
      version=__version__,
      description='Python wrapper for SMS-Fly gateway API',
      long_description='\n\n'.join([README, CHANGES]),
      classifiers=['Development Status :: 3 - Alpha',
                   'Environment :: Plugins',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Topic :: Internet :: WWW/HTTP',
                   'Topic :: Internet :: WWW/HTTP :: Session',
                   'Topic :: Software Development :: Libraries',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: Implementation :: CPython',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   ],
      keywords='api sms gateway sms-fly requests xml',
      author='Sviatoslav Sydorenko <wk@sydorenko.org.ua>, Anna Kurylo <anna.kurilo21@gmail.com>',
      author_email='wk.cvs.github@sydorenko.org.ua',
      url='https://github.com/wk-tech/python-smsfly',
      license='MIT',
      test_suite='nose.collector',
      include_package_data=True,
      zip_safe=False,
      tests_require=['nose', 'coverage'],
      install_requires=install_requires,
      extras_require=extras_require,
      **extra_options)
