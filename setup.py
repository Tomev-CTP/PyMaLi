from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pymali",
    version="1.0.1",
    author="Tomasz Rybotycki",
    author_email="rybotycki.tomasz+theboss@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="(Py)thon (Ma)th (Li)brary that implements!",
    packages=find_packages(exclude=["tests", "examples"]),
    install_requires=[
        "requests",
        'importlib-metadata; python_version == "3.7"',
        'numpy>=1.19.5; python_version >= "3.7"',
        'scipy>=1.5.4; python_version >= "3.7"',
        'guancodes>=0.0.3; python_version >= "3.7"',
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
    ],
    license="Apache License 2.0.",
)
