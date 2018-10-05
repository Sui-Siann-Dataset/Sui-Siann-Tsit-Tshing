from unittest.case import TestCase
from 加羅馬句 import tshutai_tsuanhing_huho


class 轉換全形符號單元試驗(TestCase):
    def test甲(self):
        鬥拍字的句 = "Piān-sóo sé bô tshing-khì，A móo ní á bī ē tsiok-tāng ê ooh。"
        按算 =  "Piān-sóo sé bô tshing-khì, A móo ní á bī ē tsiok-tāng ê ooh."
        self.assertEqual(tshutai_tsuanhing_huho(鬥拍字的句), 按算)
        