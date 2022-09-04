import time

import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry


def requests_retry_session(
        link: str,
        retries=3,
        backoff_factor=1,
        status_forcelist=(429, 500, 502, 503, 504),
):
    """Returns session with retry logic for requests."""

    session = requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


t0 = time.time()
link = 'http://localhost:9999'
try:
    response = requests_retry_session(link).get(
        'http://localhost:9999',
    )
except Exception as x:
    print('It failed :(', x.__class__.__name__)
else:
    print('It eventually worked', response.status_code)
finally:
    t1 = time.time()
    print('Took', t1 - t0, 'seconds')
