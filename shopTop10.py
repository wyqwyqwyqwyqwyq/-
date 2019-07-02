#top10商铺详细信息

import csv

from base.mysqlReturn import mysqlReturn


def foodRangingCity(shopName):
    sql = '''SELECT city, shopUrl,shopName,(tasteScore+environmentScore+serviceScore)/3.0 as avg,shopPower,mainRegionName,mainCategoryName,tasteScore,environmentScore,serviceScore,avgPrice,shopAddress from dazhongfood where city="%s" GROUP BY (tasteScore+environmentScore+serviceScore)/3.0 DESC limit 10;
'''%(shopName)
    listData = mysqlReturn(sql)
    return listData




if __name__ == '__main__':
    list_city = ['上海','北京','南京','天津','广州','成都','杭州','武汉','深圳','苏州','西安','重庆']
    for data in list_city:
        print(list(foodRangingCity(data)))
        with open('../data/top10.csv', 'a', encoding="utf-8") as f:
            f_csv = csv.writer(f)
            f_csv.writerows(list(foodRangingCity(data)))

