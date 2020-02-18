import asyncio
import aiohttp
import ssl
import time

ssl_ctx = ssl.SSLContext()


async def download_pep(url) ->bytes:

    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=ssl_ctx) as resp:
            content = await resp.read()
            # print(content)
            return content

# asyncio.run(download_pep("https://www.python.org/dev/peps/pep-8010/"))
# Writing the downloaded content to a new file can be done as its own coroutine.


async def write_to_file(pep_number, content):
    filename = f"async_{pep_number}.html"
    with open(filename, "wb") as pep_file:
        pep_file.write(content)

# Since we now have two coroutines, we can execute them like so:


async def web_scrape_task(pep_number):
    url = f"https://www.python.org/dev/peps/pep-{pep_number}/"

    downloaded_content = await download_pep(url)
    await write_to_file(pep_number, downloaded_content)

# I do not think we can come with something simpler than this small transformation to 4_aoihttp_simple.py
s = time.perf_counter()

for p in range(8010, 8016):
    asyncio.run(web_scrape_task(p))
elapsed = time.perf_counter() - s
print(f"Execution time: {elapsed:0.2f} seconds.")    # 1.47 sec

# Execution time: 1.47 seconds. Comparing with 3_without_aiohttp.py

