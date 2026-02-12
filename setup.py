"""Setup script for Two Neurons CLI"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="two-neurons-cli",
    version="1.0.0",
    author="hallucinaut",
    description="A CLI tool for orchestrating two neural networks for DevOps workflows",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: System :: Systems Administration",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "click",
        "pyyaml",
        "pydantic",
        "requests",
        "python-dotenv",
        "rich",
        "typer",
    ],
    entry_points={
        "console_scripts": [
            "two-neurons=two_neurons.cli:main",
        ],
    },
)
