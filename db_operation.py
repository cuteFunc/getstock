import stock
import pymysql
import time
import sys

conf = {'host': "localhost", 'port': 3306,
        'user': "root", 'password': "123456", 'database': "stock", 'charset': "utf8", 'autocommit': True}


def operationdb(sql: str, creates='', **conf):
    conn = pymysql.connect(
        host=conf['host'],
        port=conf['port'],
        user=conf['user'],
        password=conf['password'],
        charset=conf['charset'],
        database=conf['database'],
        autocommit=conf['autocommit']
    )
    cur = conn.cursor()
    try:
        cur.execute(sql)
        sys.stdout.write(f"{time.strftime('%H:%M:%S', time.localtime())}--{sql}--已插入一条数据\n")
        cur.close()
    except Exception as e:
        sys.stdout.write(f"{e.args[0]}, {e.args[1]}\n")
        conn.rollback()
        if e.args[0] == 1146:
            cur.execute(creates)
        else:
            sys.stdout.write(f"{sql},{e}\n")
        cur.close()
    conn.close()


#
# def read_codes():
#     with open('codes', 'r', encoding='utf8') as f:
#         codes = f.read()
#     return codes.split('\n')
#
# def xiugai():
#     codes = read_codes()
#     for i in range(len(codes)):
#         code = codes[i].split(',')[0]
#         code = f'sz{code}' if code[0] == '0' else f'sh{code}'
#         if code == 'sz000001':
#             code = 'sh000001'
#         sql1 = f'alter table {code} drop primary key;'
#         sql2 = f'alter table {code} add PRIMARY KEY (`date`,`time`);'
#
#         operationdb(sql1, **conf)
#         operationdb(sql2, **conf)


def run(code):
    now_time = time.strftime("%H%M", time.localtime())
    while 1:
        sec = time.strftime("%H%M%S", time.localtime())
        sys.stdout.write(f"{sec}")
        if ('0929' <= now_time <= '1131') or ('1259' <= now_time <= '1501'):
            try:
                s = stock.create_session()
                data = stock.data(stock.getstock(s, code)[1])
                values = str(tuple(i for i in data))
                sql = rf'insert into `{code}` value{values};'
                creates = rf'''
                CREATE TABLE `{code}` (
                  `today_open_price` decimal(6,2) NOT NULL,
                  `yesterday_close_price` decimal(6,2) NOT NULL,
                  `current_price` decimal(6,2) NOT NULL,
                  `today_max_price` decimal(6,2) NOT NULL,
                  `today_min_price` decimal(5,2) NOT NULL,
                  `buy_price` decimal(5,2) NOT NULL,
                  `sell_price` decimal(5,2) NOT NULL,
                  `total_volume` decimal(12,0) NOT NULL,
                  `total_amount` decimal(13,2) NOT NULL,
                  `buy_one_volume` decimal(12,0) NOT NULL,
                  `buy_one_price` decimal(5,2) NOT NULL,
                  `buy_two_volume` decimal(12,0) NOT NULL,
                  `buy_two_price` decimal(5,2) NOT NULL,
                  `buy_three_volume` decimal(12,0) NOT NULL,
                  `buy_three_price` decimal(5,2) NOT NULL,
                  `buy_four_volume` decimal(12,0) NOT NULL,
                  `buy_four_price` decimal(5,2) NOT NULL,
                  `buy_five_volume` decimal(12,0) NOT NULL,
                  `buy_five_price` decimal(5,2) NOT NULL,
                  `sell_one_volume` decimal(12,0) NOT NULL,
                  `sell_one_price` decimal(5,2) NOT NULL,
                  `sell_two_volume` decimal(12,0) NOT NULL,
                  `sell_two_price` decimal(5,2) NOT NULL,
                  `sell_three_volume` decimal(12,0) NOT NULL,
                  `sell_three_price` decimal(5,2) NOT NULL,
                  `sell_four_volume` decimal(12,0) NOT NULL,
                  `sell_four_price` decimal(5,2) NOT NULL,
                  `sell_five_volume` decimal(12,0) NOT NULL,
                  `sell_five_price` decimal (5,2) NOT NULL,
                  `date` date NOT NULL DEFAULT '2000-01-01',
                  `time` time NOT NULL DEFAULT '00:00:00',
                  PRIMARY KEY (`date`,`time`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
                '''
                operationdb(sql, creates=creates, **conf)
            except Exception as e:
                sys.stdout.write(f"{e}\n")
            time.sleep(3)
        else:
            time.sleep(60)
        now_time = time.strftime("%H%M", time.localtime())


if __name__ == "__main__":
    run("600867")