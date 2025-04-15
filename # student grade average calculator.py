# student grade average calculator

math = float(input("math grade: "))
science = float(input("science grade: "))
english = float(input("english grade: "))
turkish = float(input("turkish grade: "))
 
avarage = (math + science + english + turkish) / 4

if avarage >= 50:
    print(f"avarage: {avarage} you passed!")
else :
    print(f"avarage: {avarage} you failed!")