import termcolor
students = {}
successs = []
losers = []
quastion = "y"
while quastion == "y":
    s_name = input("enter student name :")
    s_average = input("enter [his/her] average :")
    try:
        s_average = float(s_average)
    except :
        print("enter a valide value!")
        continue
    students[s_name] = s_average 
    Q = False
    while Q == False:
        quastion = input("you want to write more student [y/n] :").lower()
        if quastion == "y" or quastion == "n":
            Q = True
        else:
            print("pleas enter just [y/n]!")

for student in students:
    A =  students.get(student)
    if A < 10:
        c = (student, A)
        losers.append(c)
    else:
        B = (student, A)
        successs.append(B)

print("pass ✅ :")
for i,losser in enumerate(losers, 1):
    print(f"{i:2d}. {losser[0]}" + " " + f"{termcolor.colored(losser[1], "red")}")
print("fail ❌ :")
for i,success in enumerate(successs, 1):
    print(f"{i:2d}. {success[0]}" + " " + f"{termcolor.colored(success[1], "green")}")
