import threading
import time

done = False

# Example 1


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
# daemon_worker_thread.start()


# Example 2
def timer1():
    numbers = [1, 2, 4, 5, 7, 8, 10]
    for number in numbers:
        print(number)
        time.sleep(1)


def timer2():
    numbers = [3, 6, 9]
    for number in numbers:
        print(number)
        time.sleep(3)


threading.Thread(target=timer1).start()
threading.Thread(target=timer2).start()


input("Press enter to quit")
done = True


