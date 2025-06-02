from resonate import Resonate
from threading import Event


# Initialize Resonate and specify the group for this node
resonate = Resonate.remote(group="bar_nodes")


# Register bar() with Resonate
@resonate.register
def bar(_, v):
    print("running bar")
    return f"{v} world"


def main():
    # Start the Resonate node
    resonate.start()
    # Wait for an event to keep the script running
    Event().wait()


if __name__ == "__main__":
    main()
