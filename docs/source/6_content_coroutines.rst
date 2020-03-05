
.. _ref_6_coroutines:

Coroutines and its importance in async operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    * The origins of the yield from keyword

        In  [6] , Chapter 16 Page 480, Luciano Ramalho  explains to us  " How Coroutines evolved form Generators" :
        On PEP 342 and PEP 380 , Luciano continues on [6],  .send() , throw() and .close() methods were added that
        allowed a caller to send() a datum into the generator , thrown and exception to be handled inside the generator,
        and terminate it.

        PEP 380 , added yield from syntax. that allows a generator , continues Luciano  in [6] in the same page 480.
        We can go deeper on the details of PEP 380, created by Gregory Ewing reading [16]

        Coroutines are just special generators .... You send values into

        Coroutines are very similar to generators in Python: they both use yield.
        Just the meaning of yield implies to 'let things go', to stop and let others continue. So, the yield keyword
        has an asynchronous meaning. Brett [8] .
        Coroutines suspend execution in the yield statement and pass control to the caller
        along with any value to the right of yield.
        Normal coroutines in python use yield to wait to receive an elements from the caller. Usually yield is to the right
        The caller send data to the coroutine using send.
        Coroutines are functions whose execution you can pause.

         We could see some examples of use of coroutines now , but what will be really useful is to see David Beazley examples
         in A Curious Course on Coroutines [9] ..., Part 1 : Introduction to Generators and Coroutines

     Then looking at Chapter [2] on David Bealey [9] , example copipe.py we will see how how to hook up a pipeline with
     coroutines.

     .. note::

         Note that stacking coroutines , meaning having one coroutine doing something passing the result of its operation
         to another coroutine so it does another things, with that kind of structure , we could get pretty powerful
         functionality. "yield from" will allow us to successfully concatenate coroutines and get messages passed back and
         forth from the caller to any coroutine in the pipe.

     Now is time we can understand and see "yield from" in Action , but taken a look to [6] Example 16-17, "Fluent Python",
     Luciano Ramalho Page [496]



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

