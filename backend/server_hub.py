from backend.server.server import FastAPIServer
from backend.database.server import DatabaseServer
import asyncio

def start():
    fast_api_server = FastAPIServer()
    database_server = DatabaseServer()
    loop = asyncio.get_event_loop()
    loop.create_task(fast_api_server.async_start())
    loop.create_task(database_server.async_start())
    loop.run_forever()

