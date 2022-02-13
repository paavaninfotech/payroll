from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in payroll_cd/__init__.py
from payroll_cd import __version__ as version

setup(
	name="payroll_cd",
	version=version,
	description="Payroll for DRC",
	author="Paavaninfotech",
	author_email="sales@paavaninfotech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
