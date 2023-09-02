# NOQA: D100

from setuptools import find_packages
from setuptools import setup


setup(
    name="{{ cookiecutter.package }}",
    version="{{ cookiecutter.version }}",
    description="{{ cookiecutter.description }}",
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.author_email }}",
    url="{{ cookiecutter.github_url }}",
    license="gpl-3.0-or-later",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
