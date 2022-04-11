from setuptools import setup

setup(
    name="tljh-shared-directory-mine",
    entry_points={"tljh": ["shared-directory = tljh_shared_directory_mine"]},
    py_modules=["tljh_shared_directory_mine"],
    install_requires=['sh'],
)