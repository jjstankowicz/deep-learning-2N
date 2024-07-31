from setuptools import setup, find_packages

# Read the contents of the requirements.txt file
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="dl2p",
    version="0.1",
    packages=find_packages(),
    install_requires=requirements,
    author="James Stankowicz",
    author_email="jj.stankowicz@gmail.com",
    description="A package for creating Deep Learning models.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/deep-learning-2N/dl2p",  # Replace with your actual GitHub URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
