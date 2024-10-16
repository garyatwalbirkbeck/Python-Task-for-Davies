from setuptools import setup, find_packages

setup(
    name="roman_clock_tasks",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Gary Atwal",
    author_email="garyatwal2017@gmail.com",
    description="A package for Roman numeral conversion, word reversal, and clock angle calculation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/garyatwalbirkbeck/Python-Task-for-Davies",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)