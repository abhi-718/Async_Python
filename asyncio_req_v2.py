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


def get_tasks(session):
    tasks = []
    for symbol in symbols:
        tasks.append(session.get(url.format(symbol,api_key),ssl=False))
    
    return tasks

async def get_symbols():
    async with aiohttp.ClientSession() as session:    
        tasks = get_tasks(session)
        resps = await asyncio.gather(*tasks)
        for resp in resps:
            results.append(await resp.json()) 


asyncio.get_event_loop().run_until_complete(get_symbols())

#asyncio.run(get_symbols())
print("time in seconds for {} api calls",len(results),(time.time() - start_time))