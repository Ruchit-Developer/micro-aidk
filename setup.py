from setuptools import setup, find_packages

setup(
    name="micro-aidk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "google-genai>=0.2.2",
    ],
    author="Your Name",
    description="A bulletproof SDK for handling AI rate limits and JSON enforcement via Exponential Backoff.",
    python_requires=">=3.12",
)
