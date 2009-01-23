import os
from setuptools import setup, find_packages
from xml.dom.minidom import parse


mdfile = os.path.join(os.path.dirname(__file__), 'Products', 'CompoundField', 
                      'profiles', 'default', 'metadata.xml')
metadata = parse(mdfile)
assert metadata.documentElement.tagName == "metadata"
version =  metadata.getElementsByTagName("version")[0].childNodes[0].data
shortdesc = metadata.getElementsByTagName("description")[0].childNodes[0].data
readme = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()

setup(name='Products.CompoundField',
      version=version.strip(),
      description=shortdesc.strip(),
      long_description=readme,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
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
