import threading
from db_operation import run


def read_codes():
    with open('codes', 'r', encoding='utf8') as f:
        codes = f.read()
    return codes.split('\n')


def multithreading():
    threads = []
    codes = read_codes()
    for i in range(len(codes)):
        code = codes[i].split(',')[0]
        code = f'sz{code}' if code[0] == '0' else f'sh{code}'
        if code == 'sz000001':
            code = 'sh000001'
        t = threading.Thread(target=run, args=(code,))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()  # 加到主线程


if __name__ == "__main__":
    multithreading()
    # print(read_codes())
