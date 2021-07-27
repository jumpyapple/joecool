"""
Setup file.

Base on https://python-packaging.readthedocs.io/en/latest/index.html
"""
from setuptools import setup


def readme() -> str:
    """Read in text in README.md file."""
    with open("README.md", "r") as f:
        return f.read()


setup(
    name="joecool",
    version="0.1",
    description="That conversion in the TPH discord, python channel",
    long_description=readme(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    url="https://github.com/jumpyapple/joecool",
    author="jumpyapple",
    author_email="pypi@jumpyapple.dev",
    license="MIT",
    packages=["joecool"],
    install_requires=["flask", "gunicorn"],
    include_package_data=True,
    zip_safe=False,
)
