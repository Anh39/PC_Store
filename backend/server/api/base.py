from backend.common import folder_path,common
import aiohttp

class BaseDBAPI:
    def __init__(self) -> None:
        self.base_url = common.get_url(common.get_config('database'))
        self.session : aiohttp.ClientSession = None
    def start(self) :
        self.session = aiohttp.ClientSession(self.base_url)
    async def stop(self) :
        await self.session.close()
        self.session = None