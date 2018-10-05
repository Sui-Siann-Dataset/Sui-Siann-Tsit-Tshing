from unittest.case import TestCase
from 加羅馬句 import thauji_tsuan_sio_sia


class 首字轉小寫單元試驗(TestCase):
    def test逗號後壁轉小寫(self):
        鬥拍字的句 = "Lán，Àm-sî tsham mi só tsú"
        按算 =  "Lán，àm-sî tsham mi só tsú"
        self.assertEqual(thauji_tsuan_sio_sia(鬥拍字的句), 按算)
        
    def test足濟逗號(self):
        鬥拍字的句 = "Lán，Àm-sî tsham mi só tsú，Ū Àm-sî tsham mi só tsú"
        按算 =  "Lán，àm-sî tsham mi só tsú，ū Àm-sî tsham mi só tsú"
        self.assertEqual(thauji_tsuan_sio_sia(鬥拍字的句), 按算)
    
    def test無變(self):
        鬥拍字的句 = "Àm-sî tsham mi só tsú"
        按算 =  "Àm-sî tsham mi só tsú"
        self.assertEqual(thauji_tsuan_sio_sia(鬥拍字的句), 按算)
        
    