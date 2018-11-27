import json

import requests


# This will make a HTTP request to the server containing the vault and secrets
from chalice import BadRequestError


def vault_controller(request, token):
    end_point = request['secret']
    url = "http://34.207.239.44/secrets/{}".format(end_point)
    headers = {
        'Content-type': "application/json",
        'X-Vault-Token': token
    }
    try:
        body = requests.get(url, headers=headers)
    except Exception as e:
        raise BadRequestError(e)

    return json.loads(body.content)
