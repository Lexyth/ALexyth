import os
import asyncpg

import database as db

DATABASE_URL = os.environ['DATABASE_URL']

async def _connect():
  return await asyncpg.connect(DATABASE_URL, ssl='require', timeout=20)

async def execute(query: str, *args, timeout: float = 20) -> str:
  conn = await _connect()
  result = await conn.execute(query, *args, timeout=timeout)
  await conn.close()
  return result

async def executemany(command: str, args, *, timeout: float = 20):
  conn = await _connect()
  await conn.executemany(command, args, timeout = timeout)
  await conn.close()

async def fetch(query: str, *args, timeout: float = 20, record_class: type = None) -> list:
  conn = await _connect()
  result = await conn.fetch(query, *args, timeout=timeout, record_class=record_class)
  await conn.close()
  return result
  
async def fetchrow(query: str, *args, timeout: float = 20, record_class: type = None):
  conn = await _connect()
  result = await conn.fetchrow(query, *args, timeout=timeout, record_class=record_class)
  await conn.close()
  return result

async def fetchval(query: str, *args, column: int = 0, timeout: float = 20):
  conn = await _connect()
  result = await conn.fetchval(query, *args, column=column, timeout=timeout)
  await conn.close()