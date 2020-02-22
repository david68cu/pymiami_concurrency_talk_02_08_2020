
import requests
import asyncio


async def fetch(pep):
    url = f"https://www.python.org/dev/peps/pep-{pep}/"
    await requests.get(url)



def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(fetch(8010))
    loop.close()
    print('Answer:', result.content)


if __name__ == '__main__':
    main()