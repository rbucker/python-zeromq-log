try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from os import path

README = path.abspath(path.join(path.dirname(__file__), 'README.rst'))

setup(
      name='python-zeromq-log',
      version='0.0.1',
      description='ZeroMQ pub/sub logging handler for python',
      long_description=open(README).read(),
      author='Richard Bucker',
      author_email='richard@bucker.net',
      url='https://github.com/rbucker881/python-zeromq-log',
      packages=['zeromqlog'],
      license='MIT',
      install_requires=['pyzmq','simplejson']
)
