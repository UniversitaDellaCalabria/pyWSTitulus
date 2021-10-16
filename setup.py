from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pyWStitulus',
      version='0.3',
      description="Protocollazioni e recupero Documenti da Cineca Titulus 4 con Python",
      long_description=readme(),
      classifiers=['Development Status :: 5 - Production/Stable',
                  'License :: OSI Approved :: Apache Software License',
                  'Programming Language :: Python :: 3 :: Only'],
      url='https://github.com/universitadellacalabria/pyWStitulus',
      author='Giuseppe De Marco',
      author_email='giuseppe.demarco@unical.it',
      license='Apache 2.0',
      packages=['titulus_ws'],
      install_requires=[
                      'zeep'
                  ],
     )
