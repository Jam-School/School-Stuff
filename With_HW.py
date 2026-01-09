steps = int(input("How many steps do you want? "))
with open('timer.txt','w') as outfile, open('log.txt','w') as log:

  for num in range(1,steps + 1):
    print(num)
    outfile.write(f'{num}\n')
  outfile.close()
  outfile = open('timer.txt','r')
  for lines in outfile:
    print(lines)
    log.write(f'{lines}\n')

input("Pressanything to close")

