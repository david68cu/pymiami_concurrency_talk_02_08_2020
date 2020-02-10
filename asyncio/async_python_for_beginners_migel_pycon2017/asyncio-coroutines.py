import asyncio

loop = asyncio.get_event_loop()


@asyncio.coroutine                # Not to use in Python above +3.5 use asynd def hello():
def hello():
    yield from asyncio.sleep(3)
    print('Hello!')


if __name__ == '__main__':
    loop.run_until_complete(hello())
