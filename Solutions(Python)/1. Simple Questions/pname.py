user = input('Please Enter your name \n')
# print(type(user))
names = user.split()#make strings to list
# print(names)
for i in range(0, len(names)):
    if i < len(names) - 1:
        # print first char only, no newline at the end
        print(names[i][0].upper()+'.', end=" ") 
    else:
        # print entire last name
        print(names[i].title()) # print entire name