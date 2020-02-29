import asyncio
import aiohttp
import ssl

ssl_ctx = ssl.SSLContext()


async def download_pep(url) -> bytes:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=ssl_ctx) as resp:
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

# We very likely will hit here an SSL error : aiohttp.client_exceptions.ClientConnectorCertificateError:
# Cannot connect to host www.python.org:443 ssl:True [SSLCertVerificationError:
# (1, '[SSL: CERTIFICATE_VERIFY_FAILED]
# certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)')]

# As the error states aiohttp is failing to check the certificate from www.python.org:443 , as can not verify
# the issuer

# Before we used requests ( for humans :-) ) requests uses certifi for root certificates source.
# This approach has own advantages and disadvantages.
#
# aiohttp  decided to not rely on custom certificate libraries , so we need to use a ssl context

# This is the reason we need to upload our scrip with ssl module
#
