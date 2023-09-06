dividend= int(input("add dividend: "))

divisor= int(input("add divisor: "))

try:
    ans= dividend/divisor

except  ZeroDivisionError as err:
    print("Cannot divisible by Zero.")
else:
    print(ans)