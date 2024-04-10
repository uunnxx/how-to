async def search():
    text = input('What keyword to you want to look for? ').strip().lower()

    async with TaskGroup() as tg:
        tp = tg.create_task(search_podcast(text, 'search.talkpython.fm'))
        pb = tg.create_task(search_podcast(text, 'search.pythonbytes.fm'))


    all_results = tp.result() + pb.result()
