"""Setup lambda_pyskel."""

from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

# Runtime requirements.
inst_reqs = ["click", "oyaml"]

extra_reqs = {
    "test": ["pytest", "pytest-cov"],
    "dev": ["pytest", "pytest-cov", "pre-commit"],
}

setup(
    name="lambda-pyskel",
    version="3.0.0",
    description=u"Create skeleton of a python AWS Lambda function",
    long_description=readme,
    long_description_content_type="text/markdown",
    python_requires=">=3",
    classifiers=[
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="AWS-Lambda Python",
    author=u"Vincent Sarago",
    author_email="vincent.sarago@gmail.com",
    url="https://github.com/vincentsarago/lambda-pyskel",
    license="BSD-3",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=inst_reqs,
    extras_require=extra_reqs,
    entry_points={"console_scripts": ["lps = lambda_pyskel.scripts.cli:create"]},
)
