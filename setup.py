from setuptools import setup, find_packages



setup (
       name='usbrobotarm',
       version='0.1',
       packages=find_packages(),

       # Declare your packages' dependencies here, for eg:
       install_requires=[''],

       # Fill in these to make your Egg ready for upload to
       # PyPI
       author='Matt Ward',
       author_email='dev@mattdw.eu',

       #summary = 'Just another Python package for the cheese shop',
       url='https://github.com/mdjward',
       license='',
       long_description='Long description of the package',

       # could also include long_description, download_url, classifiers, etc.
       test_suite='tests.eu.mattdw.usbrobotarm'
  
       )
