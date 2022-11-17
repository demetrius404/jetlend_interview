import requests as request
from typing_extensions import TypeAlias
from typing import Union

Str: TypeAlias = str


def get_ip_address() -> Union[Str, None]:
    base_url = "https://ifconfig.me"
    response = request.get(base_url)
    if response.status_code == 200:
        # ifconfig.me return already parsed ip address
        # (only ip address without other text)
        return response.text


if __name__ == "__main__":
    print(get_ip_address())
    # 127.0.0.1 - this is joke
    # actually output is my external ip address
