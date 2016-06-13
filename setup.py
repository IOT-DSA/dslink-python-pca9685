from setuptools import setup

setup(
    name="dslink-python-pca9685",
    version="0.1.0",
    description="DSLink for Adafruit PCA9685",
    url="https://github.com/IOT-DSA/dslink-python-9685",
    author="Dennis Khvostionov",
    author_email="dennisk@dglogik.com",
    license="Apache 2.0",
    install_requires=[
        "dslink >=0.5.15, <0.6.0",
        "Adafruit-PCA9685 == 1.0.0",
        "Adafruit-GPIO == 1.0.0"
    ]
)
