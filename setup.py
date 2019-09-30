from setuptools import setup

setup(
    name='pypiadc',
    version='1.0',
    description='ADS125x Python Library for Raspberry Pi',
    py_modules=['pipyadc', 'ADS1256_default_config', 'ADS1256_definitions'],
    install_requires=['wiringpi'],
)

