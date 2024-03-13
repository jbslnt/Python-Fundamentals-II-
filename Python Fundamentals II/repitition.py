# Repitition Statements
# Data types allowed to be iterated: Lists, Ranges, Sets, Tuple, Dictionaries, Strings

# x = range(5, 11)
# petName = ["snowy", "blacky", "bruno"]

# for loop
# for(inititialzation;condition;incrementation/decre) - JAVA
# for  num in x:
#     print(num)

# Slicing a lists
# for name in petName[0:2:-1]:
#     print(name)

# Looping Dictionaries
# key : value
    
# user = {
#     "first_name" : "Johhny",
#     "last_name" : "Tadea",
#     "age" : 25, 
#     "average" : 81.76, 
#     "list_subjects" : ["Programming", "Mathematics", "English"]
# }

# for key in user:
#     print(key, ":", user[key])

# Looping list of dictionaries
list_of_users = [
    
    {
    "first_name" : "Johhny",
    "last_name" : "Tadea",
    "age" : 25, 
     "average" : 81.76, 
     "list_subjects" : ["Programming", "Mathematics", "English"]
},
{
    "first_name" : "Rose",
    "last_name" : "Tadea",
    "age" : 23, 
    "average" : 82.54, 
    "list_subjects" : ["Programming", "Mathematics", "English"]
},
{
    "first_name" : "Angel",
    "last_name" : "Tadea",
    "age" : 23, 
    "average" : 81.76, 
    "list_subjects" : ["Programming", "Mathematics", "English"]
},
    ] 

for key in list_of_users:
    for x in key:
        print(x, ":", key[x])

# looping in reverse
x = range(1, 10)
for i in x[::-1]:
    print(i)