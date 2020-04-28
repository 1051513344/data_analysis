# import random
# import unicodecsv as ucsv
#
# province_list = [
#     '河南','北京','河北','辽宁','江西','上海','安徽','江苏','湖南','浙江',
#     '海南','广东','湖北','黑龙江','澳门','陕西','四川','内蒙古','重庆','云南',
#     '贵州','吉林','山西','山东','福建','青海','天津'
# ]
# data = []
#
# with open('../data/passenger_flow.csv', 'wb') as f:
#     # 实例化csv写数据对象
#     writer = ucsv.writer(f, encoding='utf-8')
#     data.append(("城市",
#                  "周四（12日）", "周五（13日）",
#                  "周六（14日）", "周日（15日）",
#                  "周一（16日）", "周二（17日）",
#                  "周三（18日）", "周四（19日）"))
#     for province in province_list:
#         random1 =  str(round(random.random(), 2))
#         random2 =  str(round(random.random(), 2))
#         random3 =  str(round(random.random(), 2))
#         random4 =  str(round(random.random(), 2))
#         random5 =  str(round(random.random(), 2))
#         random6 =  str(round(random.random(), 2))
#         random7 =  str(round(random.random(), 2))
#         random8 =  str(round(random.random(), 2))
#         data.append((province,random1, random2, random3, random4, random5, random6, random7, random8))
#
#     writer.writerows(data)


import pandas as pd

data = pd.read_csv("../data/passenger_flow.csv")
data = data.set_index("城市")

print(data)







