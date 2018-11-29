#删除数据
import pymongo

conn = pymongo.MongoClient("localhost",27017)

dblist = conn.database_names()

db = "stu"
if db in dblist:
    mydb = conn["stu"]
    mycol = mydb["acct"]
    myquery = {"acct_no":"622345888","acct_name":"Max"}
    ret = mycol.delete_one(myquery)
    print("删除笔数:%d" % ret.deleted_count)
else:
    print("db not found")
conn.close()