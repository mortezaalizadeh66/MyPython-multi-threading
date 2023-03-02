import threading


def my_function():
    # code to be executed in the thread
    print("Thread running")
    print("My name is", t1.getName())
    print("My name is", t2.getName())


# create two threads
t1 = threading.Thread(target=my_function)
t2 = threading.Thread(target=my_function)

# Set New Names for two threads
t1.setName("T1")
t2.setName("T2")

# start the threads
t1.start()
t2.start()

# wait for the threads to finish
t1.join()
t2.join()


print("All threads have finished")
