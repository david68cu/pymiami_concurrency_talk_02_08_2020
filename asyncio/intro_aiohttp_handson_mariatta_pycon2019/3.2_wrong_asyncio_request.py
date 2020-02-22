
import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor

_executor = ThreadPoolExecutor(1)


def fetch(pep):
    url = f"https://www.python.org/dev/peps/pep-{pep}/"
    return requests.get(url)


async def call_asyn():
    pep = 8010
    res = await loop.run_in_executor(_executor, fetch, pep)
    print(f"Finished downloading pep {pep}")
    return res


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(call_asyn())
    print('Answer:', result)
    loop.close()











