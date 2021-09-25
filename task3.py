import turtle as tl

Numbers = [0]*10

with open('text_for_task3.txt') as file:
    for i, line in enumerate(file):
        Numbers[i] = line.split(' ')

index = input()

#for i in range(9):
#    print(Numbers[0][i])


for i, num in enumerate(index):
    for j, coords in enumerate(Numbers[int(num)]):
        if (j*2+1>=len(Numbers[int(num)])):
            break
        if (j==0): 
            tl.penup()
        else: 
            tl.pendown()
        tl.goto(int(Numbers[int(num)][j*2])+25*i, int(Numbers[int(num)][j*2+1]))
