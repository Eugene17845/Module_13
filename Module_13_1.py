import asyncio
import time

async def start_strongman(name, power):
        print(f'Силач {name} начал соревнования.')
        num = 1
        while num <= 5:
            await asyncio.sleep(num/power)
            print(f'Силач {name} поднял {num}')
            num += 1
        print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3
asyncio.run(start_tournament())
