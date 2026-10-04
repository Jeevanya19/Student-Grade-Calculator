m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))
m4 = int(input("Enter marks for subject 4: "))
m5 = int(input("Enter marks for subject 5: "))

if 0 <= m1 <= 100 and 0 <= m2 <= 100 and 0 <= m3 <= 100 and 0 <= m4 <= 100 and 0 <= m5 <= 100:

    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    print("\n----- STUDENT RESULT -----")
    print("Total Marks:", total)
    print("Percentage:", percentage, "%")
    print("Grade:", grade)

else:
    print("Invalid marks! Enter marks between 0 and 100.")

 
