import os
from fatsecret import Fatsecret
from dotenv import load_dotenv

load_dotenv()

FS_KEY = os.getenv('FATSECRET_KEY')
FS_SECRET = os.getenv('FATSECRET_SECRET')

# fs = Fatsecret(FS_KEY, FS_SECRET)

print("key %s sec: %s" % (FS_KEY, FS_SECRET))