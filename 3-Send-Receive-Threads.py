import threading
import time
import queue


def sender(q):
    print("Sender started")
    # Create 5 messages and push them in the Queue
    for i in range(5):
        print(f"Sending message {i}")
        q.put(f"Message {i}")
        time.sleep(1)
    q.put(None)
    print("Sender finished")


def receiver(q):
    print("Receiver started")
    while True:
        # listening to the Queue to POP from Queue
        message = q.get()
        if message is None:
            break
        print(f"Received message: {message}")
    print("Receiver finished")

# Initial  Queue
q = queue.Queue()


# Initial  Threads and connect it to the Queue
t1 = threading.Thread(target=sender, args=(q,))
t2 = threading.Thread(target=receiver, args=(q,))

# Start the Threads
t1.start()
t2.start()

t1.join()
t2.join()
