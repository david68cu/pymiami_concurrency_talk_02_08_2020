
.. _ref_3_how_async_io_works:

How the heck does async/await work in Python ? Brett  Cannon [11]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    When you feel afraid of not knowing enough about async I/O , it will be a relief to know that Brett  Cannon asked himself
    the above question in  [11]. Once you know who he is, you will feel an immediate peace of mind on having
    any doubts about async I/O. He too had doubts at some point!

    David Beazley in [8] and [9], clearly describes the evolution of async I/O.
    Meanwhile, Brett  Cannon in [11] starts by taking us back to the origin and uses of 'yield from'  in coroutines.
    David Beazley is the one that takes us even further back by starting for a differentiation between generators
    and coroutines.

    David Beazley makes the distinction that 'generators' and 'generator function' should be differentiated from coroutines in both
    its intention and uses. We will see this distinction below.
