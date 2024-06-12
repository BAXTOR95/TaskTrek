import aiohttp
import asyncio
import os

# Ensure you have your Unsplash access key stored in an environment variable
UNSPLASH_ACCESS_KEY = os.getenv('UNSPLASH_ACCESS_KEY')


async def fetch_unsplash_image(session, query):
    """
    Asynchronously fetch a random image from Unsplash based on a query.

    Args:
        session (aiohttp.ClientSession): The HTTP client session.
        query (str): The search query for fetching the image.

    Returns:
        dict: The JSON response from the Unsplash API containing the image details.
    """
    url = 'https://api.unsplash.com/photos/random'
    params = {'query': query, 'orientation': 'landscape', 'count': 1}
    headers = {'Authorization': f'Client-ID {UNSPLASH_ACCESS_KEY}'}

    async with session.get(url, params=params, headers=headers) as response:
        json_response = await response.json()
        if json_response and isinstance(json_response, list) and len(json_response) > 0:
            return json_response[0]['urls']['regular']
        return None


def fetch_random_image(query=None):
    """
    Synchronously fetch a random image by running the asynchronous fetch function.

    Args:
        query (str, optional): The query for the image to fetch.

    Returns:
        dict: The combined response containing activity and image details.
    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    async def main():
        async with aiohttp.ClientSession() as session:
            return await fetch_unsplash_image(session, query)

    return loop.run_until_complete(main())
