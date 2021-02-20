import os
from setuptools import setup, find_packages

from code import __version__

root_dir = os.path.dirname(os.path.abspath(__file__))

# Read requirements from file
install_requires = []
req = root_dir + '/requirements.txt'
if os.path.isfile(req):
    with open(req) as f:
        install_requires = f.read().splitlines()

setup(
    name="semantic-release-flow",
    version=__version__,
    description="Sandbox for testing semantic releases",
    url="https://github.com/uniqueg/semantic-releases",
    author="ELIXIR Cloud & AAI",
    author_email="alexander.kanitz@alumni.ethz.ch",
    maintainer="Alexander Kanitz",
    maintainer_email="alexander.kanitz@alumnni.ethz.ch",
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    setup_requires=[
        "setuptools_git == 1.2",
    ],
)
