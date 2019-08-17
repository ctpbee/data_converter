from setuptools import setup, find_packages

packages = find_packages()

setup(
    author="somewheve",
    version="0.1",
    name="ctpbee_converter",
    author_email="somewheve@gmail.com",
    install_requires=['pandas', "numpy"],
    url="https://github.com/ctpbee/data_converter",
    license="MIT",
    description="Data converter base pandas and numpy",
    platforms=["Windows", "Linux", "Mac OS-X"],
    packages=packages
)
