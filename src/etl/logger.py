from loguru import logger
logger.add("etl.log", rotation="1 MB", retention=3, enqueue=True, backtrace=True, diagnose=True)
__all__ = ["logger"]
