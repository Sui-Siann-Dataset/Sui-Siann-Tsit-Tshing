import sys
import re
from requests.exceptions import RequestException
import requests
import json
from json.decoder import JSONDecodeError
import csv


def _tau_phah_ji(漢字句):
    # 補段落的羅馬字
    羅馬句 = None
    try:
        r = requests.get('https://服務.意傳.台灣/標漢字音標', params={
            '查詢腔口': '閩南語',
            '查詢語句': 漢字句,
        })
    except RequestException as e:
        print(e)
        sys.exit(1)

    if r.status_code == requests.codes.ok:
        pkg_str = r.content.decode('unicode_escape')
        to_guan_arr = json.loads(pkg_str)
        try:
            # 提多元書寫的臺羅
            羅馬句 = to_guan_arr['多元書寫'][0]['臺羅']
        except ValueError:
            print('可能格式錯誤：{}\n\n'.format(漢字句))
        except IndexError:
            # 無法度提著多元書寫
            print('tsua:{},,,{}'.format(漢字句, to_guan_arr))
    else:
        print('回傳狀態毋是200：{}', 漢字句)

    return 羅馬句


def _thak_guanpun_csv():
    全部句陣列 = []
    with open("臺灣閩南語常用詞辭典-外來詞-glll4678整理.csv", 'r') as csvTong:
        rows = csv.DictReader(csvTong)
        for 逝 in rows:
            if 逝['例句1'] and 逝['例句1'] != "x":
                羅馬句 = _tau_phah_ji(逝['例句1'])
                全部句陣列.append({
                    '華語': 逝['華語'],
                    '臺羅': 逝['臺羅'],
                    '例句漢': 逝['例句1'],
                    '例句羅': 羅馬句
                })
            if 逝['例句2'] and 逝['例句2'] != "x":
                羅馬句 = _tau_phah_ji(逝['例句2'])
                全部句陣列.append({
                    '華語': 逝['華語'],
                    '臺羅': 逝['臺羅'],
                    '例句漢': 逝['例句2'],
                    '例句羅': 羅馬句
                })
                break
    return 全部句陣列


def _khangkhue():
    全部句陣列 = _thak_guanpun_csv()
    print(全部句陣列)
    
if __name__ == '__main__':
    _khangkhue()
