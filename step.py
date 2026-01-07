steps = int(input("How many steps do you want? "))
timer = open('timer.txt','w')

for num in range(1,steps + 1):
  count = count + 1
  timer.write(f'{count}\n')
