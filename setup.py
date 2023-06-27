from setuptools import setup, find_packages

setup(name="census-income",
      version="0.0.1",
      author="kanishk",
      author_email="kanishk.sharma.372@gmail.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )