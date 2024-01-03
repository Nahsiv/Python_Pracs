import asyncio
import aiohttp
import time

async def fetchFromGoogle():
    url = 'https://www.google.com'
    session = aiohttp.ClientSession()
    response = await session.get(url)
    async with open('ter.txt', 'w') as f:
        f.write(await response.content.read(256))
    await session.close()
async def main():
    print(time.strftime('%X'))
    # await asyncio.gather(
    # *[fetchFromGoogle() for _ in range(20)]
    # )
    await fetchFromGoogle()
    print(time.strftime('%X'))
if __name__ == '__main__':
    asyncio.run(main())