import os
import time


source = ['/home/baka/test_backup', '/home/baka/test_backup2']


target_dir = '/home/baka/backup_dest'

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input('Type your comment: ')

if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Directory is created', today)


zip_command = f'zip -qr {target} {' '.join(source)}'


if os.system(zip_command) == 0:
    print('Everything is good: ', target)
else:
    print('Something went wrong')
