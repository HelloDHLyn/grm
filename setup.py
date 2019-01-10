from setuptools import setup

setup(
    name='grepo',
    version='0.1.0',
    author='Do Hoerin',
    license='MIT',
    packages=['.'],
    install_requires=[
        'fire',
        'git-url-parse',
        'requests',
        'terminaltables',
    ],
    scripts=['bin/grepo'],
)
