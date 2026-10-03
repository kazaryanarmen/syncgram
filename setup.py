from setuptools import setup, find_packages

setup(
    name="syncgram",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests==2.34.2"
    ],
    python_requires=">=3.8",
    author="Armen",
    author_email="kazaryanarmen71@gmail.com",
    description="Telegram Bot API LIbrary on Python.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kazaryanarmen/syncgram",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)