num = int(input("ENTER A NUMBER: "))
revnum = ""
while num > 0:
    digit = num % 10
    revnum += str(digit)
    num //= 10
print("REVERSED NUMBER:", revnum)