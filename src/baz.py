from resonate import Resonate
from threading import Event


# Initialize Resonate and specify the group for this node
resonate = Resonate.remote(group="baz_nodes")


# Register baz() with Resonate
@resonate.register
def baz(_, v):
    print("running baz")
    return f"{v}!"


def main():
    # Start the Resonate node
    resonate.start()
    # Wait for an event to keep the script running
    Event().wait()


if __name__ == "__main__":
    main()
