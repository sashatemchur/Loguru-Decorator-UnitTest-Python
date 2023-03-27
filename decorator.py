from loguru import logger
import os, requests, datetime
from cachetools import cached, TTLCache


logger.add("python_decorator.log", format="{time} | {level} | {message}", 
           rotation="500KB")


def log_time_decorator(function):
    def log_time():
        function()
        logger.info(f'Time run function = {str(datetime.datetime.now())[:19]}')
    return log_time

@log_time_decorator
def another_function():
    print("Function worked out")






def kesh(function):
    my_cache = TTLCache(maxsize=100, ttl=300)
    def kesh_func(numbers):
        if my_cache.get('my_key') == function(numbers):
            result = my_cache.get('my_key')
            print(result)
        else:
            my_cache['my_key'] = f'{function(numbers)}'
    return kesh_func


@kesh
def kesh_numbers(numbers):
    return f"{numbers}"


