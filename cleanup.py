with open('.\\sources\\yaman1.txt', 'r') as file:
    data = file.read().replace("\n","").replace("; ","")

n1 = data.replace(",N", "N0").replace(",D", "D0").replace("S'", "S2").replace("S;", "S2 ").replace("-", " ")
# print(n1)

n2 = ""
for i in range(len(n1)-1):
    if n1[i].isalpha() and n1[i+1] == " ":
        n2 = n2 + n1[i] + "1 "
    else:
        n2 = n2 + n1[i]

n2 = n2.replace(";N0","N0").split(" ")
# print(n2)
n3 = []
for i in n2:
    if i!= '':
        print(i)
        n3.append(i)
print(set(n3))

with open("yaman1format.txt", "w") as text_file:
    for i in n3:
        text_file.write(i + " ")

with open('yaman2.txt', 'r') as file:
    data = file.read().replace("\n","").replace("; ","")

n1 = data.replace("!"," ").replace(",", " ")
print(n1)



with open("yaman1format.txt", "w") as text_file:
    for i in n3:
        text_file.write(i + " ")

