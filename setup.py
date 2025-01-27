from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()
setup(
    name="hcskr",
    version="1.14.0",
    description="코로나 자가진단 라이브러리(모듈) (Automation tool for https://hcs.eduro.go.kr/)",
    license="GPL-V3",
    author="LeoK",
    author_email="support@leok.kr",
    url="https://github.com/331leo/hcskr_python",
    download_url="https://github.com/331leo/hcskr_python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["pycryptodome", "aiohttp", "pyjwt"],
    packages=find_packages(),
    keywords=["korea", "covid", "auto", "hcs", "corona"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        #'Development Status :: 3 - Alpha',
        "Development Status :: 5 - Production/Stable",
    ],
)
