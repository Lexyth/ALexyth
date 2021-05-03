import os
import asyncpg

import database as db

DATABASE_URL = os.environ['DATABASE_URL']

async def connect():
  print("Database: Establishing connectionEdited")
  conn = await asyncpg.connect("postgres://ywclyhrvozzfng:8cc2e990f893d94cf12b7bdff3445dc7f6c848103d0a5ade09588f98749701cd@ec2-54-220-35-19.eu-west-1.compute.amazonaws.com:5432/da82moegjogjbh", ssl='require', timeout=10)
  print("Connected")
  return conn