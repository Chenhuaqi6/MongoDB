#insert.py
#mongodb 的插入操作

import pymongo

#1.建立连接
conn = pymongo.MongoClient("localhost",27017)

#2.列出所有数据库
dblist = conn.database_names()
db = "stu"

if db in dblist:
    mydb = conn["stu"] #获取数据库对象
    mycol = mydb["acct"] #获取集合对象
    #定义插入的内容
    mydict = [
        {"acct_no":"622345777","acct_name":"Kevin"},
        {"acct_no":"622345666","acct_name":"Emma"},
        {"acct_no":"622345888","acct_name":"Max"}

    ]
    ret = mycol.insert_many(mydict)
    print(ret.inserted_ids) #打印新插入的id号
else:
    print("db not find")
conn.close()