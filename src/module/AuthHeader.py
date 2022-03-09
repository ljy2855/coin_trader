import jwt
import uuid
from urllib.parse import urlencode
from key import access_key, secret_key


def getAuthHeader():

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}
    return headers
