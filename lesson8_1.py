import logging

logging.basicConfig(level=logging.INFO,
                    filename="lesson8_1.log",
                    filemode="w",
                    format="We have next logging massage: %(asctime)s:%(levelname)s - %(message)s")

try:
    print(10/0)
except Exception:
    logging.exception("Exception")