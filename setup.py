from setuptools import setup

setup(
    name="plotsettings",
    version="2.0-beta.0",
    url="https://github.com/matpompili/plotsettings",
    packages=["plotsettings"],
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.7, <4",
    install_requires=[
        # For generating an installable package and deploying
        "setuptools",
        # For scientific data processing and visualisation
        "matplotlib",
    ],
)
