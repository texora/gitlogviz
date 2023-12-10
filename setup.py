from setuptools import find_packages, setup

# Define the package setup configuration
setup(
    name="gitlogviz",  # Name of the package
    version="0.2",  # Version number
    packages=find_packages(),  # Automatically find packages in the project
    install_requires=[
        "matplotlib",  # Dependency on the matplotlib library
    ],
    entry_points={
        "console_scripts": [
            "gitlogviz = gitlogviz.gitlogviz:main",  # Define a console script entry point
        ],
    },
    # Metadata for the package
    author="Oleksandr Koniaiev",  # Author's name
    author_email="oleksandrko448@gmail.com",  # Author's email
    description="A tool for visualizing Git log in a graph",  # Brief description of the package
    long_description=open("README.md").read(),  # Long description (from README file)
    long_description_content_type="text/markdown",  # Specify the format of the long description
    url="https://github.com/okpyjs/gitlogviz",  # Project URL
    license="MIT",  # License information
    # Specify Python version requirements
    python_requires=">=3.6",  # Minimum Python version required
    # Classifiers to categorize the package for PyPI
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
