import threading
import time


def child():
    print(f"{threading.current_thread().name} borned")
    time.sleep(2)
    print(f"{threading.current_thread().name} Died")


def parents():
    print("Parents made a child")
    t = threading.Thread(target=child, name="New Child")
    t.start()
    t.join()
    print("Parents did well")


parents()


print("All threads have finished")
