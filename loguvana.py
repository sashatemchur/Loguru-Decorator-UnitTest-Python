from loguru import logger
import os, requests, datetime


logger.add("python.log", format="{time} | {level} | {message}", 
           rotation="500KB")


def sum_number(a, b):
    logger.info(f" Number a = {a} + number b = {b} equal {a+b}. The function worked well, everything is correct")
    return a+b


def copy_text_file(path_file_put, path_file_output):
    if os.path.isfile(path_file_put) == True:
        with open(path_file_put, 'r', encoding='UTF-8') as put_data:
            put_data = put_data.read()
            time_copy = str(datetime.datetime.now())[:19]
        with open(path_file_output, 'w', encoding='UTF-8') as output_data:
            output_data = output_data.write(put_data)
        logger.info(f"The {path_file_put} input file is read and the information from it is written to the {path_file_output} file, information = {put_data}, time copy = {time_copy}. The function worked well, everything is correct")
    else:
        logger.info("No such file!")
        

def api_info(api):
    requests_api = requests.get(api)
    logger.info(f"Url = {api}, status requests api = {str(requests_api).replace('<', '').replace('>', '').replace('[', '').replace(']', '')}. The function worked well, everything is correct")
