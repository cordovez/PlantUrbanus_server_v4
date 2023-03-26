# thank you chatGPT
import json
import aiohttp
""" This is a script to upload data from a json document to an API endpoint
in order to add many documents to a database collection"""


async def send_aroids():
    async with aiohttp.ClientSession() as session:
        with open('aroids_list.json', 'r') as f:
            data = json.load(f)
        response = await session.post('http://127.0.0.1:8000/aroids/add_many', json=data)
        return response.status

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_aroids())
