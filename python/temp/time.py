import datetime


current_time = datetime.datetime.now()

[x for x in range(1_000_000)]

after_exec = datetime.datetime.now()

print(after_exec - current_time)
