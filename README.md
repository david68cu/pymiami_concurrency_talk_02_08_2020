# Concurrency in Python

### Created by David Gutierrez for PyMiami.

  <p> Joint our group social accounts </p>


  <table border="0">
  <tr>
      <td>  
          <a href="https://twitter.com/Py_Miami">
          <img src="Twitter_Logo_Blue.png" width="50" height="50" title="PyMiami Twitter Link">
          </a>
       </td>
       <td>
           <a href="https://www.facebook.com/PythonDevelopersMiami/">
           <img src="f_logo_RGB-Blue_1024.png" width="40" height="40" title="PyMiami Facebook Link">
           </a>
       </td>
  </tr>
  </table>
  
  
  For Professional Services, Training and application development:
    - PYTHON SOFTWARE SOLUTIONS LLC
    -  email: david@pythonsoftware.solutions 
    -  web:   https://www.pythonsoftware.solutions


##   Talks Schedules 

        Talk #1 - Concurrency with Threads and Futures , Feb 8th 2020.
        Talk #2 - Concurrency with Async I/0,  March 14th 2020 .
        Talk #3 - Paralellism in Python,  April 14th 2020 .


## IMPORTANT NOTE



    All content in this tutorial has been taken from the references below. What I have done is looking for some of the best
    , relevant information and  organize it in a way that better help understands the subject .
    I find this much better than re-create a content , and also because the creators are extremely skilled and experienced
    personalities ,and as such are  much more capable and has much more knowledge than I have.
    
    This course is also a way of recognition to the creators of the content and their live long effort and their
    contribution to Python.
    
    Take a time to follow them in their Social media Links below , and check their companies , courses ,
    training and what they do. You will benefit immensely.
    
    I will take the freedom to start by mention all the references,  and documentation used in this Tutorial.
    

## References

    -  Ramalho, Luciano. Fluent Python: Clear, Concise, and Effective Programming. Chapter 17th Concurrency with Future
    -  Quinlan, Brian: The Future is soon! (https://pyvideo.org/pycon-au-2010/pyconau-2010--the-future-is-soon.html) 
        at PyCon Australia 2010 (INTRODUCTION OF PEP 3148)
    -  Raymond Hettinger, Keynote on Concurrency, PyBay 2017(https://www.youtube.com/watch?v=9zinZmE3Ogk)
    -  Disassembled code created by David Gutierrez 
    -  Mariatta, Andrew Svetlov - Hands-on Intro to aiohttp - PyCon 2019
       https://www.youtube.com/watch?v=OxzVApXKWYM
       https://us-pycon-2019-tutorial.readthedocs.io/asyncio_intro.html  
    -  Miguel Grinberg Asynchronous Python for the Complete Beginner PyCon 2017
       https://www.youtube.com/watch?v=iG6fr81xHKA

## A brief introduction to the state of concurrency in Python

    In order to review  the state of Concurrency and Paralellism in Python, we will have 4 talks
    
    - First part:  The Future is Now.  Concurrency with Futures.
    - Second part: As old as Dijkstra. Concurrency with Threads.
    - Third part:  The big Revolution. Async I/O. Concurrency with Python asyncio.
    - Fourth part: Blame DS and AI :   Parallelism
 
   SOME HISTORY AND TERMS USED IN CONCURRENCY PROGRAMMING
       
        PYTHON THREADS ARE GREAT AT DOING NOTHING" , David Beazley

          
                            Python 3.2/ 2011        Python 3.4/2014
                                                   Created by Guido

                           +----------------------+--------------------------------+
                           | current.futures      | asyncio                        |
                           |  ThreadpoolExecutor  |                                |
                           |Context Manager       |                                +
       +-------------------+----------------------+--------------------------------+
       |Threads, Locks     | Threads, Lock        |generators,coroutines, Async I/O|
       | Semaphores,Queues | Semaphores, Queues   |not blocking loops, call back fn|
       |Events,Timer       | Events,Timer         |                                |
       +-------------------+----------------------+--------------------------------+
       |                                          |                                |
       | Multi Thread Processing                  | Single Thread Processing       |
       |                                          |                                |
       +------------------------------------------v--------------------------------+
       |                                                                           |
       | CONCURRENCY IN PYTHON:Dealing with lots of things at once                 |
       |                                                                           |
       +---------------------------------------------------------------------------+

A note to make a difference between  Parallelism and Concurrency
    - Above image applies to concurrency , NOT  parallelism
    - Parallelism is about doing lost of things at the same time and implies , using multiple CPU at once
    - In the Fourth part of this serie, we will talk about Parallelims also know as Multiprocessing


## I- First part: The Future is Now: Concurrency with Futures 

- Explain countries flag example: sequential download scripts ( flags.py)
- Explain concurrency case using concurrent.futures package with class ThreadPoolExecutor(flags_threadpool.py)
  - Follow the class to see the concurrent.future library in 
    https://github.com/python/cpython/blob/3.8/Lib/concurrent/futures/__init__.py
    https://github.com/python/cpython/blob/3.8/Lib/concurrent/futures/thread.py
    https://github.com/python/cpython/blob/3.8/Lib/concurrent/futures/_base.py
       Make them observe the Context manager __enter__ __exit__ in ThreadPoolExecutor class declaration
- Explain the benefits of these High Level Interfaces that owns a pool of worker threads or processes and 
   also a Queue for the tasks, but we do not need to know about this !!!
- But what is future, we just saw a mapping?
- A feature is a deferred execution and we see that only on
- Indeed with res = executor.map(download_one, sorted(cc_list))  # <6> we don't use any deferred excution
- For that see examples 

 https://stackoverflow.com/questions/60048835/avoiding-race-condition-while-using-threadpoolexecutor/60050144#60050144

- In no one  of the two concurrent  examples that we have seen so far we are able to perform download in paralell.
That is limited by the GIL. We do have multi thread but juts one thread at the time is executing
- So concurrent.futures are limited by the GIL. It is because the CPython interpreter is not Thread safe , so it has the 
GIL "Global Interpreter Lock" which allow only one thread at eh time to be executed
- When we write Python doe , we have no control over the GIL , but a build-in function or an extension in C 
can release the GIL
- So a Python library coded in C can manage the GIL,launch its own threads, and take advantages of all available 
CPU cores !!!
- This complicates the code of the library considerably and most library authors' do not do it!!
- If futures.ThreadPoolExecutor is not flexible enough for what we want ,  we ca build our own solution out of thread 
  components modules : Threads, Semaphores, and thread safe Queues. 
  
  In brief:
  -Futures offers less flexibility than traditional threads , however it encapsulate a lot of functionality
  that can help us solve some of our tasks without the complexity presented by traditional threads
  - There is much more than we have seen here 

    
## Second part: As old as Dijkstra: Concurrency with Threads. 

Example 18.1 spinner_thread.py 
    
    - The Class Signal is used  stop the thread from outside.In Python there is no API to terminate a thread once 
        it starts.
    - We will call the spin class in a separate Thread.
    - The principal thread keeps executions
    - The slow function simulates an slow computation or I/O.It blocks the main thread, but at that moment , 
    the GIL will be released , and the secondary thread will continues.
    - Explain the class how the programs works.Note that slow_function takes 3 sec, enough time to complete spin
    - But spin runs in an infinite cycle. So in one of those .1 sec (and after the main loop finished with slow_fun), 
    signal.go = False 
    - Spin breaks out of the infinite cycle created by itertools
    - . spinner.join() Before returning result , the main loop stops and awaiting for spiner threads finishes.
    - result is returned and we print the Answer
    
    The solution use a Class Signal to replace a Thread.Event(). Our example here uses Thread Event

This is a simple case of Python pure Thread usage.But we should note the following

    - As concurrent.future, we are using Threads ( :-) )
    - if we need to wait for the secondary Thread to finish we had to use a join() method on that thread
    - Threat are created, but they do not start until we invoque spinner.start()
    - We can pass arguments to the function that runs in the secondary thread:
    ```python
        spinner = threading.Thread(target=spin,
                               args=('thinking!', done))
    ```
    - Had we used multithread to run and write over
    - Threads are owned for the OS , so we have a limitation in its use
    - Threads are expenses to create (les tha process sure) but still expensives
    - The switching from threads is decided by the OS, sometime in teh most improper moment
    - We will see that  in async I/O this change occurrs at teh will of thea application
    
- Why we need thread safe Queues and locks if we have the GIL ? (exercise2.py)

     ....WINTER IS COMING : A nightmare with Threads
    
    - Runs first exercise1.py in concurrency_keynote.. folder so the classroom can see the expected result 
    - Despite the GIL allowing one thread at a time , race conditions could exist , giving us unexpected results 
    - Due to the GIL, there is only ever one thread per process active to execute Python bytecode
    - It means that actions that can be done in one bytecode can be thread safe, everything else is not.
    - Quickly take a look at Ramond talk in PyBay 2017
    - Explain exercise2.py in KeyNotes Folder
    - Explain the disassembled code I added to show how indeed the print() function and the counter +=1 assignation
      are build of multiple bytecode that are not thread safe as the GIL protect only one bytecode instruction
    - Do not go the solution of this exercise .It will take too much time. Just note the race condition , why it occurred
     and keep the Thread example in 18-asyncio-py3.7 , spinner_thread.py and note that the solution will involve Queues
     and other threads mechanism.Note how easily thread programming get complicated 
     
## Third  part:  The big Revolution:  Async I/O 

- INTRODUCTION
- Talk about  Guido , Marietta and Miguel work for Python 
- Ask the class to follow them in Twitter so they could see how they think and behave and what they do and have done
- Compare Flask Course form Miguel 
- Talk about O'reilly Hur Flask course
- Note that Python is free
- CLASS DETAILS
- Quickly review with the class Pycon 2017 Miguel Grinberg Asynchronous Python for the Complete Beginner PyCon 2017
- Go into  Mariatta Talk in PyCon 2019


## Four   part:  Blame DS and AI : Parallelism 
    

