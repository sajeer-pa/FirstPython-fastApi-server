import os
from motor.motor_asyncio import AsyncIOMotorClient

class MongoDB:
    def __init__(self):
        self.client = None
        self.db = None

    async def connect(self):
        self.client = AsyncIOMotorClient(os.environ['DATABASE_URL'])
        self.db = self.client.my_database  # Replace 'testdb' with your database name

    async def close(self):
        self.client.close()

# Create an instance of MongoDB
mongodb = MongoDB()