from datetime import datetime



async def time_checker(func):
    start = datetime.now()

    r = await func()

    end = datetime.now()

    print(f'Задача завершилась за {end-start}')

    return r

