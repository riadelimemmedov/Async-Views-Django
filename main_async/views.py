import asyncio
from time import sleep
from typing import List
from asgiref.sync import sync_to_async
import random

import httpx
from django.http import HttpResponse

#*helpers

#!http_call_async => asynchronous
async def http_call_async():
    for num in range(1,6):
        await asyncio.sleep(1)#each 1 seconds return response await with asyncio.sleep(1)
        print('Number asynchronous ', num)
    async with httpx.AsyncClient() as client:#for asynchronous requests
        r = await client.get('https://httpbin.org/')#send get request with httpx
        print(r)

#!http_call_sync => synchronous
def http_call_sync():
    for num in range(1,6):
        sleep(1)
        print('Number synchronous ', num)
    r = httpx.get('https://httpbin.org/')#for synchronous requests
    print(r)

#*views

#!index with async
async def index(request):
    return HttpResponse('Hello main_async')

#!async_view
async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse('Non-Blocking HTTP request')

#!sync_view 
def sync_view(request):
    http_call_sync()
    return HttpResponse('Blocking HTTP request')


#multiple operations asynchronously
#!smoke
async def smoke(smokables:List[str] = None,flavor:str='Sweet Baby Ray') -> List[str]:
    for smokable in smokables:
        print(f"Smoking some {smokable}")
        print(f"Appliying the {flavor}")
        print(f"{smokable.capitalize()} smoked")
    return len(smokables)

#!get_smokables
async def get_smokables():
    print('Getting smokables...')
    await asyncio.sleep(2)
    async with httpx.AsyncClient() as client:
        await client.get('https://httpbin.org/')
        print('Returning smokables')
        return [
            "ribs",
            "brisket",
            "lemon chicken",
            "salmon",
            "bison sirloin",
            "sausage",
        ]

#!get_flavor
async def get_flavor():
    print('Gettomh flavor...')
    await asyncio.sleep(1)
    async with httpx.AsyncClient() as client:
        await client.get('https://httpbin.org/')
        print('Returning flavor')
        return random.choice([
            "Sweet Baby Ray's",
            "Stubb's Original",
            "Famous Dave's",
        ])

#!smoke_some_meats
async def smoke_some_meats(request):
    results = await asyncio.gather(*[get_smokables(),get_flavor()])
    print('Results zero index ', results[0])
    print('Results first index ', results[1])
    total = await asyncio.gather(*[smoke(results[0],results[1])])
    print('Total ', total)
    return HttpResponse(f"Smoked {total[0]} meats with {results[1]}")
    

#What if you make a synchronous call inside an async view?
#!oversmoke
def oversmoke():
    sleep(5)
    print('Who does not love burnt meats')

#!burn_some_meats
async def burn_some_meats(request):
    oversmoke()
    return HttpResponse(f"Burned some meats...")

#Sync to Async =>
#!async_with_sync_view
async def async_with_sync_view(request):
    loop = asyncio.get_event_loop()#call asynchronous function
    async_function = sync_to_async(http_call_sync,thread_sensitive=False)
    loop.create_task(async_function())
    return HttpResponse('Non-blocking HTTP request (via sync_to_async)')
