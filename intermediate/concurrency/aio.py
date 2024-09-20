import asyncio
import time

# Coroutine - Returns Coroutine Object
async def brewCoffee():
    print("Start brewCoffee")
    await asyncio.sleep(3)
    print("End brewCoffee")
    return "Coffee ready"

async def toastBagel():
    print("Start toastBagel")
    await asyncio.sleep(2)
    print("End toastBagel")
    return "Bagel toasted"

async def main():
    start_time = time.time()

    # Synchronous
    # result_coffee = brewCoffee()
    # result_bagel = toastBagel()

    # Asynchronous
    # Returns Future Aggregating Results From Given Coroutines/Futures
    # batch = asyncio.gather(brewCoffee(), toastBagel())
    # result_coffee, result_bagel = await batch

    # Schedule Execution Of Coroutine Object In A Spawn Task
    coffee_task = asyncio.create_task(brewCoffee())
    toast_task = asyncio.create_task(toastBagel())
    result_coffee = await coffee_task
    result_bagel = await toast_task

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Result of brewCoffee: {result_coffee}")
    print(f"Result of toastBagel: {result_bagel}")
    print(f"Total execution time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())