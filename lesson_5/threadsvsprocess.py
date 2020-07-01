import time
from threading import Thread
from multiprocessing import Process

def cpu_bound():
    return range(2700 ** 1000000)


def start_sync():
    start = time.time()

    cpu_bound()
    cpu_bound()
    cpu_bound()
    print(f'end in sync mode = {time.time() - start}')


def start_in_threads():
    start = time.time()

    t = Thread(target=cpu_bound)
    t2 = Thread(target=cpu_bound)
    t3 = Thread(target=cpu_bound)

    t.start(), t2.start(), t3.start()
    t.join(), t2.join(), t3.join()
    print(f'end in threads mode = {time.time() - start}')


def start_in_process():
    start = time.time()

    t = Process(target=cpu_bound)
    t2 = Process(target=cpu_bound)
    t3 = Process(target=cpu_bound)

    t.start(), t2.start(), t3.start()
    t.join(), t2.join(), t3.join()
    print(f'end in process mode = {time.time() - start}')


a = [0, 1, 2]

start_in_process()
start_sync()
start_in_threads()

