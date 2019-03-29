import os
import time

source = ['~/Documents/notes_backup']
target_dir = '/home/malala/Documents/notes_backup_target'

target = target_dir + os.sep + 'backup_' + time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
	os.mkdir(target_dir)

zip_command = "zip -r {0} {1}".format(target,' '.join(source))

print("Zip command is:")
print(zip_command)
print ("Running:")
if os.system(zip_command) == 0:
	print ('Successful backup to', target)
else:
	print ('Backup FAILED')