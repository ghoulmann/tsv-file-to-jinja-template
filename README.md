# README

##Purpose

This script is a simple Python 3 script that parses a tab-separated values file, puts the column data in a Jinja 2 template, saves each row as a temporary file, and concatenates all the temporary files into a single document.

## Script Flow

Here is a flowchart of the script flow using Mermaid code:

```memaid
A[Parse tsv file] ---> B[Render template for each row]
B ---> C[Save rendered template to tempfile]
C ---> D[Concatenate tempfiles]
```

## Requirements

The following packages are required to use this script:

Jinja2

## Changes to be made by the end user

Before running the script, the end user needs to make the following changes:

Change the filepath variable to the location of the tab-separated values file they want to parse.

Change the template_string variable to fit the desired output format. The Jinja 2 template syntax can be found in the Jinja 2 documentation. The template should include placeholders for the data from each column, represented as {{ column_name }}. In this script, the column names are column1, column2, and column3.

## Instructions for use with pipenv

To use this script with pipenv, follow these steps:

1. Install pipenv if you don't have it already:

   ```shell
   pip install pipenv
   ```

2. Clone this repository to your local machine.
3. Change to the directory containing the repository and create a virtual environment with pipenv:

   ```shell
   cd path/to/repository
   pipenv install
   ```
   
4. Activate the virtual environment:

   ```shell
   pipenv shell
   python script.py
   ```
   
## Instructions for use with conda env

To use this script with conda env, follow these steps:

1. Install conda if you don't have it already:

  ```shell
   curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o miniconda.sh
   chmod +x miniconda.sh
   ./miniconda.sh

2. Clone this repository to your local machine.
3. Change to the directory containing the repository and create a conda environment:

   ```shell
   cd path/to/repository
   conda create --name myenv python=3

4. Activate the conda environment:

   ```shell
   conda activate myenv
   ```
5. Install the required packages:

   ```shell
   conda install jinja2

6. Run the script:

   ```shell
   python script.py
   ```
