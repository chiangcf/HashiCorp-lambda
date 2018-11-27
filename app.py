from chalice import Chalice

from chalicelib.controller import vault_controller

app = Chalice(app_name='HashiCorp-lambda')


@app.route('/vault', methods=['POST'])
def hashi_vault():
    request = app.current_request
    if request.method == 'POST':
        post_body = request.json_body
        vault_token = request.headers['X-Vault-Token']
        return vault_controller(post_body, vault_token)
