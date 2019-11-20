import os
from datetime  import datetime 
mod_time = os.stat('destination.loc.txt').st_mtime
print(datetime.fromtimestamp(mod_time))