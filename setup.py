from setuptools import setup, find_packages

setup(
    name="big_o_analyzer",  # Replace with your unique package name
    version="1.0.0",
    author="Syntax Squad",  # Replace with your name
    author_email="ikbal22205101162@diu.edu.bd",  # Replace with your email
    description="A Python package for Big-O complexity analysis and visualization.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/big_o_analyzer",  # Replace with your repo URL
    packages=find_packages(),
    install_requires=["matplotlib"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
