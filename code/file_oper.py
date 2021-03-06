#将文件存入mongo 并取出

from pymongo import MongoClient
import bson.binary

from_img = "flower.jpg" #原始图片名称
to_img = "new_flower.jpg" #生成的新图片名称

def save_img(myset):
        #存储图片
    f = open("/home/tarena/MongoDB/code/" + from_img,"rb") #只读模式二进制方式打开
    data = f.read() #度文件的内容

    #将data 转换为mongodb的存储格式
    content =bson.binary.Binary(data)

    myset.insert({"filename":from_img,#文件名
                "data":content  #文件数据
                })
    print("save.ok")
    return

def get_img(myset):#从mongodb读取图片
    img = myset.find_one({"filename":"flower.jpg"})
    with open("/home/tarena/MongoDB/code/"+to_img,"wb") as f: #打开存入文件
        f.write(img["data"]) #将data域写入文件
    print("save new img ok")
    return



#连接数据库,取得数据库对象,取得集合对象
conn = MongoClient("localhost",27017)
db = conn.gridfs #取得数据库对象
myset = db.image  #取得集合对象

# save_img(myset)
get_img(myset)

conn.close()