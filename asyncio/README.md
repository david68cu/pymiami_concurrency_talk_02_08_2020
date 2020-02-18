# ASYNC I/O

### About Documentation used for this project(Sphinx and read the docs)

We used  Sphinx and read the docs documentation .
Read more about Sphinx [here](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html)


First created on docs/folder

To start:

    ```
       mkdir docs
       workon screencasts
       pip install sphinx
       cd docs
       ls
       sphinx-quickstart
    ```

To edit make changes to /docs/source/index.srt 
   
Then compile the html with make:

    ```
    % cd /docs/
    % ls -al
        .
        ..
        -rw-r--r--   1 davidgutierrez  staff  638 Feb 13 13:14 Makefile
        drwxr-xr-x   4 davidgutierrez  staff  128 Feb 14 20:22 build
        -rw-r--r--   1 davidgutierrez  staff  799 Feb 13 13:14 make.bat
        drwxr-xr-x   7 davidgutierrez  staff  224 Feb 14 20:22 source
    % make html
    % open index.html
    ```

This generates a conf.py file and html docs 



Workflow:
    - Inside the source folder we have the index.srt that we will edit 
    - We will make html to make the new html file with the changes by 
           cd /docs
           make html
    - If we need to change teh configuration we can do it by changing the conf.py file 
    - To see changes in browser  open  docs/build/html/index.html 






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
  |       OS               |
  |________________________|
  
 -  __await__ , __aiter__ , __anext__ , __aenter__ , __aexit__
 
 Soon all these framework will run using async io
 
Twisted : 
Tornado : Tornado as "A Python web framework and asynchronous networking library
Curio
Trio

Will allow an smooth integration with RUST language that is much more secure than C
The idea is to allow an smooth integration with RUST instead of C

## AsyncIO . What I need to know

###  Before anything else , do you know  the blocks that made AsyncIO:

    generators, generator functions , coroutines 
    
    ### Generator
    
    Generator functions allow you to declare a function that behaves like an iterator, 
    i.e. it can be used in a for loop. 
    
    For this you need to implement the __next__ and __iter__ methods
    
    ### Generator Functions ( yield appears)
    
    Python provides generator functions as a convenient shortcut to building iterators.
    For this Python uses yield
    
    But ....
    
    But people knew that if we took the "pausing" part of generators and added in a "send stuff 
    back in" aspect to them, Python would suddenly have the concept of coroutines in Python
    
    When a generator yield , it keep its state
    So far we have seen generators being able to send values back to the caller
    It will cahnge soo and we will see that they will be able to accept values from the caller
    
    
     ### Diference ebtween GENERATORS AND COROUTINES
    
    
    |--------------------------------|------------------------------------------------------------|
    |   GENERATORS                                COROTUTINES                                     |
    |--------------------------------|------------------------------------------------------------|
       Produce data for iteration    |    Consume data                                            |
       Related to iteration          |    Nothing to do with iteration,even when producing values |             
    |--------------------------------|------------------------------------------------------------| 
    
    ### Coroutines and its importance in async operations 
    
    Coroutines are just special generators .... You sent values into
    
    Coroutines are very similar to genrator in Python: they both use yield
    Just the meaning of yield implies to let things go.To stop and let other continuos.So yield keyword 
    has an asynchornic meaning [8] . 
    Coroutes suspend execution in the yield statement and pass control to the caller
    along with any value to the right of yield
    Normal coroutines in python use yield to wait to receive an elemnet from the caller
    .Usually yiel is to the right
    The caller send data to the coroutine using send.
    Coroutines are functions whose execution you can pause
    
    See Luciano example page 481 ( know as pull style iterator)
    
    def simple_coroutine():
        print('->Coroutine started')
        x = yield  # Suspends execution and pass control to the caller
        print(f'-> coroutine received: {x}')
        
    my_coro = simple_coroutine()
    next(my_coro)
    my_coro.send(42)
    
    And example averager in 16.3 ( this is know as push style iterator)
    
    def averager():
    total = 0.0
    count = 0
    average = None
    while True:  # <1>
        term = yield average  # <2> Suspends the coroutines , produce a result to the caller(average) 
        total += term         # and later When the term is received the coroutines continues execution here 
        count += 1
        average = total/count
    
    caller needs to call next.close(0 to finish the coroutine
    
    Coroutines are importnat implementation of asynchronic code because the option of using threads , will depende somehow
    in the OS, as a thread below to the native OS. This is usually know in computer as Async I/O
    It is not Python , all languages today make use of Async I/O implementtaion and this has a huge implicaition for 
    the language
    For that languages shold first implement low level API (async coroutines, asyn context manager , and much more)
    Python in PEP 492, covered the implementation of PEP 492 -- Coroutines with async and await syntax
    
    ### Coroutines using nestle generators can comunciate from the caller to the end 
    sub-generator using "yield from"
    
    "yield from" allow communication between the caller and a subgenerator in nestle subgenerator applications
    
    See example 16-17 pag 497 Luciano
    See the menaing of yield form in Page 499
    
    ### Some methods in coroutines
    
    we can close a corotuine by calling
    
    besides next() and send() we can also do this to a corutines
    
    close()  # shut downs or stop teh coroutines
             # this can get also caught with a try... except GeneratorExit 
    throw()  # will throw an exception i the coroutine
    
    
    ### PIPE GENERATORS TOGUETHER
    
    Piping generators toguether give us a strong power to create some features like 
    filterings , or other piplelines computations.
    
               send           send             send           send
    |--------|     |--------|       |--------|      |--------|     |--------| 
    | SOURCE | --> | SOURCE | --->  |SOURCE  | ---> |SOURCE  |---> |SOURCE  |
    |--------|     |--------|       |--------|      |--------|     |--------|                   
    
    Chain coroutines toghether and push data through the pipe with send() opeartions
    We cna create multiple pipes , like 
    
    
                       send           send             send           send
                    |--------|     |--------|       |--------|      |--------|     |--------| 
                 -->| SOURCE | --> | SOURCE | --->  |SOURCE  | ---> |SOURCE  |---> |SOURCE  |
                /   |--------|     |--------|       |--------|      |--------|     |--------|  
               /
              /    send           send             send           send
    |--------|     |--------|       |--------|      |--------|     |--------| 
    | SOURCE | --> | SOURCE | --->  |SOURCE  | ---> |SOURCE  |---> |SOURCE  |
    |--------|     |--------|       |--------|      |--------|     |--------|   
              \
              |      send           send             send           send
              |     |--------|     |--------|       |--------|      |--------|     |--------| 
              --->  | SOURCE | --> | SOURCE | --->  |SOURCE  | ---> |SOURCE  |---> |SOURCE  |
                    |--------|     |--------|       |--------|      |--------|     |--------|   
    
    
    This is pretty similar to OO design patterns involving simple handlers
    Corotuines are faster
    
    
    
    ### Async I/O and Event Loops  
   
    Async I/O is an EVENT LOOP FRAMEWORK to implement async programming .Python implement Async I/O
    with asyncio module. But what is an EVENT LOOP?
    
    Going back to Wikipedia, an event loop "is a programming construct that waits for and dispatches 
    events or messages in a program". Basically an event loop lets you go, "when A happens, do B". 
    Probably the easiest example to explain this is that of the JavaScript event loop that's in 
    every browser. Whenever you click something ("when A happens"), the click is given to the 
    JavaScript event loop which checks if any onclick callback was registered to handle that 
    click ("do B"). If any callbacks were registered then the callback is called with the 
    details of the click. The event loop is considered a loop because 
    it is constantly collecting events and loops over them to find what to do with the event.
    
    Python gained an event loop in the standard library in the form of asyncio in Python 3.4.
    
    How async and await work?

    The async I/O implementation is very similar to other languages. However Python was not created originally 
    to be async but sync lnaguage so there is a lot of API that creates blocks. We need to research the way 
    if our application is making any  block . 
    
    Mostly if you know how to use in Javascript you can use it in Python
    Asyn I/0 is supporting much more async operations now than any other languages.
    Today Python supports Async generators, generators expressions , list comprehesnion
    
    But how it is implemented ?
    We need to understand two key new Python features
    
    1- yield from
    2- asyncio framework
    
    
    
    
    ### Python 3.4 using decorator @asyncio.coroutine
    
    In Python 3.4 all coroutines used for async operations needed to use "asyncio.coroutine" as basically 
    all native coroutine could implement yielf from 
    
    # This also works in Python 3.5.
    @asyncio.coroutine
    def py34_coro():
        yield from stuff()
        
    ### Python 3.5
    
    You can also use async def to syntactically define a function as being a coroutine, 
    although it cannot contain any form of yield expression; only return and await are allowed 
    for returning a value from the coroutine.

    async def py35_coro():
        await stuff()   # cannot contain any form of yield expression; only return and await
        
    This simple change above is important :
    
    A key thing async and types.coroutine do, though, is tighten the definition of what a coroutine is.
    It takes coroutines from simply being an interface to an actual type, making the distinction 
    between any generator and a generator that is meant to be a coroutine much more stringent
     (and the inspect.iscoroutine() function is even stricter by saying async has to be used).
   
    Note also the use of await
    
    # Summary
    
    - Defining a method with "async def" makes it a coroutine. 
    - The other way to make a coroutine is to flag a generator with types.coroutine 
    - You can only make a coroutine call chain pause with a generator-based coroutine.
    - A coroutine is n awaitable object 
    - Objects that defines __await__() -- technically collections.abc.Awaitable -- 
        which returns an iterator that is not a coroutine are also awaitable
    - An await expression is basically yield from but with restrictions of only working
       with awaitable objects (plain generators will not work with an await expression)
    - An async function is a coroutine that either has return statements -- including the 
        implicit return None at the end of every function in Python -- and/or 
        await expressions (yield expressions are not allowed).
    - The restrictions for async functions is to make sure you don't accidentally mix and match 
      generator-based coroutines with other generators since the expected use of the two types of 
      generators are rather different.
    - async/await as synonymous with asyncio, but instead think that asyncio is a framework 
      that can utilize the async/await API for asynchronous programming.
    -  David Beazley's Python Brasil 2015 keynote and his curio framework is proof of above concept
    -  async/await allows Python to provide the building blocks for asynchronous programming, 
       but without tying you to a specific event loop or other low-level details (unlike other 
       programming languages which integrate the event loop into the language directly).
    - Coroutnes allowed asyn IO because they are not just plain functions , they had an async not bloking behaivor, 
      a must for cooperative programming
    
### ASYNC IO primitives in Python allowed the creation of asyncio, twisted , curio , trio , etc

     Python corotutines , even loops and asyn await allowed the creation of asyncio 
     But of course we have others library that did the same example:  twisted, curio , trio

###  TWO WORLDS : BLOCKING WORLD and  NON-BLOCKING WORLD
  
     Today there is async IO support for almost everything from servers aiohttp, db aiomysql, aiopstgress, etc 
 
## AsyncIO functions high level

    ### Loop: get , set or create the event loop [11]
    
          lopp = asyncio.get_event_loop()     # Get the current event loop.
          lopp = asyncio.get_running_loop()   # Return the running event loop in the current OS thread.
          lopp = asyncio.set_event_loop(loop) # Set loop as a current event loop for the current OS thread
          lopp = asyncio.new_event_loop()     # Create a new event loop object.
        
        #### Running and stopping the loop     [11]
        
            loop.run_until_complete(function)
            loop.run_forever()
            loop.is_running()
            loop.close()
            loop.is_closed()
            
        #### Scheduling callbacks 
        #### Scheduling delayed callbacks 
        #### Creating Futures and Tasks
        #### Creating network servers and Opening network connections
        #### Transferring files
        #### Implementations : ships with two implementtaion one for Windows the other for Mac
        #### Server Objects
    
    ### Tasks:  
    
       - Execute a coroutine in the event lopp
    
 
    ### Coroutines 
    
       - awaits(yields) a future
       - awaits(yields) another coroutine
       - returns a result
    
    
    ### Three options to execute a coroutine
        - using asyncio.run()
        - await-ing the coroutine
        - using asyncio.create_task()
        
    
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
    Bad: Running in one process ( becuase once we finishing processing data, we will have only 
    one process)
    
    Ideally we use AsyncI/O concurrency with multiprocessing the data after it has been 
    downloaded for example 

## Django and Flask

    Flask web frameworks Django and Flask does not use async io 
    aiohttp module could hep this two frameworks
    
## MULTIPROCESSING + ASYNC I/O
Massive 

## Un Important details for beginner :

### SSL 

    aiohttp contrary to requests for example is not bind to any certificate manager like "certifi" 
    
    We should be aware that we will need to create a ssl context,  or use any other techniques for local TLS 
    certificate validations (read more about certificate in the references : certifi , ssl , TCP connectors )
    
    Example 

    ```python
    import ssl
    
    ssl_ctx = ssl.SSLContext()
    
    async def download_pep(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=ssl_ctx) as resp:
                # DO YOU STUFF HERE
    ```
    
    We can even go one step down to the transport layer and specify a TCP connector for our aiohttp request
    
    We can even create a TCP connector

### DEBUGGING

    ~~~~~
    
    import logging
    log = logging.getLogger('asyncio')
    log.setlevel(logging.DEBUUG)
    import gc
    gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
    loop=asyncio.get_event_loop()
    loop.set_debug(True)
    
    ~~~~~~
    pythonasynciodebug = 1

## References

     - 1- Yury Selivanov asyncawait and asyncio in Python 3 6 and beyond PyCon 2017.
     - 2- Miguel Grinberg Asynchronous Python for the Complete Beginner PyCon 2017.
     - 3- John Reese - Thinking Outside the GIL with AsyncIO and Multiprocessing - PyCon 2018.
     - 3.1- How to use asycn I/O with mulriperocessing.
            https://www.youtube.com/watch?v=0kXaLh8Fz3k]
           https://github.com/jreese/aiomultiprocess
     - 4- [Mariatta, Andrew Svetlov - Hands-on Intro to aiohttp - PyCon 2019].
           https://www.youtube.com/watch?v=OxzVApXKWYM
           https://us-pycon-2019-tutorial.readthedocs.io/asyncio_intro.html
     - 5- certifi for requests(https://pypi.org/project/certifi/).
     - 6- SSL context will help to solve SSL local certificate validation of web sites.
          (https://docs.python.org/3/library/ssl.html#ssl.SSLContext)
     - 7- aiohttp documentation(https://docs.aiohttp.org/en/stable/).
     - 8- Luciano Ramalho, Chapter 16, Coroutines page 480.
     - 9- How async/await works in Python3.5 by BRETT CANNON Python Core Developer.
          (https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/).
     - 10- PEP 492 -- Coroutines with async and await syntax
          (https://www.python.org/dev/peps/pep-0492/#id34)
     - 11 - EVENT LOOP(https://docs.python.org/3/library/asyncio-eventloop.html)
     - 12 - COROUTINES AND TASKS (https://docs.python.org/3/library/asyncio-task.html#coroutines)
     - 13- Łukasz Langa - Thinking In Coroutines - PyCon 2016 (https://www.youtube.com/watch?v=l4Nn-y9ktd4)
