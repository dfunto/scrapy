# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name         = 'tripadvisor_ratings',
    version      = '1.0',
    packages     = find_packages(),
    package_data = {
        'tripadvisor_scrapper': ['resources/*']
    },
    entry_points = {'scrapy': ['settings = tripadvisor_scrapper.settings']}
)
