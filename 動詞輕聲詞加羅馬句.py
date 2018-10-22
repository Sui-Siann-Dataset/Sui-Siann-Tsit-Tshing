import csv
import sys
from 加羅馬句 import _tau_phah_ji
from 文字檔加羅馬句 import _thoo_ku_txt

def _thak_guanpun_csv():
    全部句陣列 = []
    with open("../動詞輕聲詞.csv", 'r') as csvTong:
        rows = csv.DictReader(csvTong)
        for 逝 in rows:
            if 逝['例XXXXXX句1'] and 逝['例句1'] != "x":
                羅馬句 = _tau_phah_ji(逝['例XXXX句1'])
                全部句陣列.append({
                    '句漢': 逝['例句1'],
                    '句羅': 羅馬句
                })
            if 逝['例XXXXXXX句2'] and 逝['例句2'] != "x":
                羅馬句 = _tau_phah_ji(逝['例句XXXX2'])
                全部句陣列.append({
                    '句漢': 逝['例句2'],
                    '句羅': 羅馬句
                })
    return 全部句陣列

def _khangkhue(原始檔名, 輸出檔名):
    全部句陣列 = _thak_guanpun_csv()
    _thoo_ku_txt(全部句陣列, 輸出檔名)



if __name__ == '__main__':
    try:
        原始檔名 = sys.argv[1]
        輸出檔名 = sys.argv[2]
    except IndexError:
        print('請傳原始檔名kah輸出檔名……')
        exit(0)
    _khangkhue(原始檔名, 輸出檔名)
