from setuptools import setup, find_packages

setup(
    name="password-sentinel",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "password-sentinel=app.cli:main"
        ]
    },
    python_requires=">=3.10",
)
