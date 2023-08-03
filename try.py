import requests
import ssl
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
from requests.packages.urllib3.util.ssl_ import create_urllib3_context

class TLSAdapter(HTTPAdapter):
    def __init__(self, ssl_options=0, **kwargs):
        self.ssl_options = ssl_options
        super().__init__(**kwargs)

    def init_poolmanager(self, *pool_args, **pool_kwargs):
        context = create_urllib3_context(self.ssl_options)
        self.poolmanager = PoolManager(*pool_args,
                                       ssl_context=context,
                                       **pool_kwargs)

# Force TLSv1.2
adapter = TLSAdapter(ssl.PROTOCOL_TLSv1_2)

s = requests.Session()
s.mount("https://", adapter)

response = s.get('https://httpbin.org/get')

print(response.status_code)
print(response.text)
