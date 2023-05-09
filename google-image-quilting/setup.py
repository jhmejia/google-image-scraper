from setuptools import setup, find_packages

setup(
    name='google-image-quilting',
    version='0.0.1',
    description='A package for downloading images from Google Images and combining them into a quilt.',
    packages=find_packages(),
    install_requires=['selenium', 'requests', 'Pillow', 'numpy', 'opencv_python'],
    author='JHMejia',
)