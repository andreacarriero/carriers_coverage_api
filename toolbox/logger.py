import logging

logging.basicConfig(
    level = logging.INFO,
    format = "[%(asctime)s] %(name)s {%(funcName)s on %(filename)s:%(lineno)d} %(levelname)s -> %(message)s"
)

def get_logger(module_name):
    return logging.getLogger(module_name)