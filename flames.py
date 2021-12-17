def red(msg):
    return "{}{}{}".format('\033[91m', msg, '\033[0m')

def remove(string):
	return string.replace(" ", "")

print(red("❤️  Welcome to Flame Game ❤️"))

name_1=input("enter the first name : ")
name_2=input("enter the second name : ")

name_one=list(remove(name_1))
name_two=list(remove(name_2))

for n1 in name_one:
    for n in name_two:
        if n1==n:
            name_one.remove(n1)
            name_two.remove(n1)

remaning_letters=[]

for i in name_one: 
    remaning_letters.append(i)

for i in name_two:
    remaning_letters.append(i)
	
flame = ["Friend", "Love", "Affection", "Marriage", "Enemy"]

relationship =flame[int(len(remaning_letters)/int(len(flame))-1)]

if relationship == "Enemy":
    relationship ="are Enemies"
if relationship == "Affection":
    relationship ="are Affection"
if relationship == "Marriage":
    relationship ="are Married"
if relationship == "Love":
    relationship ="are in Love"
if relationship == "Friend":
    relationship ="are Friends"

print(red(f"{name_1} and {name_2} are {relationship}"))


