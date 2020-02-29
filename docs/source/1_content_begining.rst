
.. _ref_1_content_begining:

At the beginning there were threads..
======================================

    In our  first talk about this subject, “Talk #1 - Concurrency with Threads and Futures, Feb 8th, 2020.”, we discussed the evolution
    of concurrency in Python.

    We started by analyzing Chapter 17, and the first part of Chapter 18 of Luciano Ramalho's book
    “Fluent Python” [6] In Chapter 17 “Concurrency and Features”, Luciano starts by explaining a sequential download.
    It is, of course, necessary we can see a sequential example and how we could later improve it using concurrency.

    Luciano starts Chapter 18 with an example of Threads, and later move us to coroutines and finally async I/O.
    We discussed Chapter 17 and used the treads example in Chapter 18 to learn about Threads and Futures.
    We discussed Raymond Hettinger [12] talk, “Keynote on Concurrency, PyBay 2017”,
    where we learned the complexity and perils that lure on the Threads world.

    Finally, we were able to arrive to below evolutionary conclusion in Table 1.
    If you want to know more about this, we encourage you to read our  talk and the resources mentioned.

.. csv-table:: Table 1. Concurrency in Python: Threads , Futures and Async I/O
   :file: Table1.csv
   :widths: 24, 24, 24
   :header-rows: 1


We are here, one month later ,  to talk about async I/O, far away from the thread and blocked world we discussed
in February, entering into a new universe of cooperation multitasking and event loops.

But then, we wonder what is Async I/O and what Python has to do with this.?
