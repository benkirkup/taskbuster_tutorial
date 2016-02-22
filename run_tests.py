import subprocess

subprocess.call('coverage run --source="." manage.py test', shell=True)