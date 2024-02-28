"""
测试 mongodb 数据库
"""


import pymongo

# 连接到 MongoDB
client = pymongo.MongoClient("mongodb://172.16.2.249:27017/")

# 选择一个数据库
db = client["ciwei"]


# 获取一个集合（类似于表）
collection = db["employee"]

# 插入一条数据
data = {"name": "John", "address": "Highway 37"}
insert_result = collection.insert_one(data)

print(insert_result.inserted_id)  # 打印插入的文档 ID
