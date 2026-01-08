steps = int(input("How many steps do you want? "))
timer = open('timer.txt','w')

for num in range(1,steps + 1):
  print(num)
  timer.write(f'{num}\n')

input("Pressanything to close")
timer.close()
