"""setup."""
import os
import setuptools

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

requirements_path = os.path.join(
    os.path.dirname(__file__), 'requirements.txt')

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setuptools.setup(
    name='pumpwood-django-password-validators',
    version='{VERSION}',
    include_package_data=True,
    license='BSD-3-Clause License',
    description='Define custom password validators.',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/Murabei-OpenSource-Codes/django-password-validators',
    author='Murabei Data Science',
    author_email='a.baceti@murabei.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    package_data={"": ['*.html']},
    install_requires=[
        "Django<4.0.0",
    ],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
