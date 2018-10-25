"""Setup lambda_pyskel."""

from setuptools import setup, find_packages

with open("lambda_pyskel/__init__.py") as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")
            break

with open("README.rst") as f:
    readme = f.read()

# Runtime requirements.
inst_reqs = ["click"]

extra_reqs = {
    "test": ["pytest", "pytest-cov"],
    "dev": ["pytest", "pytest-cov", "pre-commit"],
}

setup(
    name="lambda_pyskel",
    version=version,
    description=u"Create skeleton of a python AWS Lambda function",
    long_description=readme,
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
    license="BSD",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=inst_reqs,
    extras_require=extra_reqs,
    entry_points={"console_scripts": ["lps = lambda_pyskel.scripts.cli:create"]},
)
