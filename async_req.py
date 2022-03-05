import ssl
from flask import session
import requests
import asyncio
import aiohttp
import time

api_key = "WULE790DY5WDI0VC"
url =  'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL','MSFT','TSLA','GOOG','PEP','AAPL','MSFT','TSLA','GOOG','PEP','AAPL','MSFT','TSLA','GOOG','PEP','AAPL','MSFT','TSLA','GOOG','PEP','AAPL','MSFT','TSLA','GOOG','PEP','AAPL','MSFT','TSLA','GOOG','PEP','AAPL','MSFT','TSLA','GOOG','PEP']
results = []
start_time = time.time()


async def get_symbols():
    async with aiohttp.ClientSession() as session:    
        for symbol in symbols:
            print(symbol)
            resp = await session.get(url.format(symbol,api_key),ssl=False)
            results.append(await resp.json())


# loop = asyncio.get_event_loop()
# loop.run_until_complete(get_symbols())
# loop.close()
asyncio.run(get_symbols())
print("time in seconds for {} api calls",len(results),(time.time() - start_time))