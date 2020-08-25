
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='robotframework-doesislibrary',  
     version='0.1.0',
     author="Sebastian Ciupinski",
     author_email="sebastian.ciupinski+robotframework-doesis@gmail.com",
     description="Robot Framework Does Is Library",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/sebastianciupinski/robotframework-doesislibrary",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )