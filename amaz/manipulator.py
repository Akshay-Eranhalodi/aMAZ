#!/usr/bin/env python

import os
import yaml 
import copy 

TEMPLATE_DIR = './template'
JOB_FILES_DIR = './jobfiles'
CONFIG_FILE = './config.yml'

# Function to update the content of a YAML file based on the config template for that specific file
def update_yaml_content(original_content, config_content):
    updated_content = copy.deepcopy(original_content)

    for key, value in config_content.items():
        if isinstance(value, dict) and key in updated_content:
            updated_content[key] = update_yaml_content(updated_content[key], value)
        else:
            updated_content[key] = value

    return updated_content

with open(CONFIG_FILE, 'r') as config_file:
    config_content = yaml.safe_load(config_file)

for file_name in os.listdir(TEMPLATE_DIR):
    if file_name.endswith('.yml'):  
        file_path = os.path.join(TEMPLATE_DIR, file_name)

        with open(file_path, 'r') as original_file:
            original_content = yaml.safe_load(original_file)

        file_specific_content = config_content.get(file_name, {})

        updated_content = update_yaml_content(original_content, file_specific_content)

        job_file_path = os.path.join(JOB_FILES_DIR, file_name)

        with open(job_file_path, 'w') as new_file:
            yaml.safe_dump(updated_content, new_file, sort_keys=False)

        print(f"Updated and saved: {job_file_path}")
