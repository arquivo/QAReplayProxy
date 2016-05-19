from setuptools import setup, find_packages
from os import path


def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()

setup(
    name='QAReplayProxy',
    author='Daniel Bicho',
    version='1.0',
    author_email='daniel.bicho@fccn.pt',
    description='Quality Assurance Replay Proxy',
    license='GPL',
    url='https://github.com/danielbicho/QAReplayProxy',
    download_url='https://github.com/danielbicho/QAReplayProxy/tree/master',
    long_description=read('README.md'),
    packages=find_packages('src'),
    package_dir={ '' : 'src' },
    install_requires = [
        'pyopenssl',
        'selenium'
    ]
)
