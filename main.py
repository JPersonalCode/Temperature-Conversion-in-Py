# Globals 
user_temp = ""
temp_key=""
temp_int = 0

# Functions
def validatetemp(string):
    for x in string:
        if not x.isdigit():
            raise Exception("Please enter a number for the Temp")

def validatekey(String):
    if String != "C" and String != "F":
        raise Exception

def convert_F2C(Int):
    Int = (Int - 32) * 5/9
    return Int

def convert_C2F(Int):
    Int = (Int *9/5) + 32
    return Int


# Call Stack 
user_temp = input("Please input Tempreture to Convert: ")
validatetemp(user_temp)
temp_key = input("Please enter F or C to convert to that scale: ") 
validatekey(temp_key)
temp_int = int(user_temp)
if temp_key == "C":
    print(str(convert_F2C(temp_int))+"C")
elif temp_key == "F":
    print(str(convert_C2F(temp_int))+"F")

    

