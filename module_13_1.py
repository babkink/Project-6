import asyncio

async def strong_man(name, power):
    print(f'Strong man {name} started tournament')
    for ball_number in range(1, 6):
        await asyncio.sleep(5 / power)
        print(f'Strong man {name} lifted ball number {ball_number}!')
    print(f'Strong mand {name} finushed tournament!!!')

async def start_tournament():
    task_1 = asyncio.create_task(strong_man('Bob', 5))
    task_2 = asyncio.create_task(strong_man('Mel', 3))
    task_3 = asyncio.create_task(strong_man('Wal', 1))
    await task_1
    await task_2
    await task_3

asyncio.run(start_tournament())