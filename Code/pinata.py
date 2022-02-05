import json
import requests

class PinataClient:
    BASE_IPFS_URL = "ipfs://{0}"
    BASE_HTTP_URL = "https://api.pinata.cloud/pinning/{0}"

    def __init__(self, api_key, secret_key):
        self.__build_headers(api_key, secret_key)

    def __build_headers(self, api_key, secret_key):
        self.__file_headers = {
            "pinata_api_key": api_key,
            "pinata_secret_api_key": secret_key
        }
        self.__json_headers = self.__file_headers.copy()
        self.__json_headers.update({"Content-Type": "application/json"})

    def __pin_file_to_ipfs(self, file):
        response = requests.post(self.BASE_HTTP_URL.format("pinFileToIPFS"), files={'file': file}, headers=self.__file_headers)
        return response.json()["IpfsHash"]

    def __build_token_metadata(self, name, category, file_hash):
        return {"name": name, "category": category, "image": file_hash}

    def __build_json_data(self, metadata):
        data = {"pinataOptions": {"cidVersion": 1}, "pinataContent": metadata}
        return json.dumps(data)
        
    def __pin_json_to_ipfs(self, json):
        response = requests.post(self.BASE_HTTP_URL.format("pinJSONToIPFS"), data=json, headers=self.__json_headers)
        return response.json()["IpfsHash"]
    
    def upload_image(self, name, category, file):
        file_hash = self.__pin_file_to_ipfs(file)
        metadata = self.__build_token_metadata(name, category, file_hash)
        json_data = self.__build_json_data(metadata)
        json_hash = self.__pin_json_to_ipfs(json_data)
        return self.BASE_IPFS_URL.format(json_hash)
