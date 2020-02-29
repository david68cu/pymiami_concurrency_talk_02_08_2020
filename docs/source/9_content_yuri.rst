
.. _ref_9_yuri:

His name is Yuri Selivanov, or,  "async / await to take us outside of the chaos"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PEP 492 [13]  was introduced by Yuri Selivanov. to save us the rest of the mortals from the confusions and darkness.
You can see also Yuri Selivanov in our first reference here.
Go and take a look at Python PEP and search async and its authors. You will find its name close to multiples PEP

In the abstract we can read

" ...[PEP 492] It is proposed to make coroutines a proper standalone concept in Python, and introduce new supporting syntax.
The ultimate goal is to help establish a common, easily approachable, mental model of asynchronous
programming in Python and make it as close to synchronous programming as possible.

This PEP assumes that the asynchronous tasks are scheduled and coordinated by an Event Loop similar
to that of stdlib module asyncio.events.AbstractEventLoop. While the PEP is not tied to any specific Event Loop
implementation, it is relevant only to the kind of coroutine that uses yield as a signal to the scheduler,
indicating that the coroutine will be waiting until an event (such as IO) is completed."

In brief : async await is a new syntax created in Python to work with coroutines, just to make it clear it is a coroutine
( and as we already know reinforce the idea of asymmetric behavior) , and not a generator.

Dusty Phillips, in [14] (p. 295) note:

There is an alternate syntax for coroutines using the async and await keywords. The syntax makes it clearer that
the code is a coroutine and further breaks the deceiving symmetry between coroutines and generators.
The syntax doesn't work very well without building a full event loop ...

So in the new world of async, and in the newest version of Python  , coroutines reinforce the sense of
asynchronous behavior by using:

* async --> instead of --> "yield"
* await --> instead of --> "yield from" ( This transfer control back to the caller, in asyncio world ,the Event Loop)
* "async def" is now used to declare a native coroutine
* "async def" functions are always coroutines, even without await expressions
* coroutine object is the object returned when we call a coroutine(like generator objects are returned from generators)

.. code-block:: python

    import asyncio

    async def echo_server():
        print('Serving on localhost:8000')
        await asyncio.start_server(handle_connection,
                                   'localhost', 8000)

    async def handle_connection(reader, writer):
        print('New connection...')

        while True:
            data = await reader.read(8192)

            if not data:
                break

            print('Sending {:.10}... back'.format(repr(data)))
            writer.write(data)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(echo_server())
    try:
        loop.run_forever()
    finally:
        loop.close()

Above is the example given in the PEP 492.

Now let's see and discuss some more example. Luciano in [6] , Exercise 18=2, takes the time of creating teh same
script using asyncio , and curio .


It is in the GitHub project of the book not in the book itself


.. code-block:: python

    #!/usr/bin/env python3

    # spinner_curio.py

    # credits: Example by Luciano Ramalho inspired by
    # Michele Simionato's multiprocessing example in the python-list:
    # https://mail.python.org/pipermail/python-list/2009-February/538048.html
    import curio

    import itertools
    import sys


    async def spin(msg):  # <1>
        write, flush = sys.stdout.write, sys.stdout.flush
        for char in itertools.cycle('|/-\\'):
            status = char + ' ' + msg
            write(status)
            flush()
            write('\x08' * len(status))
            try:
                await curio.sleep(.1)  # <2>
            except curio.CancelledError:  # <3>
                break
        write(' ' * len(status) + '\x08' * len(status))


    async def slow_function():  # <4>
        # pretend waiting a long time for I/O
        await curio.sleep(3)  # <5>
        return 42


    async def supervisor():  # <6>
        spinner = await curio.spawn(spin('thinking!'))  # <7>
        print('spinner object:\n ', repr(spinner))  # <8>
        result = await slow_function()  # <9>
        await spinner.cancel()  # <10>
        return result


    def main():
        result = curio.run(supervisor)  # <12>
        print('Answer:', result)


    if __name__ == '__main__':
        main()

and now the same example using asyncio with await and the new coroutine definitions asyn def

.. code-block:: python

    #!/usr/bin/env python3

    # spinner_await.py

    # credits: Example by Luciano Ramalho inspired by
    # Michele Simionato's multiprocessing example in the python-list:
    # https://mail.python.org/pipermail/python-list/2009-February/538048.html

    import asyncio
    import itertools
    import sys


    async def spin(msg):  # <1>
        write, flush = sys.stdout.write, sys.stdout.flush
        for char in itertools.cycle('|/-\\'):
            status = char + ' ' + msg
            write(status)
            flush()
            write('\x08' * len(status))
            try:
                await asyncio.sleep(.1)  # <2>
            except asyncio.CancelledError:  # <3>
                break
        write(' ' * len(status) + '\x08' * len(status))


    async def slow_function():  # <4>
        # pretend waiting a long time for I/O
        await asyncio.sleep(3)  # <5>
        return 42


    async def supervisor():  # <6>
        spinner = asyncio.ensure_future(spin('thinking!'))  # <7>
        print('spinner object:', spinner)  # <8>
        result = await slow_function()  # <9>
        spinner.cancel()  # <10>
        return result


    def main():
        loop = asyncio.get_event_loop()  # <11>
        result = loop.run_until_complete(supervisor())  # <12>
        loop.close()
        print('Answer:', result)


    if __name__ == '__main__':
        main()


We can see that both library make use of async / await syntax and each one implement the same functionality ,
an Async I/O execution one using curio and anotehr using asyncio

