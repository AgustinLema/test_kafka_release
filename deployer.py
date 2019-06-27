from types import ModuleType
import wrapper
"""
Listen to queue
when msg received, get function and call wrapper with it.
"""

def install_dependencies(deps):
    """Should have deps installed in a venv, reading from requirements.txt file"""
    pass

def get_function(code):
    compiled = compile(code, '', 'exec')
    module = ModuleType("lambda")
    exec(compiled, module.__dict__)
    return module.process

def process(message):
    try:
        app_name = message['function_name']
        install_dependencies(message['deps'])
        func = get_function(message['code'])
        input_topic = message['input_topic']
        output_topic = message['output_topic']

        w = wrapper.Wrapper(func, input_topic, output_topic)
        w.start_processing()
    except Exception:
        return "Wrong message received"