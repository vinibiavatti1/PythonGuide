"""
Async and Await

* Async IO is a concurrent programming design that has received dedicated
  support in Python
* Asynchronous IO (async IO): a language-agnostic paradigm (model) that has
  implementations across a host of programming languages
* async/await: two new Python keywords that are used to define coroutines
* asyncio: the Python package that provides a foundation and API for running
  and managing coroutines
* References:
  * https://docs.python.org/3/library/asyncio.html

* Some features of asyncio are:
###############################################################################
Resource                    Description
###############################################################################
run()                       Create event loop, run a coroutine, close the loop.
create_task()               Start an asyncio Task.
to_thread()                 Asynchronously run a function in a separate OS
                            thread.
await sleep()               Sleep for a number of seconds.
await gather()              Schedule and wait for things concurrently.
await wait_for()            Run with a timeout.
await shield()              Shield from cancellation.
await wait()                Monitor for completion.
###############################################################################
"""
import asyncio


###############################################################################
# Async Function
###############################################################################


# Defining async function
# * To define a asynchronous function, just use the async keyword
async def async_function():
    print('Hello')
    await asyncio.sleep(1)
    print('World')
    return 'Finished!'


###############################################################################
# Running
###############################################################################


# Calling async function (normal way)
# * Using normal calling for async function will not work
# * The function will return a coroutine object, not the execution result
# * An error will be raised if async function is called without await keyword
print(async_function())
"""
<coroutine object async_function at 0x0000023E64261840>
RuntimeWarning: coroutine 'async_function' was never awaited
    print(async_function())
"""


# Calling async function
# * Using asyncio.run() function
asyncio.run(async_function())
# Hello
# World (after 1 second)


###############################################################################
# Tasks
###############################################################################


# Creating task
# * To create tasks, the asyncio.create_task() function can be used
async def task_example():
    task = asyncio.create_task(async_function(), name="My Task")
    await task


# Executing task
asyncio.run(task_example())
# Hello
# World


# Cancelling task
# * A task can be cancelled with task.cancel() method
# * The asyncio.CancelledError exception will be reaised if the task was
#   canceled and awaited
async def task_cancel_example():
    task = asyncio.create_task(async_function(), name="My Task")
    await asyncio.sleep(.5)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print('Cancelled!')


# Executing task
asyncio.run(task_cancel_example())
# Cancelled!


###############################################################################
# Running Concurrently
###############################################################################


# Multiple Tasks (Gather)
# * The asyncio.gather() function can be used to run concurrently
async def multiple_tasks_gather():
    await asyncio.gather(
        async_function(),
        async_function(),
        async_function()
    )


# Executing task
asyncio.run(multiple_tasks_gather())
# Hello
# Hello
# Hello
# World
# World
# World


# Multiple Tasks (Wait)
# * The asyncio.wait() function can be used to run concurrently, but is more
#   low level then asyncio.gather() and allows to configure if it has to wait
#   for all futures to finish or just the first one.
# * NOTE: It is necessary to use tasks, cause passing coroutine objects to
#   wait() directly is deprecated.
async def multiple_tasks_wait():
    t1 = asyncio.create_task(async_function())
    t2 = asyncio.create_task(async_function())
    done, pending = await asyncio.wait(
        [t1, t2],
        return_when=asyncio.ALL_COMPLETED
    )
    print('Tasks in done?', t1 in done, t2 in done)


# Executing task
asyncio.run(multiple_tasks_wait())
# Hello
# Hello
# World
# World
# Tasks in done? True True


###############################################################################
# Shield
###############################################################################


# Create task with shield to prevent cancellation
# * The asyncio.shield() function can be used to block the task for
#   cancellation
# * When the cancelation is executed, the shield will be canceled, but the
#   default task will continues to run
async def task_shield_example():
    task = asyncio.create_task(async_function(), name="My Task")
    safe_task = asyncio.shield(task)
    await asyncio.sleep(.5)
    safe_task.cancel()
    try:
        await safe_task
    except asyncio.CancelledError:
        print('Shield Cancelled.')
        print(f'{task.cancelled() = }')


# Executing task
asyncio.run(task_shield_example())
# Shield Cancelled!
# task.cancelled() = False


###############################################################################
# Timeout
###############################################################################


# Defining async function with timeout
# * To execute some async task with timeout, we can use the asyncio.wait_for()
#   function, and set the timeout parameter.
# * The asyncio.TimeoutError will be raised if the timeout get reached
async def timeout_function():
    try:
        await asyncio.wait_for(async_function(), timeout=.5)
    except asyncio.TimeoutError:
        print('Timeout!')


# Executing task
asyncio.run(timeout_function())
# Timeout!


###############################################################################
# Threads
###############################################################################


# Defining async function with thread
# * We can use the asyncio.to_thread() function to asynchronously run function
#   func in a separate thread.
async def thread_function():
    await asyncio.to_thread(print, 'Thread!')


# Executing task
asyncio.run(thread_function())
# Thread!
