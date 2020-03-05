
.. _ref_7_interlude_generators:

Interlude : Generators are not Coroutines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    David Beazley minute 30:42 of Curious Course on Coroutines and Concurrency [9]

    Coroutines evolved from generators.From coroutines a new syntax gave birth to async and await keywords
    and that is the reason we have taken a look to all that here so far.

    But as David Beazley quoted in above references [9], generators are not coroutines.

|    Below Table show the differences.

    .. list-table:: Table 2 Differences between GENERATORS and COROUTINES
       :widths: 35 65
       :header-rows: 1

       * - GENERATORS
         - COROUTINES
       * - Produce data
         - Consume data
       * - Related to iteration
         - Nothing to do with iteration,even when producing values and Related to async behavior

|    Python’s coroutines, are special functions that give up control to the caller without losing their state, Dough Hellman [13]
|    They allow to return information from a pipe of multiple coroutines using yield from
|    They consume data and evolved from generators


