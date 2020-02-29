.. _ref_11_aiohttp_andrew-mariatta:

Andrew Svetlov:  aiohttp
^^^^^^^^^^^^^^^^^^^^^^^^

In order to use asyncio, we must use libraries that are not blocking
It means that those libraries or frameworks, need in turn to use asyncio's implementation of all I/O functions !!!
So let say we want to use asyncio to get a web site. It should be easy with what we have done so far, right ? or not?

.. code-block:: python

    # Example similar to the Mariatta and Andrew exercises in [5]
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

.. code-block::

    # OUTPUT
    >>File "../asyncio/intro_aiohttp_handson_mariatta_pycon2019/3.1_wrong_asyncio_requests.py", line 7, in fetch
    >>await requests.get(url)
    >>TypeError: object Response can't be used in 'await' expression

So what happened here ?

The reason for this is that requests is not awaitable .Requests comes from the another universe, the universe
of blocking and uses sockets() that is blocking by nature, and as such we can not use it.
So then what we are going to do.?

We have two options:

    - We use a function or library that is awaitable ( requests is not awaitable)
    - We can call this function in another Thread or Process , so it will be immediately awaitable

So let's try to solve the issue using the second technique :

.. code-block:: python

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

I can see the stupor in your face.

Did not you say you were to take me to a new universe away from Threads and Process , and OS limitations
to an  unblocked world of cooperative multitasking ?
Did not you show me what the Gods and Prophets, listed in that immense   Reference above  have  said ?
How is that you are talking about Threads and asyncio all mixed up together ?

Our friend requests (for humans)  can not be used any longer in this new universe without pain.
And meanwhile we await for a new and  awaitable requests library for humans, from this artist that gracefully
created it for us , `Kenneth Reitz <https://www.kennethreitz.org/>`_  we have at least for now aiohttp.

Fortunately Andrew Svetlov created aiohttp and we can use it for cases like this.
Andrew Svetlov and Mariatta Wijaya, in [4] and [5], provided us with some examples we will analyze later

But for now let's try to simply solve this problem .All that we want is to use asyncio to go and  grap a response
from a web site , but without using Threads , or Future or any other type of concurrency in Python.

.. code-block:: python

    import asyncio
    import aiohttp


    async def fetch():
        url = f"http://httpbin.org/get"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                print(resp.status)
                print(await resp.text())


    if __name__ == '__main__':
        asyncio.run(fetch())

And finally we get our first correct response using asyncio

Oh , but wait , it is not the same url neither the same requests, so tehre is no wait I can compare !!

Sorry about that , it will be easy to write our first example similar to the one we saw earlier
Here we go

.. code-block:: python

    import asyncio
    import aiohttp


    async def fetch(pep):
        url = f"https://www.python.org/dev/peps/pep-{pep}/"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                print(resp.status)
                print(await resp.text())


    if __name__ == '__main__':
        asyncio.run(fetch(8010))

Ah it did not work !!
We are getting an TLS cetificate error

Well aiohttp is not linked to any specific certificate manager at the client side , so it does not kow how to
validate the https.

In our friend requests library  Kenneth Reitz, incorpotated the certificate validation for us using certifi so signatures of
certificates could be verified using the installed root certificates source in our system.

It is simple fix in aiohttp

.. code-block:: python

    import asyncio

    import aiohttp
    import ssl

    ssl_ctx = ssl.SSLContext()

    async def fetch(pep):
        url = f"https://www.python.org/dev/peps/pep-{pep}/"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=ssl_ctx) as resp:
                print(resp.status)
                print(await resp.text())


    if __name__ == '__main__':
        asyncio.run(fetch(8010))

Is it the end !!
Well almost at this point you have the basic blocks to use this amazing library in Python for any multiprocessing.

And what you should do now?

    - Every day new Python libraries, that support asyncio, are created, so go  there and study them and use them.
    - Go to Twitter and follow the amazing People that created this tool for us
    - Buy the books I mentioned in this serie , they will really help you
    - Check the authors talks in conferences
    - And finally study deeper the resources provided
