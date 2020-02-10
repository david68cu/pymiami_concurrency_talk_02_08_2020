# ASYNC I/O

## Is there other ways though?

- threads
- callbacks/promise
- getevent/ eventlet/ stackless
- generators 

## Why AsyncIO ?

- First reason: Threads is a system resources , so you can not create as
many as you want.Event C# has thread limitations

    - AsyncIO will manage thousands+ of async requests
    - Threads will manage hundreds of async request 
    - Process will manage tens of async request 

- Easier to reason than threads or eventlet etc
- Better than call backs and promises
- Promote better pattern : Example Message passing (better than global variable)

## Async History started in Python  3.5

- Python 3.5 Async function, context Managers , async Iterators, await expression
- Python 3.6 Async generators, generators expressions , list comprehesnion
- Python 3.7 yield from

## Async/Await is a Protocol

 - Indeed async await is a protocol that use magic methods based on iterator 
 protocol.
 
   _______________________
  | Application            |
  |________________________|
  |  Application Framework |
  |________________________|
  | Async Framework        |
  |________________________|
  | Python Interpreter     |
  |________________________|
  |       OS                |
  |________________________|
  
 -  __await__ , __aiter__ , __anext__ , __aenter__ , __aexit__
 
 Soon all these framework will run using async io
 
Twisted : 
Tornado : Tornado as "A Python web framework and asynchronous networking library
Curio
Trio

Will allow an smooth integration with RUST language that is much more secure than C
The idea is to allow an smooth integration with RUST instead of C

## Async I/O low level APIs

    The async I/O implementation is very similar to other languages. However Python was not created originally 
    to be async but sync lnaguage so tehre is a lot of API that creates blocks. We need to research the way 
    if our application is making any  block . 
    
    Mostly if you know how to use in Javascript you can use it in Python
    Asyn I/0 is supporting much more async operations now than any other languages.
    Today Python supports Async generators, generators expressions , list comprehesnion


## Async I/O functions high level

    loop = asyncio.get_event_loop()
    
    loop.run_until_complete(function)
    loop.run_forever()
    loop.run_in_executor()
    lopp.create_task()
    
    asyncio.gather()
    await asyncio.sleep(3)

    It is importnat to keep all the loop arguments and to pass it
    However starting in 3.7 we should not use loop. any more
    
    To actually execute the coroutine, you have three options:
    
    # To execute a coroutine we have 3 options
    
    -1) using asyncio.run() 
       Example : 
       asyncio.run(long_running_task(3))
       
    -2) await-ing the coroutine
        Example:
        async def main():
            await long_running_task(3)   
         asyncio.run(main())
    
    - 3)using asyncio.create_task()
        Example:
        async def main():
            task = asyncio.create_task(long_running_task(3))  
            await task
        asyncio.run(main())

## IDEAL WORLD

Async I/O
Good:Massive concurrency thousansd
Bad: Running in one process ( becuase once we finishing processing data, we will have only one process)

Ideally we use AsyncI/O concurrency with multiprocessing the data after it has been downloaded for example 

## Django and Flask

    Flask web frameworks Django and Flask does not use async io 
    aiohttp module could hep this two frameworks
    
## MULTIPROCESSING + ASYNC I/O
Massive 
## References

 - Yury Selivanov asyncawait and asyncio in Python 3 6 and beyond PyCon 2017
 - Miguel Grinberg Asynchronous Python for the Complete Beginner PyCon 2017
 - John Reese - Thinking Outside the GIL with AsyncIO and Multiprocessing - PyCon 2018
   How to use asycn I/O with mulriperocessing
   [https://www.youtube.com/watch?v=0kXaLh8Fz3k]
   https://github.com/jreese/aiomultiprocess
 - [Mariatta, Andrew Svetlov - Hands-on Intro to aiohttp - PyCon 2019]
   https://www.youtube.com/watch?v=OxzVApXKWYM
   https://us-pycon-2019-tutorial.readthedocs.io/asyncio_intro.html