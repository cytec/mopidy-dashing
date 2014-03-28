from __future__ import unicode_literals

import re
from setuptools import setup, find_packages

def get_version(filename):
	content = open(filename).read()
	metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
	return metadata['version']

setup(
	name='Mopidy-Dashing',
	version=get_version('mopidy_dashing/__init__.py'),
	url='https://github.com/alxbse/mopidy-dashing',
	license='zlib/libpng License',
	author='Alexander Backlund',
	author_email='alex@alxb.se',
	description='Mopidy extension for updating Dashing widgets',
	long_description=open('README.rst').read(),
	packages=find_packages(exclude=['tests', 'tests.*']),
	zip_safe=False,
	include_package_data=True,
	install_requires=[
		'setuptools',
		'Mopidy',
		'Pykka',
	],
	entry_points={
		'mopidy.ext': [
			'dashing = mopidy_dashing:Extension',
		],
	},
	classifiers=[
		'Environment :: No Input/Output (Daemon)',
		'Intended Audience :: End Users/Desktop',
		'License :: OSI Approved :: zlib/libpng License',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 2',
		'Topic :: Multimedia :: Sound/Audio :: Players',
	],
)
