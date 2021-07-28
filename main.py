import hcskr
import os
import time

name = os.environ.get('NAME')
birth = os.environ.get('BIRTH')
region = os.environ.get('REGION')
school = os.environ.get('SCHOOL')
school_level = os.environ.get('SCHOOL_LEVEL')
password = os.environ.get('PASSWORD')

data = hcskr.selfcheck(name,birth,region,school,school_level,password)
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
linelol = "-------------------"

print(linelol)
print(now)
print(data['code'])
print(data['message'])
print(linelol)