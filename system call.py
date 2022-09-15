import os
val = os.fork()
if val == 0:
    pid = os.getpid()
    print(f"Hi I am Child Process and my PID is {pid}.")
elif val > 0:
    pid = os.getpid()
    print(f"Hi I am Parent Process and my PID is {pid} and PID {val} is my Child Process.")
else:
    print("Sorry!! Child Process creation has failed...")
