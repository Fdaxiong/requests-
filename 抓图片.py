import os
import requests
from lxml import etree

url = "https://bobopic.com/category/chahua"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"}
response = requests.get(url, headers=headers)

html = etree.HTML(str(response.text))

# 专题链接列表
list_img_rul = html.xpath("//div[@class='entry-media with-placeholder']/a/@href")
# 专题名字列表
list_img_rul_name = html.xpath("//h2[@class='entry-title']/a/text()")
# print(list_img_rul)


# 创建文件夹,以专题名字命名
for i in list_img_rul_name:
    print(i)
    try:
        os.mkdir("./img")
    except FileExistsError:
        pass
    try:
        os.mkdir("./img/%s" % i)
    except FileExistsError:
        pass

# 循环每一个专题名字列表,拿到单个专题名字
for i in list_img_rul_name:
    num = 1
    print(i)
    # print(list_img_rul)

    # 循环每一个专题链接,拿道每一个专题链接里面的图片链接列表
    url_index = list_img_rul_name.index(i)
    response = requests.get(list_img_rul[url_index], headers=headers)
    html = etree.HTML(str(response.text))
    img_url_list = html.xpath("//div[@class='card']/a/@href")  # 专题里面的图片
    print("1")
    print(img_url_list)
    print("2")

    # 循环每一个图片列表 拿到每一个图片链接
    for v in img_url_list:
        print(v)
        list_img_rul_one = requests.get(v, headers=headers)
        with open(r".\img\%s\%d.jpg" % (i, num), "wb")as f:
            f.write(list_img_rul_one.content)
            num += 1

