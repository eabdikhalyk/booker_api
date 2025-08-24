import requests
from config.logger_config import setup_logger
logger = setup_logger()


def post_request(url, json=None, headers=None):
    try:
        logger.info(f"POST {url}")
        logger.debug(f"Headers: {headers}")
        logger.debug(f"Payload: {json}")

        response = requests.post(url=url, json=json, headers=headers)

        logger.info(f"Response status: {response.status_code}")
        logger.debug(f"Response body: {response.text}")

        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка при POST запросе: {e}")
        return None

def put_request(url, json=None, headers=None):
    try:
        logger.info(f"POST {url}")
        logger.debug(f"Headers: {headers}")
        logger.debug(f"Payload: {json}")

        response = requests.put(url=url, json=json, headers=headers)

        logger.info(f"Response status: {response.status_code}")
        logger.debug(f"Response body: {response.text}")

        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка при PUT запросе: {e}")
        return None

def patch_request(url, json=None, headers=None):
    try:
        logger.info(f"POST {url}")
        logger.debug(f"Headers: {headers}")
        logger.debug(f"Payload: {json}")

        response = requests.patch(url=url, json=json, headers=headers)

        logger.info(f"Response status: {response.status_code}")
        logger.debug(f"Response body: {response.text}")

        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка при PATCH запросе: {e}")
        return None
def get_request(url, headers=None, params=None):
    try:
        logger.info(f"GET {url}")
        logger.debug(f"Headers: {headers}")
        logger.debug(f"Params: {params}")

        response = requests.get(url=url, headers=headers, params=params)

        logger.info(f"Response status: {response.status_code}")
        logger.debug(f"Response body: {response.text}")

        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка при GET запросе: {e}")
        return None


def delete_request(url, headers=None, params=None):
    try:
        logger.info(f"DELETE {url}")
        logger.debug(f"Headers: {headers}")
        logger.debug(f"Params: {params}")

        response = requests.delete(url=url, headers=headers, params=params)

        logger.info(f"Response status: {response.status_code}")
        logger.debug(f"Response body: {response.text}")

        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка при DELETE запросе: {e}")
        return None
