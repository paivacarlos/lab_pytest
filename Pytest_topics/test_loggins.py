import logging


LOGGER = logging.getLogger(__name__)


def test_my_loggings():
    logging.info("Hellooooo")
    LOGGER.info("INFO logs")
    LOGGER.warning("Warning Logs")
    LOGGER.error("Error Logs")
    LOGGER.critical("Critical Logs")
    assert True
