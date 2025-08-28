"""
Async IO

* The async IO model allows for concurrent execution of code, making it easier
  to write programs that perform I/O-bound tasks without blocking the main
  thread.
* The model is based on the concept of coroutines, which are special functions
  that can be paused and resumed, allowing for more efficient use of resources.
* The `asyncio` library is a core part of the async IO model in Python,
  providing the necessary tools and infrastructure to work with asynchronous
  code, such as event loops, coroutines, and tasks.
* When importing the `asyncio` library, the `async` and `await` keywords are
  activated and can be used to define and work with coroutines.
* It is a lightweight and efficient way to handle asynchronous programming in
  Python compared to traditional threading or multiprocessing approaches.
"""


###############################################################################
# Enabling Async IO
###############################################################################


# Enabling Async IO
# * To enable the `async` and `await` keywords, and the coroutine support in
#   Python, you need to import the `asyncio` library at the beginning of your
#   script.
import asyncio


###############################################################################
# Async Function
###############################################################################


# Defining an async function
# * The async keyword is used in functions to define that the function is a
#   coroutine.
async def my_coroutine():
    print('Hello World')


# Calling an async function
# * When an async function is called, it will not execute immediately. Instead,
#   it returns a coroutine object that can be awaited.
# * Note that the interpreter will issue a warning if the coroutine is not
#   awaited.
x = my_coroutine()
print(x)
# <coroutine object my_coroutine at 0x0000023E64261840>
# <sys>:0: RuntimeWarning: coroutine 'my_coroutine' was never awaited


###############################################################################
# Await
###############################################################################


# Await
# * The await keyword is used to pause the execution of a coroutine until the
#   awaited task is complete.
# * It can only be used inside an async function.
# * When the awaited task is complete, the coroutine resumes execution.
# * NOTE: The await keyword can only be used inside async functions. If a
#   non-async function tries to use await, it will raise a SyntaxError.
async def other_coroutine():
    await my_coroutine()  # Runs and waits for my_coroutine to finish
    print('Finished!')


###############################################################################
# Running Coroutines
###############################################################################


# Running the main coroutine
# * When developing an async modules, we must use `asyncio.run()` to run the
#   main coroutine, since we cannot use await at the top level.
# * This function creates a new event loop, runs the coroutine, and closes the
#   loop when the coroutine is done.
asyncio.run(my_coroutine())


###############################################################################
# Timeout
###############################################################################


# Defining a coroutine
# * For the example below, we will need to define a coroutine.
# * This coroutine will accept arguments and return a value.
# * The `asyncio.sleep()` function is used to simulate a long-running
#   operation.
async def long_task():
    await asyncio.sleep(10)


# Defining timeouts
# * To execute some async task with timeout, we can use the
#   `asyncio.wait_for()` function, and set the timeout parameter.
# * The asyncio.TimeoutError will be raised if the timeout get reached.
async def my_coroutine():
    try:
        await asyncio.wait_for(long_task(), timeout=.5)
    except asyncio.TimeoutError:
        print('Timeout!')


# Running example
# * We will run the example above to see the results.
asyncio.run(my_coroutine())
# Timeout!


###############################################################################
# Tasks
###############################################################################


# Defining a coroutine
# * For the example below, we will need to define a coroutine.
# * This coroutine will accept arguments and return a value.
# * The `asyncio.sleep()` function is used to simulate a long-running
#   operation.
async def long_task():
    await asyncio.sleep(10)
    return 'Long task result'


# Creating a Task
# * A task is a coroutine that has been wrapped in a Task object.
# * Tasks are used to have more control over the execution of coroutines.
# * A task is performed in the exact moment it is defined, and the await only
#   waits for this task if it is not already finished. This enables more
#   control over the execution flow.
# * Note that if the coroutine returns a value, it can be retrieved with the
#   await, even if the task is already done.
async def my_coroutine():
    task = asyncio.create_task(long_task(), name='My Task')
    await asyncio.sleep(.5)
    if not task.done():
        task.cancel()
        print('Task cancelled!')
    else:
        result = await task
        print(f'Task done! Result: {result}')


# Running example
# * We will run the example above to see the results.
asyncio.run(my_coroutine())
# Task cancelled!


###############################################################################
# Running Multiple Coroutines
###############################################################################


# Defining a coroutine
# * For the example below, we will need to define a coroutine.
# * This coroutine will accept arguments and return a value.
async def coro_1(arg):
    return arg + 1


# Defining other coroutine
# * We will define another coroutine that performs a different operation.
async def coro_2(arg):
    return arg * 2


# Running multiple coroutines concurrently (gather)
# * To run multiple coroutines concurrently, we can use `asyncio.gather()`
# * This method takes multiple awaitable objects and runs them concurrently.
# * It will wait for all of the coroutines to finish and return their results.
# * To get the results, we can unpack the returned values from
#   `asyncio.gather()`.
async def run_coroutines():
    results = await asyncio.gather(
        coro_1(1),
        coro_2(2)
    )
    print(results)


# Running example
# * We will run the example above to see the results.
asyncio.run(run_coroutines())
# [2, 4]


# Running multiple coroutines concurrently (wait)
# * The `asyncio.wait` allows you to run multiple coroutines (or tasks)
#   concurrently.
# * The main difference between `asyncio.gather` and `asyncio.wait`:
#   * `gather` returns the results of all coroutines in order.
#   * `wait` returns two sets: the tasks that are done and those still pending.
# * The `wait` is useful when you want to monitor or manage tasks individually,
#   for example, to cancel some or handle them as they complete.
# * The `return_when` parameter allows you to specify when the wait should
#   stop: (asyncio.FIRST_COMPLETED or asyncio.ALL_COMPLETED)
async def run_coroutines():
    tasks = [
        asyncio.create_task(coro_1(1)),
        asyncio.create_task(coro_2(2))
    ]
    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.ALL_COMPLETED
    )
    results = [task.result() for task in done]
    print(results)


# Running example
# * We will run the example above to see the results.
asyncio.run(run_coroutines())
# [2, 4]
