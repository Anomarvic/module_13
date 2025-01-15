import time
import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')

    for ball in range(1, 6):
        slp = 1 / power
        await asyncio.sleep(slp)
        print(f'Силач {name} поднял {ball} шар')

    print(f'Силач {name} закончил соревнования.')


async def tournament():
    participants = [
        ('Pasha', 3),
        ('Denis', 4),
        ('Apollon', 5),
    ]

    tasks = [start_strongman(name, power) for name, power in participants]

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(tournament())