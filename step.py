steps = int(input("How many steps do you want? "))
with open('timer.txt','w') as outfile:

  for num in range(1,steps + 1):
    print(num)
    timer.write(f'{num}\n')

  for lines in timer:
    print(lines)

input("Pressanything to close")
