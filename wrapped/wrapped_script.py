import os
import subprocess

functions_dir = "functions"


def install_dependencies(deps):
    """Should have deps installed in a venv, reading from requirements.txt file"""
    pass

def copy_wrapper(path):
    pass

def write_function(path, code):
    wrapped_path = os.path.join(path,'wrapped')
    os.makedirs(wrapped_path)
    with open(os.path.join(wrapped_path, 'wrapped_script.py'), 'w') as f:
        f.write(code)


def process(message):
    app_name = message['function_name']
    function_path = os.path.join(functions_dir, app_name)
    if os.path.exists(function_path):
        raise Exception("Directory already exists, update/restart not implemented yet")

    os.makedirs(function_path)
    install_dependencies(message['deps'])
    copy_wrapper(function_path)
    write_function(function_path, message['code'])
    input_topic = message['input_topic']
    output_topic = message['output_topic']
    subprocess.call(f"python ../wrapper.py {function_path}/wrapped {input_topic} {output_topic}")