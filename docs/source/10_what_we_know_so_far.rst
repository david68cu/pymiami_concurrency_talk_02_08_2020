
.. _ref_10_what_we_know_so_far:

So at the end, what we need to know so far
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before trying to understand anything else  we need to go to David Beazley's curio GitHub implementation
`here <https://github.com/dabeaz/curio>`_.
No worries , we are not going to try to understand it. But  we will read something really interesting :

 "Curio - There Are Many Async Libraries, But This One is Mine"

Unfortunately on Thursday 20th, 2020  at around 7:00pm ET, just a few days after I had writen this part of the conference,
David Beazley changed the message  of curio to Curio - "It's the Sauce!"


Now you need to go to Brett Cannon essay in [7]. and  ,read this twice:

[7]....In that talk, David pointed out that async/await is really an API for asynchronous programming
(which he reiterated to me on Twitter). What David means by this is that people shouldn't think that async/await
as synonymous with asyncio, but instead think that asyncio is a framework that can utilize the async/await
API for asynchronous programming.

David Beazley actually believes this idea of async/await being an asynchronous programming API that he has created
the curio project to implement his own event loop. This has helped make it clear to me that async/await allows
Python to provide the building blocks for asynchronous programming, but without tieing you to a specific event
loop or other low-level details (unlike other programming languages which integrate the event loop into the
language directly). This allows for projects like curio to not only operate differently at a lower level
(e.g., asyncio uses future objects as the API for talking to its event loop while curio uses tuples), but to also
have different focuses and performance characteristics (e.g., asyncio has an entire framework for implementing
transport and protocol layers which makes it extensible while curio is simpler and expects the user to worry
about that kind of thing but also allows it to run faster)."


So at this point we should be clear of the following:

    - What is Async I/O ? (read above we discussed this concept before)
    - What is an Event Loop ? (read above we discussed this concept before)
    - async/await is an  asynchronous programming API
    - async/await allows Python to provide the building blocks for asynchronous programming
    - asyncio is a framework that can utilize the async/await API for asynchronous programming.
    - curio  is a library that uses  the async/await API for asynchronous programming.
    - trio is a library that uses the async/await API for asynchronous programming.
    - aiohttp is an asynchronous HTTP client/server framework for asyncio



