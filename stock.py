import requests
from requests.adapters import HTTPAdapter
from data import data

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': '0',
    'Connection': 'keep-alive',
    'Host': 'hq.sinajs.cn',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}


def getstock(s, code):
    req = s.get(f'http://hq.sinajs.cn/list={str(code)}', headers=headers, timeout=3)
    if code[1] == 'z':
        result = req.text[11:].split(',')[:-1]
    else:
        result = req.text[11:].split(',')[:-2]
    if len(result) <= 1:
        print(code, result)
        raise IndexError
    return result[0], result[1:]


def create_session():
    s = requests.session()
    s.mount('http://', HTTPAdapter(max_retries=3))
    s.mount('https://', HTTPAdapter(max_retries=3))
    return s


if __name__ == '__main__':
    s = create_session()
    a = data(getstock(s, 600370)[1])
    print(str(tuple(i for i in a)))
