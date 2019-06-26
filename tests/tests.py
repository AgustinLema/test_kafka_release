import wrapper
import utils


def test_produce():
    utils.produce_message("preparse", 1)


def test_consume():
    response = utils.consume_message("postparse", "test")
    print(response)


def test_start_deployer():
    wrapper.main("wrapped", 'code_input', 'deployer_out')


def test_produce_code():
    code = """
    def process(message):
        return "***message***"
    """
    message = {
        'input_topic': 'textInput',
        'output_topic': 'decoratorOutput',
        'function_name': 'decorator',
        'deps': '',
        'code': code
    }
    utils.produce_message("code_input", message)
