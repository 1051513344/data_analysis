

import pandas as pd
import unicodecsv as ucsv
from Tool.Predict import predict_passer
class C:

    def __init__(self, csv_path):

        self.temp = pd.read_csv("{}/data/all_temperature.csv".format(csv_path)).set_index("城市")
        self.wea = pd.read_csv("{}/data/all_weather.csv".format(csv_path)).set_index("城市")
        self.passer = pd.read_csv("{}/data/all_passer.csv".format(csv_path)).set_index("城市")

        self.temp_ = ""
        self.wea_ = ""
        self.passer_ = ""

        self.wea_dict = {
            20: 0,
            40: 0.15,
            60: 0.15,
            80: 0.3
        }

    def tem_section(self, tem):
        if tem>0 and tem<10:
            return 0.15
        elif tem>=10 and tem<25:
            return 0
        elif tem>=25 and tem<35:
            return 0.15
        else:
            return 0.3

    def passer_section(self, passer):
        if passer>0 and passer<0.3:
            return 0
        elif passer>=0.3 and passer<0.5:
            return 0.1
        elif passer>=0.5 and passer<0.7:
            return 0.2
        elif passer >= 0.7 and passer < 0.9:
            return 0.3
        else:
            return 0.4

    def score(self, tem, wea, passer):

        tem_score = self.tem_section(tem)
        wea_score = self.wea_dict.get(wea)
        passer_score = self.passer_section(passer)

        return (round(1 - tem_score - wea_score - passer_score, 2))*100

    def to_list(self):
        self.temp_ = self.temp["周五（13日）"]
        self.wea_ = self.wea["周五（13日）"]
        self.passer_ = self.passer["周五（13日）"]


        temp_list = [i for i in self.temp_.values]
        wea_list = [i for i in self.wea_.values]
        passer_list = [i for i in self.passer_.values]

        return temp_list, wea_list, passer_list

    def export(self):

        temp_list, wea_list, passer_list = self.to_list()
        province_list = [
            '河南', '北京', '河北', '辽宁', '江西', '上海', '安徽', '江苏', '湖南', '浙江',
            '海南', '广东', '湖北', '黑龙江', '澳门', '陕西', '四川', '内蒙古', '重庆', '云南',
            '贵州', '吉林', '山西', '山东', '福建', '青海', '天津'
        ]

        data = []

        with open('../data/score.csv', 'wb') as f:
            # 实例化csv写数据对象
            writer = ucsv.writer(f, encoding='utf-8')
            data.append(("城市", "分数"))
            for province, t, w, p in zip(province_list, temp_list, wea_list, passer_list):

                temp_l = self.temp.loc[province, "周五（6日）":]
                wea_l = self.wea.loc[province, "周五（6日）":]
                passer_l = self.passer.loc[province, "周五（6日）":]
                score = self.score(t, w, predict_passer(temp_l, wea_l, passer_l))
                data.append((province, score))

            writer.writerows(data)

c = C("..")
c.export()


