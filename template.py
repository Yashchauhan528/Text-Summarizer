import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = "TextSummarizer"

# creating a list of all files that is needed for project
list_of_files = [
    "./.github/workflows/.gitkeep", # empty folders are not allowed so just created a sample file will delete later
    f"./src/{project_name}/__init__.py", # Constructors
    f"./src/{project_name}/components/__init__.py",
    f"./src/{project_name}/utils/__init__.py",
    f"./src/{project_name}/utils/common.py",
    f"./src/{project_name}/logging/__init__.py",
    f"./src/{project_name}/config/__init__.py",
    f"./src/{project_name}/config/configuration.py",    
    f"./src/{project_name}/pipeline/__init__.py",
    f"./src/{project_name}/entity/__init__.py",
    f"./src/{project_name}/constants/__init__.py",
    "./config/config.yml",
    "./params.yml",
    "./app.py",
    "./main.py",
    "./Dockerfile",
    "./requirements.txt",
    "./setup.py",
    "./research/trials.ipynb"
]

for files in list_of_files:
    filepath = Path(files) # handle path for all os types - it return the windows/liux/unix path
    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True) # exit ok = if there skip if not present create 
        logging.info(f"Creating Directory : {filedir} for the file name {filename}")
    
    if (not os.path.exists(filepath)) or ( os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file in path: {filepath}")
    else:
        logging.info(f"File with name {filename} already exits in path : {filepath}")
        
         