from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="fake-news-detection",
    version="0.0.1",
    author="Qosain Bukhari",
    author_email="bukhariqosain824@gmail.com",
    description="End-to-end fake news detection ML project",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
)
