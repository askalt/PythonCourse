from multiprocessing import Queue, Process
from datetime import datetime
import time
from codecs import encode


def log(msg):
    print(f"[{datetime.now()}]: {msg}\n")


def worker_a(in_queue, out_queue):
    while True:
        try:
            msg = in_queue.get()
        except BaseException:
            return

        if msg is None:
            break

        log(f"a: received {msg}, go process")
        msg = msg.lower()

        try:
            time.sleep(5)
        except BaseException:
            return

        out_queue.put(msg)


def worker_b(in_queue, out_queue):
    while True:
        try:
            msg = in_queue.get()
        except BaseException:
            return
        if msg is None:
            break
        log(f"b: received {msg}, go encode")
        out_queue.put(encode(msg, "rot_13"))


if __name__ == "__main__":
    me_a_queue = Queue()
    a_b_queue = Queue()
    b_me_queue = Queue()

    process_a = Process(target=worker_a, args=(me_a_queue, a_b_queue))
    process_b = Process(target=worker_b, args=(a_b_queue, b_me_queue))
    process_a.start()
    process_b.start()

    while True:
        try:
            msg = input()
        except KeyboardInterrupt:
            me_a_queue.put(None)
            process_a.join()
            process_b.join()
            log("main: joined")
            break
        me_a_queue.put(msg)
