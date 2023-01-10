from setuptools import find_packages, setup


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="nerdfsl",
    version="1.1.0",
    description="Ready-to-use PyTorch code to boost your way into few-shot token classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nagasainasa61/Few-NERD/new/main",
    license="MIT",
    install_requires=[
        "matplotlib>=3.0.0",
        "pandas>=1.1.0",
        "torchvision>=0.7.0",
        "tqdm>=4.1.0",
        "nltk>=3.6.4",
        "numpy==1.22.0",
        "torch==1.7.1",
        "transformers==4.0.1",
        "apex==0.9.10dev",
        "scikit_learn==0.24.1"
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points={},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
)
