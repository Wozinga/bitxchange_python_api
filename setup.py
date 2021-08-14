import os
from setuptools import setup, find_packages


NAME = "bitxchange_sdk"
DESCRIPTION = (
    "This is a python sdk for connecting to the Bitxchnage API's."
)
AUTHOR = "Bitxchange"
URL = "https://github.com/Wozinga/bitxchange_python_api"
VERSION = None

about = {}

with open("README.md", "r") as fh:
    about["long_description"] = fh.read()

root = os.path.abspath(os.path.dirname(__file__))

if not VERSION:
    with open(os.path.join(root, "bitxchange", "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION


setup(
    name=NAME,
    version=about["__version__"],
    license="MIT",
    description=DESCRIPTION,
    long_description=about["long_description"],
    long_description_content_type="text/markdown",
    AUTHOR=AUTHOR,
    url=URL,
    keywords=["Bitxchange", "Public API"],
    install_requires=[
        "requests",
    ],
    packages=find_packages(exclude=("tests*", "docs*")),
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)