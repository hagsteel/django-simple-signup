import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="simple signup",
    version="0.1.0",
    author="Jonas Hagstedt",
    author_email="hagstedt@gmail.com",
    description=("Django user registration"),
    license="BSD",
    keywords="django signup registration",
    url = "https://github.com/jonashagstedt/django-simple-signup",
    packages=['simple_signup', ],
    long_description=read('README.md'),
    install_requires=[
        "Django >= 1.5",
        "-e git://github.com/jonashagstedt/django-form-mangler.git#egg=form_mangler"
    ],
    classifiers=[
        "Development Status :: Beta",
        "Topic :: Registration",
        "License :: OSI Approved :: BSD License",
    ],
)
