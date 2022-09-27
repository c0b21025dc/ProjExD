from random import randint

from random import choice
a = 10 #対象文字数
b = 2  #欠損文字数
c = []
a_ls = [] #対象文字
b_ls = [] #欠損文字
def syutudai(a,b):
    for i in range(a):
        a_ls.append(randint(65,90))
    for i in range(b):
        c.append(a_ls.pop(choice(a)))
        b_ls.append(c)

syutudai(a,b)
print(a_ls)
print(b_ls)