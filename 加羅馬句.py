import sys
import re
from requests.exceptions import RequestException
import requests
import json
from json.decoder import JSONDecodeError
import csv

逗號首字 = re.compile('， *(.)')


def lowercaseLomaji(matchobj):
    return '，' + matchobj.group(1).lower()

def thauji_tsuan_sio_sia(鬥拍字的臺羅):
    return 逗號首字.sub(lowercaseLomaji, 鬥拍字的臺羅)


def tshutai_tsuanhing_huho(鬥拍字的臺羅):
    # 因為鬥拍字的羅馬字袂轉做半形符號
    臺羅句 = 鬥拍字的臺羅.replace("，", ", ")
    臺羅句 = 臺羅句.replace("。", ". ")
    臺羅句 = 臺羅句.replace("！", "! ")
    臺羅句 = 臺羅句.replace("？", "? ")
    臺羅句 = 臺羅句.rstrip()
    return 臺羅句


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
            羅馬句 = ""
            for 一多元 in to_guan_arr['多元書寫']:
                一子句 = tshutai_tsuanhing_huho(一多元['臺羅'])
                羅馬句 += 一子句
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
    return 全部句陣列


def _thoo_sin_e_csv(全部句陣列):
    with open("日語外來詞kap例句.csv", 'w', newline='', encoding='utf-8') as csvTong:
        欄位 = ['華語', '臺羅', '例句漢', '例句羅']
        writer = csv.DictWriter(csvTong, 欄位, delimiter='|')
        writer.writeheader()
        for 句 in 全部句陣列:
            writer.writerow(句)


def _thoo_txt(全部句陣列):
    with open("日語外來詞kap例句.txt", 'w', encoding='utf-8') as txtTong:
        for 句 in 全部句陣列:
            print(句['華語'], file=txtTong)
            print(句['臺羅'], file=txtTong)
            print(句['例句漢'], file=txtTong)
            print(句['例句羅'], file=txtTong)
            print("", file=txtTong)


def _khangkhue():
    全部句陣列 = _thak_guanpun_csv()
    # 目前無需要轉出csv
    #_thoo_sin_e_csv(全部句陣列)
    _thoo_txt(全部句陣列)


if __name__ == '__main__':
    _khangkhue()
