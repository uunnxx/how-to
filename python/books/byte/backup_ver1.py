import os
import time


source = ['/home/baka/test_backup', '/home/baka/test_backup2']


target_dir = '/home/baka/backup_dest'
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = f'zip -qr {target} {' '.join(source)}'


if os.system(zip_command) == 0:
    print('Everything is good: ', target)
else:
    print('Something went wrong')
