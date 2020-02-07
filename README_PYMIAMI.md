# PyMiami Concurrency Talk

###  I ASKED THE  PARTICIPANTS TO NOT RUN THIS EXERCISE AS IT COULD BE SEEING AS A DoS ATTACK 

Please clone the repo to follow up with this talk

git remote add origin https://github.com/david68cu/pymiami_concurrency_talk_Feb_2020.git


## First part:  Concurrency with Futures
## Second part:  Concurrency with Threads
## Third part:  Concurrency with Async I0
## Fourth part: Parallelism

#### ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
####   CREATED BY DAVID GUTIERREZ FOR PYMIAMI TALK FEB 2020 FIU 
####   david@pythonsoftware.solutions , david@pymiami.org
####   https://www.pymiami.org , https://www.pythonsoftware.solutions
#### ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   
           


          
                            Python 3.2/ 2011        Python 3.4/2014
                                                   Created by Guido

                           +----------------------+--------------------------------+
                           |current.futures       | asyncio                        |
                           |  ThreadpoolExecutor  |                                |
                           |Context Manager       |                                +
       +-------------------+----------------------+--------------------------------+
       |Threads, Locks     | Threads, Lock        |generators,coroutines, Async I/O|
       | Semaphores,Queues | Semaphores, Queues   |not blocking loops, call back fn|
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



### PYTHON THREADS ARE GREAT AT DOING NOTHING" , David Beazley

#### ~~~~~~~~~~~ First part:  Concurrency with Futures ~~~~~~~~~~~~~~~~~~~~~~~~~~

- Explain different kind of concurrency in Python: Threads (Threads, current.futures.ThreadPoolExecutor, Async I/O), Multiprocessing
- Explain Thread with more details and its Feature
- Explain countries flag example: sequential download scripts ( flags.py)
- Explain concurrency case using concurrent.futures package with class ThreadPoolExecutor(flags_threadpool.py)
  - Follow the class to see the concurrent.future library in 
    https://github.com/python/cpython/blob/3.8/Lib/concurrent/futures/__init__.py
    https://github.com/python/cpython/blob/3.8/Lib/concurrent/futures/thread.py
    https://github.com/python/cpython/blob/3.8/Lib/concurrent/futures/_base.py
       Make them observe teh Context manager __enter__ __exit__ in ThreadPoolExecutor class declaration
- Explain the benefits of these High Level Interfaces that owns a pool of worker threads or processes and 
   also a Queue for the tasks, but we do not need to know about this
- But what is future, we just saw a mapping?
- A feature is a deferred execution and we see that only on
- Indeed with res = executor.map(download_one, sorted(cc_list))  # <6> we don't use any deferred excution
- For that see examples 

 https://stackoverflow.com/questions/60048835/avoiding-race-condition-while-using-threadpoolexecutor/60050144#60050144

- In no one  of the two concurrent  examples that we have seen so far we are able to perform download in paralell.
That is limited by teh GIL. We do have multi thread but juts one thread at the time is executing
- So concurrent.futures are limited by teh GIL. It is because teh CPython interpreter is not Thread safe , so it has the 
GIL "Global Interpreter Lock" which allow only one thread at eh time to be executed
- When we write Python doe , we have no control over the GIL , but a build-in function or an extension in C 
can release the GIL
- So a Python library coded in C can manage the GIL,launch its own threads, and take advantages of all available 
CPU cores !!!
- This complicates the code of the library considerably and most library authors' do not do it!!
- If futures.ThreadPoolExecutor is not flexible enough for what we want ,  we ca build our own solution out of thread 
  components modules : Threads, Semaphores, and thread safe Queues. 

    
## References

## Examples where taken from 

-  Ramalho, Luciano. Fluent Python: Clear, Concise, and Effective Programming. Chapter 17th Concurrency with Future
-  Quinlan, Brian: The Future is soon! (https://pyvideo.org/pycon-au-2010/pyconau-2010--the-future-is-soon.html) 
    at PyCon Australia 2010 (INTRODUCTION OF PEP 3148)
-  Raymond Hettinger, Keynote on Concurrency, PyBay 2017(https://www.youtube.com/watch?v=9zinZmE3Ogk)
-  Stack Overlow Question: Is there a Race Condition in my code? While using current.futures.ThreadPoolExecutor
    (Race)[https://stackoverflow.com/questions/60048835/avoiding-race-condition-while-using-threadpoolexecutor/60050144#60050144] 