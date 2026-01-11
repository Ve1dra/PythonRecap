def Calc():
    scores: list[int] = []
    grades: list[int] = []

    c = int(input("How many courses are you offering? "))
    print("Enter 'scores' to input your score and grade ")
    ent = str(input())
    for i in range (c):
        if ent == 'scores'.lower():
            try :
                s = int(input("Enter your grade "))
                g = int(input("Enter your course unit "))
                scores.append(s)
                grades.append(g)
            except ValueError:
                print("Invalid input")

    total_s = 0
    total_g = 0

    for score, unit in zip(scores, grades):
        total_s += score * unit
        total_g += unit

    print("Total score:", total_s)
    print("Total units:", total_g)
    if total_g > 0 :
        print("CGPA:", total_s/total_g)
    else:
        print("No valid courses entered.")
d = Calc()