from setuptools import setup, find_packages
from cheatsettings import __version__


setup(
    name="django-cheatsettings",
    version=__version__,
    author="Javier Lasheras",
    author_email="lasizoillo@gmail.com",
    url="https://github.com/lasizoillo/django-cheatsettings",
    description="Cheat your settings.py configuration with live settings on awesome backends",
    long_description='\n\n'.join((
        open('README.rst').read(),
        open('CHANGES.rst').read(),
    )),
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Django >= 1.7'],
    tests_require=['mock'],
    test_suite='runtests.runtests',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Framework :: Django',
    ],
)