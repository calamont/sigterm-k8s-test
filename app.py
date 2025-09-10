import itertools
import signal
import time
from types import FrameType


class SigTermStatus:
    received: int = False

def handler(signum: int, frame: FrameType) -> None:
    if SigTermStatus.received:
        # Follow SIGTERM follow the default behaviour
        raise KeyboardInterrupt

    print("Got the SIGTERM")
    SigTermStatus.received = True

signal.signal(signal.SIGTERM, handler)

with open("/tmp/READY_AT", "w") as f:
    f.write("Created /tmp/READY_AT file")


count = itertools.count()
while not SigTermStatus.received:
    print(f"Starting iteration {next(count)}")
    time.sleep(1)
    print("Finishing iteration")

print("Finished")
# Sleep for a bit to allow you to review the logs in Kubernetes
time.sleep(60)
