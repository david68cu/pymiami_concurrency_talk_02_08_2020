import asyncio
import aiohttp

async def download_pep(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            content = await resp.read()
            print(content)
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


asyncio.run(web_scrape_task(8010))