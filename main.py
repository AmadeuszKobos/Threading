import threading
import time

done = False


def worker():
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(counter)


def daemon_worker(text):
    counter = 0
    while True:
        time.sleep(1)
        counter += 5
        print(f"{text}", counter)


worker_thread = threading.Thread(target=worker)

daemon_worker_thread = threading.Thread(target=daemon_worker, daemon=True, args=("Value: ",))

# daemon=True means that when all important threads will end we can end the program without waiting till this thread end

# worker_thread.start()
daemon_worker_thread.start()

input("Press enter to quit")
done = True


