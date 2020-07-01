import time
from threading import Thread, enumerate


def io_bound(idx, t):
    print(f'Operation with index {idx} started')
    time.sleep(t)
    print(f'Operation with index {idx} ended in {t} seconds')



start = time.time()
# io_bound(0, 3)
# io_bound(1, 4)
# io_bound(2, 3)

t = Thread(target=io_bound, args=(0, 0), name='Sleeping', daemon=True)
t2 = Thread(target=io_bound, args=(1, 6), name='blocking', daemon=True)
t3 = Thread(target=io_bound, args=(2, 3), name='io bound', daemon=True)
t4 = Thread(target=io_bound, args=(3, 3), daemon=True)

t.start()
t2.start()
t3.start()
t4.start()

print(t.is_alive(), t2.is_alive(), t3.is_alive(), t4.is_alive())

print(f'Total {time.time() - start}')