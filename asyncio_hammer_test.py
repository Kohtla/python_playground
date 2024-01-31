import asyncio
import aiohttp


async def send_request(url, responses):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response is not None:
                responses.append(response)


async def requests_producer(
    tasks: list,
    responses,
    created_queue: asyncio.Queue,
    completed_queue: asyncio.Queue,
    url,
    batch_size,
):
    print("Producer launched")
    while True:
        tasks.extend([send_request(url, responses) for _ in range(batch_size)])
        # print("Tasks added")
        await created_queue.put(None)
        await completed_queue.get()
        # print("Tasks completed")
        tasks.clear()


async def requests_runner(
    tasks, created_queue: asyncio.Queue, completed_queue: asyncio.Queue
):
    print("Runner launched")
    while True:
        await created_queue.get()
        await wait_for_tasks_execution(tasks, completed_queue)


async def wait_for_tasks_execution(tasks, completed_queue):
    async with asyncio.TaskGroup() as tg:
        background_tasks = set()
        for task in tasks:
            background_tasks.add(tg.create_task(task))
    await completed_queue.put(None)


async def counter(responses: list):
    while True:
        await asyncio.sleep(1)
        print(f"{len(responses)} requests done")
        responses.clear()


async def main():
    url_to_bomb = "http://localhost:8888/polls"
    batch_size = 100

    responses = []
    tasks = []
    tasks_created_queue = asyncio.Queue()
    completed_queue = asyncio.Queue()

    consumer = asyncio.create_task(counter(responses))
    runner = asyncio.create_task(
        requests_runner(tasks, tasks_created_queue, completed_queue)
    )
    producer = asyncio.create_task(
        requests_producer(
            tasks,
            responses,
            tasks_created_queue,
            completed_queue,
            url_to_bomb,
            batch_size,
        )
    )
    await consumer
    await runner
    await producer


if __name__ == "__main__":
    asyncio.run(main())
