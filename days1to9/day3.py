import datetime
import re
start = datetime.datetime.now()
count = 0
x = open("text/day3.txt")
for line in x:
    match = re.search(r'mul\((\d+),(\d+)$',line)
    if match:
        numbers = [int(a) for a in match.groups()]
        count += numbers[0]*numbers[1]
print(count)
print()
print("Time: "+ str(datetime.datetime.now() - start))

start = datetime.datetime.now()
f = open("text/day3.txt")
text = f.read()
#text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5)))"
list = ["0","1","2","3","4","5","6","7","8","9",",","(",")","'","d","l","m","n","o","t","u"]
for char in text:
    if not char in list:
        x = text.replace(char,"!")
        text = x



y = x.split("don't")

z=[]
z.append(y[0])
for i in range(1,len(y)):
    if y[i].count("do") > 0:
        x = y[i].split("do")
        for j in range(1,len(x)):
            z.append(x[j])

b = z

h = []
for i in range(0,len(b)):
    x = b[i].split(")")
    h.append(x)


f = []
for i in range(0,len(h)):
    for j in range(0,len(h[i])):
        if len(h[i][j]) > 2:
            if h[i][j][len(h[i][j])-1].isdigit() == True:
                f.append(h[i][j])

y = f

z = []
i = 0
while i < len(y):
    if y[i].count("mul(") > 0:
        x = y[i].rsplit("mul(")
        z.append(x)
    i+=1
    
w = []
i = 0
while i < len(z):
    j = 0
    while j < len(z[i]):
        if len(z[i][j]) > 2:
            k = 0
            while k < len(z[i][j]) - 2:
                if z[i][j][k].isdigit() == True and z[i][j][k+1] == "," and z[i][j][k+2].isdigit() == True:
                    x = z[i][j].rsplit(",")
                    w.append(x)
                    k = len(z[i][j])
                else:
                    k+=1
        j+=1
    i+=1

 
i = 0
count = 0
count1 = 0
while i < len(w):
    if len(w[i]) == 2:
        if w[i][0].isdigit() == True and w[i][1].isdigit() == True:
            x = int(w[i][0]) * int(w[i][1])
            count+=x
            count1+=1
    i+=1

print()
print(count)
print()
print("Time: "+ str(datetime.datetime.now() - start))