import json

import requests


# This will make a HTTP request to the server containing the vault and secrets
def vault_controller(request, token):
    end_point = request['endpoint']
    url = "http://34.207.239.44/{}".format(end_point)
    headers = {
        'Content-type': "application/json",
        'X-Vault-Token': token
    }
    body = requests.get(url, headers=headers)
    return json.loads(body.content)
