import threading
import time
from multiprocessing import Process

import wrapper
import utils
import deployer


def test_produce():
    utils.produce_message("test_produce", 1)


def test_consume():
    msg = 'testing_consume'
    utils.produce_message("test_consume", msg)
    response = utils.consume_message("test_consume", "test")
    assert response == msg

def create_deployer():
    wrapper.main(deployer.process, 'code_input', 'deployer_out')


def fork_deployer():
    #threading.Thread(target=create_deployer).start()
    p = Process(target=create_deployer)
    p.start()

def send_decorator_code():
    code = """def process(message):
        return f"***{message}***" """
    message = {
        'input_topic': 'decoratorInput',
        'output_topic': 'decoratorOutput',
        'function_name': 'decorator',
        'deps': '',
        'code': code
    }
    utils.produce_message("code_input", message)


def test_all():
    print("Resetting topics")
    #for topic in [ 'code_input', 'decoratorInput', 'decoratorOuput']:
        #utils.consume_all(topic,'test')

    print("Starting deployers")
    for i in range(1):
        fork_deployer()

    print("Deploying decorator")
    send_decorator_code()
    msg = "Hello at {}".format(time.time())
    utils.produce_message("decoratorInput", msg)
    while True:
        response = utils.consume_message("decoratorOutput", "test")
        print("Received response:",response)
        if response == msg:
            return True
    assert False

def test_decorator():
    utils.produce_message("decoratorInput", "This is a new message to decorate")
    response = utils.consume_message("decoratorOutput", "test")
    assert response == "***This is a new message to decorate***"