import asyncio


async def countdown(n):
    for timer in range(n,0,-1):
        print(timer)
        await asyncio.sleep(1)


async def main():
    await countdown(3)



# Run the program
asyncio.run(main())

