
.. _ref_2_content_asyncio_intro:

...And then we were given a breath of life Async I/O
=====================================================

    What is async I/O ?

    According to Wikipedia, "In computer science, asynchronous I/O (also non-sequential I/O) is a form of input/output
    processing that permits other processing to continue before the transmission has finished".

    David Beazley, "Python Brasil 2015 keynote..." [8] , starts by recounting that Async I/O was implemented by C# a
    long time ago . Łukasz Langa, "Thinking In Coroutines - PyCon 2016" [6] states that those who knows JavaScript/ NodeJS
    async I/O should easily get the concept in Python.

    Async I/O is not a Python concept and indeed has been implemented in other languages a long time ago.

    Async I/O gives us the possibility of writing  concurrent programs without using Threads. Threads belong to the OS
    and ,as such, are more expensive and less scalable than async I/O cooperative multitasking . So just using one thread ,
    the main thread,  we are able to gain multiprocessing capability.

    Before going any step further ,take a moment to look at Miguel Grinberg's,  Asynchronous Python for the
    Complete Beginner talk [2] where, in just a few minutes, Miguel quickly describes the universe of async programing.

    But then we want the details, the "how was this possible?", and the desire to understand how async I/O works ?

