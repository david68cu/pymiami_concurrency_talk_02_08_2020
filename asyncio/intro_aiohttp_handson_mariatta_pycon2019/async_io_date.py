import asyncio
import datetime


async def hello():
    print(f'[{datetime.datetime.now()}] hello')
    await asyncio.sleep(0)                        # Hey loop, take care of this. I will be sleeping for x seconds
    print(f'[{datetime.datetime.now()}] world!!')

asyncio.run(hello())


