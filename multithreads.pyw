import threading
from db_operation import run


# def job(l, q):
#     global lock
#     lock.acquire()
#     for i in range(len(l)):
#         l[i] = l[i] ** 2
#     lock.release()
#     q.put(l)  # 必须用put拿返回结果


def multithreading():
    threads = []
    codes = ["603777", "601006", "600570"]
    for i in range(len(codes)):
        t = threading.Thread(target=run, args=(codes[i],))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()  # 加到主线程


if __name__ == "__main__":
    multithreading()
