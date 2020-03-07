
.. _ref_8_event_loops:

Event Loops
^^^^^^^^^^^

Doug Hellman in his mater book "The Python 3 Standard Library by Example"  (Developer's Library) 1st Edition
Chapter 10.5 describes what an Event Loop is:

"Event loop, a first-class object that is responsible for efficiently handling I/O events, system events,
and application context changes. Several loop implementations are provided, to take advantage of the
operating systems’ capabilities efficiently. While a reasonable default is usually selected automatically,
it is also possible to pick a particular event loop implementation from within the application". [13]

Python documentation describes the event loop as follow:
"Event loops run asynchronous tasks and callbacks, perform network IO operations, and run subprocesses". [14]

"In computer science, the event loop is a programming construct or design pattern that waits for and dispatches
events or messages in a program. The event loop works by making a request to some internal or external
"event provider" (that generally blocks the request until an event has arrived),
then calls the relevant event handler ("dispatches the event").

The event loop is also sometimes referred to as the message dispatcher, message loop, message pump, or run loop."


MDN gives us the following definition of JavaScript event loop:

"JavaScript has a concurrency model based on an event loop,
which is responsible for executing the code, collecting and processing events,
and executing queued sub-tasks. "

In any case an event loop is as its name says , is a loop :-) . In Python we can implement loops with something so
simple as a while statement . Also we can do it using a context Manager, etc.

In brief the Event Loop is an important part of any Async I/O architecture, and in Python this is also the case.

Specifically the asyncio module , one of many async i/o implementations in Python , creates the event loop in the
BaseDefaultEventLoopPolicy class . This event loop runs in its own thread and what we expect from it
( efficiency, simplicity and responsibility in task delegation ) we certainly get it.

See below some lines of the source code for the method get_event_loop() in the BaseDefaultEventLoopPolicy class .

`BaseDefaultEventLoop <https://github.com/python/cpython/blob/9ce361d3bb15cf49b82fa03e3e593d7cbd8ee1ff/Lib/asyncio/events.py#L205>`_.

.. code-block:: python

    class BaseDefaultEventLoopPolicy(AbstractEventLoopPolicy):
        """Default policy implementation for accessing the event loop.
        In this policy, each thread has its own event loop.  However, we
        only automatically create an event loop by default for the main
        thread; other threads by default have no event loop.
        Other policies may have different rules (e.g. a single global
        event loop, or automatically creating an event loop per thread, or
        using some other notion of context to which an event loop is
        associated).
        """

        _loop_factory = None

        class _Local(threading.local):
            _loop = None
            _set_called = False

        def __init__(self):
            self._local = self._Local()

        def get_event_loop(self):
            """Get the event loop for the current context.
            Returns an instance of EventLoop or raises an exception.
            """
            if (self._local._loop is None and
                    not self._local._set_called and
                    isinstance(threading.current_thread(), threading._MainThread)):
                self.set_event_loop(self.new_event_loop())

            if self._local._loop is None:
                raise RuntimeError('There is no current event loop in thread %r.'
                                   % threading.current_thread().name)

            return self._local._loop




David Beazley curio library uses  as event loop an Object he called the Kernel.
We ask the Kernel to run and pass as a parameter to it,   a coroutine.
One more time the Kernel ( Event Loop) has only limited coordination and functionality and is build on top of simple
data structures, threads.Event object (real threads) etc

`The curio Event Loop (Kernel) run function <https://github.com/dabeaz/curio/blob/master/curio/kernel.py>`_

.. code-block:: python

    def run(corofunc, *args, with_monitor=False, selector=None,
            debug=None, activations=None, **kernel_extra):
        '''
        Run the curio kernel with an initial task and execute until all
        tasks terminate.  Returns the task's final result (if any). This
        is a convenience function that should primarily be used for
        launching the top-level task of a curio-based application.  It
        creates an entirely new kernel, runs the given task to completion,
        and concludes by shutting down the kernel, releasing all resources used.

        Don't use this function if you're repeatedly launching a lot of
        new tasks to run in curio. Instead, create a Kernel instance and
        use its run() method instead.
        '''
        kernel = Kernel(selector=selector, debug=debug, activations=activations,
                        **kernel_extra)

        # Check if a monitor has been requested
        if with_monitor or 'CURIOMONITOR' in os.environ:
            from .monitor import Monitor
            m = Monitor(kernel)
            kernel._call_at_shutdown(m.close)
            kernel.run(m.start)

        with kernel:
            return kernel.run(corofunc, *args)

Ok so we have mentioned 3 Event loops two in Python and one in javascript
the asyncio event loop is able to run asynchronous code ( threads , futures) as well as async i/o not blocking code

This is taken from the Python documentation

.. code-block:: python

    import asyncio
    import concurrent.futures

    def blocking_io():
        # File operations (such as logging) can block the
        # event loop: run them in a thread pool.
        with open('/dev/urandom', 'rb') as f:
            return f.read(100)

    def cpu_bound():
        # CPU-bound operations will block the event loop:
        # in general it is preferable to run them in a
        # process pool.
        return sum(i * i for i in range(10 ** 7))

    async def main():
        loop = asyncio.get_running_loop()

        ## Options:

        # 1. Run in the default loop's executor:
        result = await loop.run_in_executor(
            None, blocking_io)
        print('default thread pool', result)

        # 2. Run in a custom thread pool:
        with concurrent.futures.ThreadPoolExecutor() as pool:
            result = await loop.run_in_executor(
                pool, blocking_io)
            print('custom thread pool', result)

        # 3. Run in a custom process pool:
        with concurrent.futures.ProcessPoolExecutor() as pool:
            result = await loop.run_in_executor(
                pool, cpu_bound)
            print('custom process pool', result)

    asyncio.run(main())

As we can see we use the asyncio Event Loop was used to run  Process and  Threads!!

So lets see some more examples of Even Loops

From Python asyncio docs :

.. code-block:: python

    import asyncio

    def hello_world(loop):
        """A callback to print 'Hello World' and stop the event loop"""
        print('Hello World')
        loop.stop()

    loop = asyncio.get_event_loop()

    # Schedule a call to hello_world()
    loop.call_soon(hello_world, loop)

    # Blocking call interrupted by loop.stop()
    try:
        loop.run_forever()
    finally:
        loop.close()

More examples: