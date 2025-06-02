from resonate import Resonate


# Initialize Resonate as the default node group
resonate = Resonate.remote()


# Register foo() with Resonate
@resonate.register
def foo(ctx, greeting):
    print("running foo")
    greeting = yield ctx.rfc("bar", greeting).options(target="poll://bar_nodes")
    # to make this call asynchronous
    # promise = yield ctx.rfi("bar", greeting).options(target="poll://bar_nodes")
    # greeting = yield promise
    greeting = yield ctx.rfc("baz", greeting).options(target="poll://baz_nodes")
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
