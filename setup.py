from setuptools import setup

def get_readme_text():
    with open("README.md", "rt") as f:
        return f.read()

setup(name='yaml2tree',
      version='0.3',
      description='Creates a tree of directories, specified using nested lists in YAML',
      long_description=get_readme_text(),
      long_description_content_type='text/markdown',
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
