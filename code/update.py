#修改数据
import pymongo

#连接数据库
conn = pymongo.MongoClient("localhost",27017)

#列出所有数据库
dblist = conn.database_names()
db = "stu" #操作的数据库
if db in dblist:
    mydb = conn["stu"]
    mycol = mydb["acct"]
    #修改
    myquery = {"acct_no":"622345111111"}
    new_values = {"$set":{"balanc":99.99}}
    ret = mycol.update_one(myquery,new_values,False,False)
    print("修改笔数:%d"%ret.modified_count)
else:

    print("db not found")
conn.close()