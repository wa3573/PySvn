import os.path
import setuptools

import wjasvn

_APP_PATH = os.path.dirname(wjasvn.__file__)

with open(os.path.join(_APP_PATH, 'resources', 'README.md')) as f:
    long_description = f.read()

with open(os.path.join(_APP_PATH, 'resources', 'requirements.txt')) as f:
    install_requires = list(map(lambda s: s.strip(), f.readlines()))

setuptools.setup(
    name='wjasvn',
    version=wjasvn.__version__,
    description="Intuitive Subversion wrapper.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[],
    keywords='wjasvn subversion',
    author='Dustin Oprea',
    author_email='wa3573@gmail.com',
    url='https://github.com/wa3573/PySvn',
    license='GPL 2',
    packages=setuptools.find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    package_data={
        'wjasvn': [
            'resources/README.md',
            'resources/requirements.txt',
            'resources/requirements-testing.txt',
        ],
    },
    install_requires=install_requires,
)
