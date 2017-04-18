#users = ['admin', 'john', 'alice', 'mark', 'robert']
current_users = ['admin', 'frank', 'maria', 'milana']
new_users = ['MarIa', 'john', 'obama', 'vladimir']

#if users:
#    for user in users:
#        if user == 'admin':
#            print("Hello admin, would you like to see a status report?")
#        else:
#            print("Hello " + user.title() + ", thank you for logging in again.")
#else:
#    print("We need to find some users!")

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Unavailable name " + new_user.title() + ". Please, select a new name.")
    else:
        print("Correct name " + new_user.title())
