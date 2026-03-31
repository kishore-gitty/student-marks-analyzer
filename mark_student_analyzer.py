loop=int(input("enter count of students:"))
b={}
n=1
highest_mark=int(input("enter mark conducted for exam?:"))
good_student=None
bad_student=None
for i in range(loop):
    student=input("enter student name:")
    mark=int(input(f"enter mark of {student}:"))
    while mark > highest_mark:
        print(f"please enter a valid mark warning:{mark} should not greater that {highest_mark}")
        mark=int(input(f"enter mark of {student}:"))
    b.update({student:mark})
print("the students and marks are listed below")
g_mark=max(b.values())
b_mark=min(b.values())
for i in b:
    print(n,".",i,b[i])
    n+=1
for i,j in b.items():
    if j==g_mark:
        good_student=i
    if j==b_mark:
        bad_student=i
print(f"from the above list we can blindly say that {good_student} got {g_mark} which is highest mark ")
print(f"{bad_student} got {b_mark} which is low mark ")
permission_perc=input("you need to get percentage for everyone(Y/N):")
if permission_perc == "Y":
    perc_list={}
    for i,j in b.items():
        perc=(j/highest_mark)*100
        perc_list.update({i:perc})
    n=1
    for i in perc_list:
        print(n,".",i,perc_list[i],"%")
        n+=1
elif permission_perc == "N":
    print("THANK YOU FOR USING THIS SOFTWARE")

        
