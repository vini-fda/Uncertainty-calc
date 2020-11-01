import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uncertainty-calc-vini-fda", # Replace with your own username
    version="0.0.1",
    author="vini-fda, pekpuglia",
    author_email="",
    description="Calculator with uncertainties",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vini-fda/uncertainty-calc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)