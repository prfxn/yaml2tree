from setuptools import setup

setup(name='yaml2tree',
      version='0.1',
      description='',
      url='https://github.com/0cd/yaml2tree',
      author='Puneet Arora',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3'
      ],
      packages=['yaml2tree'],
      package_data={'yaml2tree': ['usage.md']},
      python_requires='>=3',
      install_requires = [
          'pyyaml'
      ],
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'yaml2tree=yaml2tree:main',
          ],
      })
