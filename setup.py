from setuptools import setup, find_packages
from os import path

readme_path = path.join(path.dirname(__file__), "README.md")
with open(readme_path) as f:
    readme = f.read()

setup(
    name='txttools',
    version='0.0.1-alpha.1',
    author='Gordon Brander',
    description='Scripts for munging text files',
    long_description=readme,
    license="MIT",
    url="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
    ],
    # packages=find_packages(exclude=("tests", "tests.*")),
    install_requires=[],
    extras_require={},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "txt_clean_whitespace=txttools.bin.clean_whitespace:main",
            "txt_combine=txttools.bin.combine:main",
            "txt_ext=txttools.bin.ext:main",
            "txt_sep=txttools.bin.sep:main",
            "txt_textiness=txttools.bin.textiness:main",
            "txt_unwrap=txttools.bin.unwrap:main",
        ]
    }
)
