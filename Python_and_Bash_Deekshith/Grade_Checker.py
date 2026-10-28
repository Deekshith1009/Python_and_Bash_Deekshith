std=int(input("Enter Score: "))
if std >= 90:
    print("A Grade")
elif std >= 80:
    print("B Grade")
elif std >= 70:
    print("C Grade")
elif std >= 60:
    print("D Grade")
elif std < 60:
    print("F Grade")
else:
    print("Give a Valid Number")