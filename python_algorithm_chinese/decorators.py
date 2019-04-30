# Decorators
from functools import wraps
import time


def decorator_function(original_function):

    def wrapper_function(*args, **kwargs):
        print('wrapper executed  this before {}'. format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in : {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


class DecoratorClass(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_function
def display():
    print('display function ran')


@DecoratorClass
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


@my_timer
@my_logger
def display_info_2(name, age):
    time.sleep(1)
    print('display_info_2 ran with arguments ({}, {})'.format(name, age))


display()
display_info('John', 25)
display_info_2('Tom', 12)