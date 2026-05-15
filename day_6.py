#1
"""
i = 0
for x in range(0, 4, 1):
    for i in range(0, 4, 1):
        if(x == i):
            print("*"*i,end = ' ')
    print("\n")
"""


#2
"""
i = 0
for x in range(4 , 0, -1):
    for i in range(4, 0, -1):
        if(x == i):
            print("*"*x,end = ' ')
    print("\n")
"""

#3
"""
i = 0
for x in range(0 , 4 ,1 ):
    for i in range(4-x , 0, -1):
        print(" ",end = ' ')
    for i in range(x, 0, -1):
        print("*",end = ' ')
    print("\n")
for x in range(0 , 4 ,1 ):
    for i in range(x , 0, -1):
        print(" ",end = ' ')
    for i in range(4-x, 0, -1):
        print("*",end = ' ')
    print("\n")
"""
#리스트로 반복문 찍기
"""
stars = [1,2,3,4] #0~3

for j in stars[0:3]:
    print('*'*stars[j])
for k in stars[-3::-1]:#stars[0:4] stars[-3::-1]
    print('*'*stars[k])
"""

# nums = [1,2,3,4,5]

# for n in nums:
#     spaces = 10 - n + 1
#     print(" "* spaces+ "*" * n)
#==========================
# nums = [1,2,3,4,5]

# pattern = nums + nums[-2::-1]
# print(pattern)

# for n in pattern:
#     spaces = 10 - n + 1
#     print(" "* spaces+ "*" * n)