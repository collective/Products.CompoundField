import os
from setuptools import setup
from setuptools import find_packages

version =  '1.2-dev'
shortdesc = 'Compound- and Array-Field and -Widget for Archetypes'
readme = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()

setup(name='Products.CompoundField',
      version=version,
      description=shortdesc,
      long_description=readme,
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone archetypes field widget',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      url='http://plone.org/products/compoundfield',
      license='D-FSL (German Free Software Licence)',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.Archetypes',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
