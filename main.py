import time

my_time = int(input("Type in seconds: "))

for x in range(my_time, 0, -1):
  second=x%60
  minute=int(x/60)%60
  
  print(f"00:{minute: 02}:{second: 02}")

time.sleep(1)
print("Time's up!")