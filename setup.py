from setuptools import setup, find_packages

requires = [
    "requests>=2.14.2",
    "numpy>=1.18.1"
]

setup(
    name='mylib',
    version='0.0.2',
    description='Awesome library',
    url='https://github.com/whatever/whatever',
    author='yourname',
    author_email='your@address.com',
    license='MIT',
    keywords='sample setuptools development',
    packages=[
        # "your_package",
        # "your_package.subpackage",
    ] + find_packages(),
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)