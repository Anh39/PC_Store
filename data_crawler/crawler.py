from data_crawler.hacom_crawler import Handler as Hacom
import asyncio,json

async def main():
    test = Hacom()
    await test.init()
    await test.process()
    
    await asyncio.sleep(1)
    
    await test.close()
    
asyncio.run(main())