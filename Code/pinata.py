import json
import requests

class PinataClient:
    BASE_URL = "https://api.pinata.cloud/pinning/{0}"

    def __init__(self, api_key, secret_key) -> None:
        self.__build_headers(self, api_key, secret_key)

    def __build_headers(self, api_key, secret_key):
        self.__file_headers = {
            "pinata_api_key": api_key,
            "pinata_secret_api_key": secret_key
        }
        self.__json_headers = self.__file_headers.copy()
        self.__json_headers.update({"Content-Type": "application/json"})
        print(self.__file_headers)
        print(self.__json_headers)

    def convert_data_to_json(self, content):
        data = {"pinataOptions": {"cidVersion": 1}, "pinataContent": content}
        return json.dumps(data)

    def pin_file_to_ipfs(self, file):
        response = requests.post(self.BASE_URL.format("pinFileToIPFS"), files={'file': file}, headers=self.__file_headers)
        return response.json()["IpfsHash"]

    def pin_json_to_ipfs(self, json):
        response = requests.post(self.BASE_URL.format("pinJSONToIPFS"), data=json, headers=self.__file_headers)
        return response.json()["IpfsHash"]
