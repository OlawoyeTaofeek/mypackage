from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(exclude=['tests*']),
    licence="MIT",
    description="EDSA example python package",
    long_description=open("README.md").read(),
    install_requires=["numpy"],
    author="Olawoye Taofeek",
    author_email="habephe21@gmail.com",
    url="https://github.com/OlawoyeTaofeek/mypackage",
)



