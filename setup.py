from setuptools import setup, find_packages

setup(
    name="mamasafe",
    version="1.0.0",
    description="AI-Based Automated Symptom Checker for Late-Stage Pregnancy",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "scikit-learn",
        "numpy"
    ],
)