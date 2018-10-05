from unittest.case import TestCase
from 加羅馬句 import tsuan


class 轉整合試驗(TestCase):
    def test轉逗號和首字小寫(self):
        鬥拍字的句 = "Piān-sóo sé bô tshing-khì，A móo ní á bī ē tsiok-tāng ê ooh。"
        按算 =  "Piān-sóo sé bô tshing-khì, a móo ní á bī ē tsiok-tāng ê ooh."
        self.assertEqual(tsuan(鬥拍字的句), 按算)
  
    