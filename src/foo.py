from resonate.stores import RemoteStore
from resonate.task_sources import Poller
from resonate.targets import poll
from resonate import Resonate


# Initialize Resonate with a RemoteStore and a Poller task source
resonate = Resonate(
    store=RemoteStore(url="http://localhost:8001"),
    task_source=Poller(url="http://localhost:8002"),
)


# Register foo() with Resonate
@resonate.register
def foo(ctx, greeting):
    print("running foo")
    greeting = yield ctx.rfc("bar", greeting).options(send_to=poll("bar_nodes"))
    # to make this call asynchronous
    # promise = yield ctx.rfi("bar", greeting).options(send_to=poll("bar_nodes"))
    # greeting = yield promise
    greeting = yield ctx.rfc("baz", greeting).options(send_to=poll("baz_nodes"))
    return greeting


# Define the main function
def main():
    try:
        # Invoke foo()
        handle = foo.run(id="hello-world-greeting", greeting="hello")
        # Print the result of foo()
        # handle.result() is a blocking call
        print(handle.result())
    except Exception as e:
        print(e)


# Run the main function when the script is invoked
if __name__ == "__main__":
    main()
