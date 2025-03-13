from resonate.stores import RemoteStore
from resonate.task_sources import Poller
from resonate import Resonate
from threading import Event


# Initialize Resonate with a RemoteStore and a Poller task source
resonate = Resonate(
    store=RemoteStore(url="http://localhost:8001"),
    task_source=Poller(url="http://localhost:8002", group="bar_nodes"),
)


# Register bar() with Resonate
@resonate.register
def bar(_, v):
    print("running bar")
    return f"{v} world"


def main():
    # Wait for an event to keep the script running
    Event().wait()


if __name__ == "__main__":
    main()
