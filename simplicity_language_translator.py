import os
chars = {
    "@":"A", ";":"B", "'":"C", "$":"D", "3":"E", "_":"F", "&":"G", 
    "-":"H", "8":"I", "+":"J", "(":"K", ")":"L", "?":"M", "!":"N",
    "9":"O", "0":"P", "1":"Q", "4":"R", "#":"S", "5":"T", "7":"U",
    ":":"v", "2":"W", '"':'X', "6":"Y", "*":"Z", "•":" ", "~":"1", 
    "`":"2", "|":"3", "¥":"4", "√":"5", "π":"6", "÷":"7", "×":"8", 
    "¶":"9", "∆":"0"
    }

user_input = str(input())

count = 0
st = ""

for x in user_input:
    if count == 0:
        st += str(chars[x]).upper()
        count += 1
        continue

    st += str(chars[x]).lower()

print(st)

os.system("pause")
