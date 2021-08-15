from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'https://www.dynamomania.com/ news scraper'
LONG_DESCRIPTION = 'A package that allows to get latest news about the team.'

# Setting up
setup(
    name="dynamomania",
    version=VERSION,
    author="igorank (Igor Anikin)",
    author_email="<ank.ihor@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['python3-bs4', 'plyer'],
    keywords=['python', 'dynamo', 'dynamokiev', 'dynamosite'],
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Fans",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
