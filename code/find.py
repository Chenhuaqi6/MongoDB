#查询
import pymongo

#1.连接数据库
conn = pymongo.MongoClient("localhost",27017)

#2.列出所有数据库
dblist = conn.database_names()

db = "stu"
#判断库是否存在
if db in dblist:
    #3.获取数据库对象
    mydb = conn["stu"]
    mycol = mydb["acct"] #选择集合
    #查询打印
    # docs = mycol.find({},{"_id":0})
    docs = mycol.find({"acct_no":"622345111111"},{"_id":0})
    for dos in docs:
        print(dos)
else:
    print("not found collection",db)
conn.close()