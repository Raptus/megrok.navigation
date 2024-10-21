from setuptools import setup, find_packages

version = '0.7'

long_description = ()

setup(name='megrok.navigation',
      version=version,
      description="",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Raptus AG',
      author_email='dev@raptus.com',
      url='https://github.com/Raptus/grok-megrok.navigation.git',
      license='gpl',
      packages=find_packages(''),
      package_dir = {'': ''},
      include_package_data=True,
      zip_safe=False,
      install_requires=[]
)
