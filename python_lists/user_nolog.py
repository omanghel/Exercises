'''
Problem:
We have login data with the following information:
* used_id
* date: seven consecutive days: 1,2...7
* login: if a user logs into our software on that date: 1 mean yes, 0 means no
We can assume that the data is complete, ordered by used_id and date and there are no duplicates

Compute the maximum number of consecutive days (max_no_login) that each user doesn't log in, return results in a dictionary.

Example:
login_data = {'user_id':[1,1,1,1,1,1,1,2,2,2,2,2,2,2],
'date':[1,2,3,4,5,6,7,1,2,3,4,5,6,7],
'login': [1,1,0,0,0,0,1,0,0,0,1,0,1,0]}
Expected results:
{'user_id':[1,2],
'max_no_login':[4,3]}
'''

def count_no_login(login_data):
    users = login_data['user_id']
    us = 0
    max_nonlog = []
    user_nolog = []
    for i in range(len(users)):
        if users[i] != us or i==len(users)-1:
            us  = login_data['user_id'][i]
            if i > 0:
                max_nonlog.append(max_count)
                user_nolog.append(users[i-1])
            max_count = 0
            counter = 0
        if int(login_data['login'][i]) == 0:
            counter += 1
        else:
            if max_count < counter:
                max_count = counter
            counter = 0
    list_nolog = {'user_id':user_nolog,'max_no_login':max_nonlog}
    return list_nolog

if __name__== '__main__':
    login_data = {'user_id':[1,1,1,1,1,1,1,2,2,2,2,2,2,2],
    'date':[1,2,3,4,5,6,7,1,2,3,4,5,6,7],
    'login':[1,1,0,0,0,0,1,0,0,0,1,0,1,0]}
    print(count_no_login(login_data))
