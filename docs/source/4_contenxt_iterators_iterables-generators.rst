
.. _ref_4_how_async_io_works:

Iterables and Iterator and Generator Function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Generators are intrinsically linked to iteration. And that is the reason we start by analyzing the meaning of
    iterable and iterator in Python.

    Luciano Ramalho in [6] , Chapter 14 clearly defined iterable and iterator concepts. But before going there
    take note the name of that Chapter :

    "Iterables, Iterator and Generators".

    iterable:

    Any object from which the iter built-in function can obtain an iterator. Objects implementing an __iter__ method
    returning an iterator are iterable.
    Sequences are always iterable; as are objects implementing a __getitem__ method that takes 0-based indexes.

    It’s important to be clear about the relationship between iterables and iterators:
    Python obtains iterators from iterables.

    In page 418 [6], Luciano  stops to explain why Sequences are iterable and what the interpreter does when it needs to
    iterate over an object


    Then in the same Chapter in page 423 he gives us a definition of iterator

    iterator:

    Any object that implements the __next__ no-argument method that returns the next item in a series
    or raises StopIteration when there are no more items. Python iterators also implement the __iter__ method
    so they are iterable as well.

    Now,let's see an example and carefully look that we have not used the keyword "yield" so far for anything.
    Remember the title of the Chapter does not mention coroutines : "Iterables, Iterator and Generators".

