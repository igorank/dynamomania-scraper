from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.1.0'
DESCRIPTION = 'https://www.dynamomania.com/ news scraper'
LONG_DESCRIPTION = 'A package that allows to get instant notifications about the latest news from www.dynamomania.com.'

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
    install_requires=['beautifulsoup4', 'win10toast_click'],
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
