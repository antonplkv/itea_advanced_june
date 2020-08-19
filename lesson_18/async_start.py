import asyncio


async def useful_action(seconds):
    print(f'Sleep for {seconds} seconds')
    await asyncio.sleep(seconds)
    print('woken up')
    return seconds


async def main():
    tasks = []
    tasks.append(asyncio.create_task(useful_action(3)))
    tasks.append(asyncio.create_task(useful_action(5)))
    tasks.append(asyncio.create_task(useful_action(2)))
    tasks.append(asyncio.create_task(useful_action(3)))

    for result in asyncio.as_completed(tasks):
        print(await result)


asyncio.run(main())