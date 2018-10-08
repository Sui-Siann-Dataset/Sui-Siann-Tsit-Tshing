from 加羅馬句 import _tau_phah_ji
import sys


def _thak_koosu_txt(檔名):
    全部句陣列 = []
    with open(檔名, 'r') as txtTong:
        rows = txtTong.readlines()
        for 逝 in rows:
            tsua = 逝.rstrip()
            羅馬句 = _tau_phah_ji(tsua)
            全部句陣列.append({
                '句漢': tsua,
                '句羅': 羅馬句
            })
    return 全部句陣列


def _thoo_txt(全部句陣列, 輸出檔名):
    with open(輸出檔名, 'w', encoding='utf-8') as txtTong:
        for 句 in 全部句陣列:
            print(句['句漢'], file=txtTong)
            print(句['句羅'], file=txtTong)
            print("", file=txtTong)


def _khangkhue(原始檔名, 輸出檔名):
    # gin-a-koo文字檔
    全部句陣列 = _thak_koosu_txt(原始檔名)
    _thoo_txt(全部句陣列, 輸出檔名)


if __name__ == '__main__':
    try:
        原始檔名 = sys.argv[1]
        輸出檔名 = sys.argv[2]
    except IndexError:
        print('請傳原始檔名kah輸出檔名……')
        exit(0)
    _khangkhue(原始檔名, 輸出檔名)
