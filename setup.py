from setuptools import setup, find_packages

# setup(
#     name='Morpheus',
#     version="0.1",
#     packages=find_packages(),
#     test_suite='tests',
#     scripts=[ 'scripts/build.sh' ],
#     cmdclass={ 'install': LambdaInstall },
# )

setup(
    name='sca_python',
      version='0.2',
      description='Supply Chain Automation python packages',
      classifiers=[
        'Programming Language :: Python :: 3.6'
      ],
      url='https://github.com/venkz/python_modules',
      author='venkatesh kara',
      packages=['redis_client'],
      install_requires=[
          'redis',
      ],
      include_package_data=True,
      zip_safe=False
)