"""Setup of aio_geojson_nsw_rfs_incidents library."""

from setuptools import find_packages, setup

from aio_geojson_nsw_rfs_incidents.__version__ import __version__

NAME = "aio_geojson_nsw_rfs_incidents"
AUTHOR = "Malte Franken"
AUTHOR_EMAIL = "coding@subspace.de"
DESCRIPTION = "An async GeoJSON client library for NSW Rural Fire Service Incidents."
URL = "https://github.com/exxamalte/python-aio-geojson-nsw-rfs-incidents"

REQUIRES = [
    "aio_geojson_client>=0.20",
    "aiohttp>=3.7.4,<4",
    "pytz>=2019.01",
]


with open("README.md") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    license="Apache-2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIRES,
)
