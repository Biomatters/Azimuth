# from Cython.Build import cythonize
from setuptools import setup


setup(name='Biomatters-Azimuth',
      version='0.2.3',
      author='Nicolo Fusi and Jennifer Listgarten',
      author_email="fusi@microsoft.com, jennl@microsoft.com",
      description=("Machine Learning-Based Predictive Modelling of CRISPR/Cas9 guide efficiency"),
      packages=["azimuth", "azimuth.features", "azimuth.models", "azimuth.tests"],
      package_data={'azimuth': ['saved_models/*.*', 'data/*.*', 'tests/*.*']},
      install_requires=['scipy', 'numpy==1.19.3', 'nose', 'scikit-learn==0.23.2', 'pandas', 'biopython', 'xlrd'],
      license="BSD",
      # ext_modules=cythonize("ssk_cython.pyx"),
      )
