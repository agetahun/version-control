#this is the folder that creates another to display date and time
s = ["import datetime\n", "print(datetime.datetime.now())\n"]


with open("version.md", "w") as f:
    f.writelines(s)
