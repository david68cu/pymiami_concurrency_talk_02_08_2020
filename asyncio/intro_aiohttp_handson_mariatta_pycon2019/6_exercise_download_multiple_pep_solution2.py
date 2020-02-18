import asyncio
import time
import ssl

import aiohttp

ssl_ctx = ssl.SSLContext()


async def download_pep(pep_number: int) -> bytes:

    url = f"https://www.python.org/dev/peps/pep-{pep_number}/"
    print(f"Begin downloading {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=ssl_ctx) as resp:
            content = await resp.read()
            print(f"Finished downloading {url}")
            return content


async def write_to_file(pep_number: int, content: bytes) -> None:
    filename = f"async_{pep_number}.html"
    with open(filename, "wb") as pep_file:
        print(f"Begin writing to {filename}")
        pep_file.write(content)
        print(f"Finished writing {filename}")


async def web_scrape_task(pep_number: int) -> None:
    content = await download_pep(pep_number)
    await write_to_file(pep_number, content)


async def main() -> None:
    tasks = []
    for i in range(8010, 8016):
        tasks.append(web_scrape_task(i))   # Just create an arrays of nested coroutines . No execution whatsoever
    breakpoint()                           # Can we possible inspect the coroutines at this point ??
    await asyncio.wait(tasks)              # Here is when begin downloading and writing occurs !!


if __name__ == "__main__":
    s = time.perf_counter()

    asyncio.run(main())

    elapsed = time.perf_counter() - s
    print(f"Execution time: {elapsed:0.2f} seconds.")

# This is Mariatta and Andrew solution to the exercise number 4.
# However our solution in 5 was also acceptable

# But now is a good moment to review some of ths aiohttp classes and its methods

"""
The download function

async def download_pep(pep_number: int) -> bytes:

    url = f"https://www.python.org/dev/peps/pep-{pep_number}/"
    print(f"Begin downloading {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=ssl_ctx) as resp:
            content = await resp.read()
            print(f"Finished downloading {url}")
            return content

- This is a coroutine as it is declared with "async def" async def download_pep(pep_number: int)
- All courutines  are awaitable objects
- content is indeed the page returned as raw bytes 
- It will asynchronously get the pages and return each page in the content variable to the caller
- It uses await (yield from) resp.read() 
- so resp is awaitable object as well , as it is session  


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Lest see the write function"

async def write_to_file(pep_number: int, content: bytes) -> None:
    filename = f"async_{pep_number}.html"
    with open(filename, "wb") as pep_file:
        print(f"Begin writing to {filename}")
        pep_file.write(content)
        print(f"Finished writing {filename}")
        
- It is a coroutine as it is declared with "async def
- as it is a coroutine it is awaitable

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

the web scraple method

async def web_scrape_task(pep_number: int) -> None:
    content = await download_pep(pep_number)
    await write_to_file(pep_number, content)
    
- It is a coroutine as it is declared with "async def
- as it is a coroutine it is awaitable
- it awaits for the content of the page( download_pep) .It means it get it  asynchonously
- it also awaits for write_to_file(pep_number, content) .It means it get it  asynchonously
- as it is awaitable , we can wait for it
"""


