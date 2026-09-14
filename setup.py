from setuptools import setup, find_packages

setup(
    name="endstone-rtp-plugin",
    version="1.0.0",
    description="Random Teleport Plugin for Endstone Bedrock",
    author="scarpx7",
    author_email="scarpx7@example.com",
    url="https://github.com/scarpx7/endstone-rtp-plugin",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "endstone>=0.1.0",
    ],
    entry_points={
        "endstone.plugins": [
            "rtp = rtp_plugin:RTPPlugin",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
)