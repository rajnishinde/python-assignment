q1 = """ Question 1
a.ans 1
b.ans 2
c. ans 3
d. ans 4
"""
q2 = """ Question 2
a.ans 1
b.ans 2
c. ans 3
d. ans 4
"""
q3 = """ Question 3
a.ans 1
b.ans 2
c. ans 3
d. ans 4
"""

question = {q1: "a", q2: "a", q3: "a"}
name = input("Enter your name : ")
print("hello",name,"welcome to the quiz game")
score = 0
# j = 1
# q_n = "Q" + str(j)
# print(q_n +" "+ i)

for i in question:
    print(i)
    skip = input("Do you want to skip this question(y/n)? : ")
    if skip.lower() == "y":
        continue
    ans = input("enter the answer(a/b/c/d) : ")
    if ans.lower() == question[i]:
        print("correct answer,you got 1 point")
        score = score + 1
    else:
        print("wrong answer, you loose the game ")
    quit_gm = input("Do you wnat to quit (y/n) : ")
    if quit_gm.lower() == "y":
        break

print("final score : ", score)

