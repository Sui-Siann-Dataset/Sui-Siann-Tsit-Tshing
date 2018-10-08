from 加羅馬句 import _tau_phah_ji


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
            break
    return 全部句陣列


def _thoo_txt(全部句陣列):
    with open("../Gin-A-Koo/漢羅句.txt", 'w', encoding='utf-8') as txtTong:
        for 句 in 全部句陣列:
            print(句['句漢'], file=txtTong)
            print(句['句羅'], file=txtTong)
            print("", file=txtTong)


def _khangkhue(檔名):
    # gin-a-koo文字檔
    全部句陣列 = _thak_koosu_txt(檔名)
    _thoo_txt(全部句陣列)


if __name__ == '__main__':
    _khangkhue("../Gin-A-Koo/賣圓仔的神仙_林麗黛.txt")
