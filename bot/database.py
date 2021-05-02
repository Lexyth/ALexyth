import os
import asyncpg

import database as db

DATABASE_URL = os.environ['DATABASE_URL']

async def connect():
  return await asyncpg.connect(DATABASE_URL, ssl='require')