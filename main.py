from tokenize import Double
import python as py
import subprocess
import os

print("do you want compiler optimization? (y/n)")
str = input()

if(str == 'y'):
    os.system("g++ -O3 cplusplus.cc -o cplusplus")
else:
    os.system("g++ cplusplus.cc -o cplusplus")

pythonTime = py.runtime()
temp= subprocess.Popen(["./cplusplus"], stdout = subprocess.PIPE)

while True:
  line = temp.stdout.readline()
  if not line:
    break
  #the real code does filtering here
  print( "\nCPP time:", line.rstrip())

pythonTime*=1000000


print(f"\nPython runtime: {pythonTime} microseconds") 
