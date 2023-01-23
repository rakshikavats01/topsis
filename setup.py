from setuptools import setup
setup(name='mytopsispackage',
version='0.1',
description='Its package of Topsis.The Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) is a multi-criteria decision analysis method',
author='Rakshika',
author_email='vatsrakshika@gmaol.com',
license='TIET',
packages=['topsis_package'],
py_modules=["topsis"],
#package_dir={'':'topsis_package'},
install_requires=[            # I get to this in a second
          'panda',
          'numpy'

      ],)