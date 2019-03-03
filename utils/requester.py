import requests

from constants.constants import OK_RESPONSE_CODE


def get(url):
    print("trying to get: " + url + "\n")

    request_data = requests.get(url)

    if request_data.status_code == OK_RESPONSE_CODE:
        return request_data
    else:
        raise Exception
