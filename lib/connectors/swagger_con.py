import json

import requests
from pyftpdlib.ioloop import Connector
from pyats.topology import Device

class SwaggerConnector:
    def __init__(self,device:Device):
        self._session = None
        self._headers = None
        self._auth = None
        self._url=None

    def connect(self):
        host=self.device.connections.swagger.ip
        port=self.device.connections.swagger.port
        protocol=self.device.connections.swagger.protocol
        self._url=f"{protocol}://{host}:{port}"
        self._headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        self.__login()

    def __login(self):
        endpoint='/api/fdm/latest/fdm/token'
        response=requests.post(
            url=self._url+endpoint,
            headers=self._headers,
            verify=False,
            data=json.dumps({
                'username': self.device.credentials.username,
                'password':self.device.credentials.password.plaintext,
                'grant_type': 'password',
            }
            )
        )
        self.access_token=response.json()['access_token']
        self.refresh_token=response.json()['refresh_token']
        self.token_type=response.json()['token_type']


    def logout(self):
        pass