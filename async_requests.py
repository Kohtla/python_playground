import asyncio, requests, time
from main import timer


async def make_request(loop, url):
    future = loop.run_in_executor(None, requests.get, url)
    response = await future
    return response.status_code


async def make_requests(number):
    loop = asyncio.get_event_loop()
    results = {}
    url = "https://www.google.com"

    tasks = [make_request(loop, url) for _ in range(number)]

    req_results = await asyncio.gather(*tasks)

    for result in req_results:
        if results.get(result, None) is None:
            results[result] = 1
        else:
            results[result] += 1
    print(results)
    return results


if __name__ == "__main__":
    start = time.time()
    asyncio.run(make_requests(100))
    print(time.time() - start)
