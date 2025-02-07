pw = '12345'
lg = 'durov'
checklg = input('Login: ')
checkpw = input('Password: ')
if (checklg == lg) and (checkpw == pw):
    pw = input('New password: ')
    print(f'User {lg} has changed the password to {pw}')
else:
    print('Login or password is not correct!')