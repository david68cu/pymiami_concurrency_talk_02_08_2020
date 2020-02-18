CONCURRENCY IN PYTHON
=====================

Second Part: Python Async I/O
=============================


Created by: David Gutierrez for PyMiami Org.
email: david @ pymiami . org

Join us at
Twitter
Facebook

Do you need help ?

    Contact us for training at david @ pythonsoftware.solutions

Important Note
--------------

All content in this tutorial has been taken from the references below. What I have done is looking for some of the best
, relevant information and  organize it in a way that better help understands the subject .
I find this much better than re-create a content , and also because the creators are extremely skilled and experienced
personalities ,and as such are  much more capable and has much more knowledge than I have.

This course is also a way of recognition to the creators of the content and their live long effort and their
contribution to Python.

Take a time to follow them in their Social media Links below , and check their companies , courses ,
training and what they do. You will benefit immensely.

I will take the freedom to start by mention all the references,  and documentation used in this Tutorial.


References
----------

     - 1- Yury Selivanov,  `Async await and asyncio in Python 3.6 and beyond PyCon 2017. <https://www.youtube.com/watch?v=2ZFFv-wZ8_g>`_
     - 2- Miguel Grinberg,  `Asynchronous Python for the Complete Beginner PyCon 2017. <https://www.youtube.com/watch?v=iG6fr81xHKA>`_
     - 3- John Reese, `Thinking Outside the GIL with AsyncIO and Multiprocessing - PyCon 2018. <https://www.youtube.com/watch?v=0kXaLh8Fz3k>`_
     - 4- Mariatta Wijaya, `Hands-on Intro to aiohttp - PyCon 2019] video. <https://www.youtube.com/watch?v=OxzVApXKWYM>`_
     - 5- Andrew Svetlov, `Hands-on Intro to aiohttp - PyCon 2019] slides. <https://us-pycon-2019-tutorial.readthedocs.io/asyncio_intro.html>`_
     - 6- Luciano Ramalho, `Fluent Python 1st Edition,  book , Chapter 16, Coroutines page 480. <https://www.amazon.com/Fluent-Python-Concise-Effective-Programming/dp/1491946008>`_
     - 7- Brett Cannon, `How async/await works in Python3.5. <https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/).>`_
     - 8- David Beazley, `Python Brasil 2015 keynote and his curio framework is proof of above concept <https://www.youtube.com/watch?v=lYe8W04ERnY>`_
     - 9- David Beazley, `Curios Course on Coroutines and Concurrency, <http://www.dabeaz.com/coroutines/>`_
     - 10- Łukasz Langa, `Thinking In Coroutines - PyCon 2016, <https://www.youtube.com/watch?v=l4Nn-y9ktd4>`_
     - 11- Brett Cannon, `How the heck does async/await work in Python 3.5?, <https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/>`_
     - 12- Raymond Hettinger, `Keynote on Concurrency, PyBay 2017 <https://www.youtube.com/watch?v=9zinZmE3Ogk&t=55s>`_


Documents and Papers
^^^^^^^^^^^^^^^^^^^^

     - 10- `certifi documentation <https://pypi.org/project/certifi/>`_.
     - 11- `SSL context documentation <https://docs.python.org/3/library/ssl.html#ssl.SSLContext>`_.
     - 12- `aiohttp documentation, <https://docs.aiohttp.org/en/stable/>`_.
     - 13- `PEP 492, Coroutines with async and await syntax, <https://www.python.org/dev/peps/pep-0492/#id34>`_.
     - 14- `Python Event loop, <https://docs.python.org/3/library/asyncio-eventloop.html>`_.
     - 15- `Coroutines and tasks, <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_.
     - 16- `PEP 380, Syntax for Delegating to a Subgenerator. <https://www.python.org/dev/peps/pep-0380/>`_.



.. toctree::
   :maxdepth: 2
   :caption: Contents:


At the beginning there were threads..
======================================

In our first talk about Concurrency we discussed the evolution of concurrency in Python.

We started by analyzing chapter 17,  and first part of chapter 18 of Luciano Ramalho book  "Fluent Python" [6]
In chapter 17 "Concurrency and Features" , Luciano starts by explaining a sequential download . It is of course necessary
we can see a sequential example and how we could later improve it using concurrency.

Luciano starts  Chapter 18  with an example of Threads, and later move us to coroutines and finally async I/O.

We discussed chapter 17 and used the treads example in Chapter 18  to learn about Threads and Futures

To learn about Threads we fully discussed Raymond Hettinger talk, "Keynote on Concurrency, PyBay 2017" , where we
learned the complexity and perils that lure on the Threads world

Finally we were able to  arrive to below evolutionary conclusion in Table 1.

If you want to know more about this , we encourage you to search our talk or the resources mentioned.


  CONCURRENCY IN PYTHON : "Dealing with lots of things at once"
  [6] Chapter 18th

.. csv-table:: Table 1
   :file: TAble1.csv
   :widths: 33, 33, 33
   :header-rows: 1




And here we are one month later to learn about async I/O , await from the Thread and blocked world into a new universe of
cooperation multitasking  and event loops. But then what is Async I/O and what Python have to do with this


...And then we were given a breath of life Async I/O
=====================================================

What is async I/O ?

As per Wikipedia " In computer science, asynchronous I/O (also non-sequential I/O) is a form of input/output
processing that permits other processing to continue before the transmission has finished.

David Beazley, `Python Brasil 2015 keynote...[8] , starts by recounting that Async I/O was implemented by C# a
long time ago . Łukasz Langa, `Thinking In Coroutines - PyCon 2016 [6] states that those who knows JavaScript/ NodeJS
async I/O should easily get the concept in Python.

So Async I/O is not a Python concept and indeed has been implemented in other languages a long time ago

Async I/O gives us the possibility of write concurrent programs , without using Threads. Threads belong to the OS
and as such are more expensive and less scalable than async I/O cooperative multitasking . So just using one thread ,
the main thread,  we are able to gain multiprocessing capability.

Before going any step further , this is the moment to take a look at Miguel Grinberg,  `Asynchronous Python for the
Complete Beginner talk [2] where in just a few minutes , Miguel quickly describe the universe of async programing.

But then we want the details , the how this was possible, and indeed understand how async I/O works ?


How the heck does async/await work in Python
--------------------------------------------

When you feel afraid of not knowing enought about async I/O , it will be a releif to know that Brett  Cannon asked himself
the above question in  [11]. Once you know who he is you will feel and imediate peace of mind , on having
some doubts ( or maybe many ?) about async I/O. He had too at some moment !!

David Beazley in [8] and [9], clearly describe the evolution of async I/O
Meanwhile Brett  Cannon in [11] starts by taking us back to the origin and uses of 'yield from'  in coroutines , is
David Beazley the one that take us even further back and deeper , by starting for a diferentiation between generators ,
an coroutines.

David Beazley  make a distintion that generators and generators function should be differenciated from coroutines in both
its intention and uses. We will see this distintion below

Generator
^^^^^^^^^

    Generator functions allow you to declare a function that behaves like an iterator,
    i.e. it can be used in a for loop.

    For this you need to implement the __next__ and __iter__ methods

    Luciano Ramalho in [6] , Chapter 14 clearly defined iterable and iterator in Chapter 14. But beofre going there
    take note the name of that Chapter "Iterables, Iterator and Generators". We will see why later

    iterable:

    Any object from which the iter built-in function can obtain an iterator. Objects implementing an __iter__ method
    returning an iterator are iterable.
    Sequences are always iterable; as are objects implementing a __getitem__ method that takes 0-based indexes.

    It’s important to be clear about the relationship between iterables and iterators:
    Python obtains iterators from iterables.

    In page 418 he stops to explain why Sequences are iterable and what teh interpreter oes when needs to
    iterate over an object


    Then in the same Chapter in page 423 he gives us a definition of iterator

    iterator:

    Any object that implements the __next__ no-argument method that returns the next item in a series
    or raises StopIteration when there are no more items. Python iterators also implement the __iter__ method
    so they are iterable as well.

    Now let see an example and carefully look that we have not used the keyword yield so far for anything:





Generator Functions ( yield appears)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Python provides generator functions as a convenient shortcut to building iterators.
    For this Python uses yield


    Simple generator function countdown.py , taken from  David Beazley... [9]


    .. code-block:: python

            #countdown.py
            # A simple generator function

            def countdown(n):
                print "Counting down from", n
                while n > 0:
                    yield n
                    n -= 1
                print "Done counting down"

            # Example use
            if __name__ == '__main__':
                for i in countdown(10):
                    print i



    .. note::
        Note the use of the yield to the left of the value. So yield is pausing execution of the countdown() function
    and returning back  to the caller both the n value and the control.


    But ....

    But people knew that if we took the "pausing" part of generators and added in a "send stuff
    back in" aspect to them, Python would suddenly have the concept of coroutines in Python ..Brett [11]

    When a generator yields , it keep sits state
    So far we have seen generators being able to send values back to the caller.
    It will change soon and we will see that they will be able to accept values from the caller


Coroutines and its importance in async operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Coroutines are just special generators .... You sent values into

    Coroutines are very similar to generators in Python: they both use yield.
    Just the meaning of yield implies to let things go.To stop and let other continuous. So yield keyword
    has an asynchronous meaning. Brett [8] .
    Coroutines suspend execution in the yield statement and pass control to the caller
    along with any value to the right of yield.
    Normal coroutines in python use yield to wait to receive an elements from the caller. Usually yield is to the right
    The caller send data to the coroutine using send.
    Coroutines are functions whose execution you can pause.

    In  [6] , Chapter 16 Page 480, Luciano Ramalho  explains to us  " How Coroutines evolved form Generators" :
    On PEP 342 and PEP 380 , Luciano continues in [6],  .send() , throw() and .close() methods were added that
    allowed a caller to send() a datum into the generator , thrown and exception to be handle inside the generator,
    and terminate it.

    PEP 380 , added yield from syntax. that allows a generator , continues Luciano [6] in the same page
    We can go deeper on the details of PEP 380, created by Gregory Ewing reading [16]

     We could see some examples of use of coroutines now , but what will be really useful is to see David Beazley examples
     in A Curious Course on Coroutines [9] ..., Part 1 : Introduction to Generators and Coroutines

     Then looking at Chapter [2] on David Bealey [9] , example copipe.py we will see how how to hook up a pipeline with
     coroutines

     Now is time we can understand and see yield from in Action.

Luciano Ramalho , Fluent Python,  Page [496]  Example 16-17
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


    .. code-block:: python


            def averager():
                total = 0.0
                count = 0
                average = None
                while True:
                    term = yield
                    if term is None :
                        break
                    total + = term
                    count + = 1
                    average = total / count
                    return Result ( count , average )

             # the delegating generator
             def grouper ( results , key ):
                while True :
                    results [ key ] = yield from averager ( )

             # the client code, a.k.a. the caller

             def main ( data ):
                results = { }
                for key , values in data . items ( ):
                group = grouper ( results , key )
                next ( group )
                for value in values:
                    group.send(value)
                group.send(None) # important!

                # print(results) # uncomment to debug
                report ( results )

                # output report
                def report ( results ):
                    for key , result in sorted ( results . items ( ) ):
                        group , unit = key . split ( ' ; ' )
                        print ( ' {:2} {:5} averaging {:.2f}{} '.format(
                                  result.count, group, result.average, unit))

             data = { ' girls;kg ':
                            [ 40.9 , 38.5 , 44.3 , 42.2 , 45.2 , 41.7 , 44.5 , 38.0 , 40.6 , 44.5 ] ,
                      ' girls;m ':
                            [ 1.6 , 1.51 , 1.4 , 1.3 , 1.41 , 1.39 , 1.33 , 1.46 , 1.45 , 1.43 ] ,
                       ' boys;kg ':
                             [ 39.0 , 40.8 , 43.2 , 40.8 , 43.1 , 38.6 , 41.4 , 40.6 , 36.3 ] ,
                       ' boys;m ':
                             [ 1.38 , 1.5 , 1.32 , 1.25 , 1.37 , 1.48 , 1.25 , 1.49 , 1.46 ] , }

             if __name__ == ' __main__ ':
                main(data)

We can easily see now the power of "yield from" and how this keywords will allow us to extract values and send
values directly to the subgenerator, which yield data back at the caller.


Interlude : Generators are not Coroutines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                  ....(David Beazley minute 30:42 of Curious Course on Coroutines and Concurrency[9]

Coroutines evolved from generators.From coroutines a new syntax gave birth to async and await keywords
and that is the reason we have take a look to all that here so far.

But as David Beezley quoted in above reference, generators are not coroutines.
Below Table show the differences.

    .. list-table:: Table 2 Differences between GENERATORS and COROUTINES
       :widths: 35 65
       :header-rows: 1

       * - GENERATORS
         - COROUTINES
       * - Produce data
         - Consume data
       * - Related to iteration
         - Nothing to do with iteration,even when producing values and Related to async behavior

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
