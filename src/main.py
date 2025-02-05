#this is the folder that creates another to display date and time
from datetime import datetime

# saving the current date and time
now = datetime.datetime.now()

dateTime = now. strftime("%Y-%m-%d %H:%M:%S:")

with open("version.md", "w") as f:
    f.write(dateTime)
