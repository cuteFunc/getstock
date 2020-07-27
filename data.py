class data:
    def __init__(self, data: list):
        self.list = [float(a) if '.' in a else int(a) for a in data[:-2]]
        self.list = self.list + data[-2:]
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.i += 1
            return self.list[self.i - 1]
        except Exception as e:
            raise StopIteration


if __name__ == '__main__':
    a = ['3.200', '3.180', '3.190', '3.210', '3.170', '3.180', '3.190', '3414850', '10897014.000', '134000', '3.180',
         '289200', '3.170', '167700', '3.160', '123500', '3.150', '110300', '3.140', '382100', '3.190', '348200',
         '3.200', '412000', '3.210', '51800', '3.220', '58100', '3.230', '2020-07-03', '11:30:00']
    b = data(a)
    print([i for i in b])
