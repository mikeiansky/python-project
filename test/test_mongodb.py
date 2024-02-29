"""
测试 mongodb 数据库
"""


import pymongo
from config import config

def get_connection():
    client = pymongo.MongoClient(host=config.MONGO_HOST,
                                 port=config.MONGO_PORT,
                                 username=config.MONGO_USER,
                                 password=config.MONGO_PWD,
                                 authSource=config.MONGO_DB)
    return client

def insert():
    client = get_connection()
    # 选择一个数据库
    db = client["test"]

    # 获取一个集合（类似于表）
    collection = db["people"]

    tag = '003'
    # 插入一条数据
    data = {"name": f"John-{tag}", "address": f"Highway 37-{tag}"}
    insert_result = collection.insert_one(data)
    print(insert_result)
