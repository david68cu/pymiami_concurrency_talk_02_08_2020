
.. _ref_5_generator_functions:

Generator Functions ( yield appears)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Python provides generator functions as a convenient shortcut to building iterators.
    For this Python uses yield


    Simple generator function "countdown.py" , taken from  David Beazley... [9]

    .. code-block:: python

            #countdown.py
            # A simple generator function

            def countdown(n):
                print("Counting down from", n)
                while n > 0:
                    yield n
                    n -= 1
                print "Done counting down"

            # Example use
            if __name__ == '__main__':
                for i in countdown(10):
                    print(i)



    .. note::
        Note the use of the yield to the left of the value. The yield statement is pausing execution of the countdown() function
        and returning back to the caller both the n value and the control. It is important to see that the state of
        the countdown function remains the same therefore when the caller returns control to the generator , the function
        continues execution after the yield n statement !!


   A Python function that has the yield keyword in its body is a generator function.
   When this function is called it returns a generator object. In other words, a generator function is a generator
   factory, (...Luciano pag 428 [6])


   But ....

   people knew that if we took the "pausing" part of generators and added in a "send stuff
   back in" aspect to them, Python would suddenly have the concept of coroutines ..Brett [11]

   When a generator yields , it keep its state.

   As we have seen so far, generators are able to send values back to the caller.
   We'll see very soon that they will be able to accept values from the caller as well.
   But that will come with a price: they will be renamed to something called coroutines and deterred from the
   new world of async operations forever.

   .. They will land in a new world and will be forced to change their name, like Americans who
   wanted to immigrate to Spanish colonies, had to  change their names and last names from Robert Baker to
   Roberto Bequer. What an horror history is !!
    .. I don't recommend putting this, someone could take this statement personally and find it offensive.
