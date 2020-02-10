# More Careful Threading with Queues
# Interestingly, the rules for threading are just for computing and programming. The physical world is
# full of concurrency as well. Many of these techniques has physical analogs that are useful
# for managing people and projects.

# Read The 5 rules RR1000-RR1005 on the Reference section of th e README.md file
# [Slides and Notes: Key notes on  Concurrency](https://pybay.com/site_media/slides/raymond2017-keynote/threading.html)

# So we will create two Queues,
#
# Queues: counter_queue and print_queue
# Queue Managers methods : def counter_manager(): and def print_manager():

# Read all documentation in the README.md References section

import threading, time, random, queue

##########################################################################################
# Fuzzing is a technique for amplifying race condition errors to make them more visible

FUZZ = True


def fuzz():
    if FUZZ:
        time.sleep(random.random())

###########################################################################################


counter = 0

counter_queue = queue.Queue()


def counter_manager():
    'I have EXCLUSIVE rights to update the counter variable'
    global counter

    while True:
        increment = counter_queue.get() # Used by queue consumer threads to start processing the queue
        fuzz()
        oldcnt = counter
        fuzz()
        counter = oldcnt + increment
        fuzz()
        print_queue.put([
            'The count is %d' % counter,
            '---------------'])
        fuzz()
        # For each get() used to fetch a task, a subsequent call to task_done()
        # tells the queue that the processing on the task is complete.
        counter_queue.task_done()


t = threading.Thread(target=counter_manager)
t.daemon = True
t.start()
del t


###########################################################################################

print_queue = queue.Queue()


def print_manager():
    'I have EXCLUSIVE rights to call the "print" keyword'
    while True:
        job = print_queue.get()  # Used by queue consumer threads to start processing the queue
        fuzz()
        for line in job:
            print(line, end='')
            fuzz()
            print()
            fuzz()
        # For each get() used to fetch a task, a subsequent call to task_done()
        # tells the queue that the processing on the task is complete.
        print_queue.task_done()
        fuzz()


t = threading.Thread(target=print_manager)
t.daemon = True
t.start()
del t

# ----------------------------------------------------------------


def worker():
    'My job is to increment the counter and print the current count'
    counter_queue.put(1)
    fuzz()


# main loop below
if __name__ == "__main__":
    print_queue.put(['Starting up'])   # We do not print directly but send a message to the print_queue
    fuzz()

    # We will append all created threads here so we can join() all of them one by one, later
    # Had we used ThreadPool from concurrent.future , we do not need this as we could had use a
    # context Manager that controls a with statement that uses __exit__ and automatically do the join()
    worker_threads = []

    for i in range(10):
        t = threading.Thread(target=worker)
        worker_threads.append(t)
        t.start()
        fuzz()
    for t in worker_threads:
        fuzz()
        # Wait until the thread terminates. This blocks the calling thread until the thread terminates
        # either normally or through an unhandled exception –or until the optional timeout occurs.
        # join() raises a RuntimeError if an attempt is made to join the current thread as that would cause a deadlock
        t.join()

    # When all workers are done we print Finishing up , so we wait for them to finish with a join
    counter_queue.join()   # Queue.join() Blocks until all items in the queue have been gotten and processed.
    fuzz()
    print_queue.put(['Finishing up'])
    fuzz()
    print_queue.join()     # Queue.join() Blocks until all items in the queue have been gotten and processed.
    fuzz()
