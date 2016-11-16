# 8_vk_friends_online
This script finds who is online in vkontakte social network. It returns list of your friends, which are on the site now.
## launching
Type following command in console to launch script:`vk_friends_online.py`  
After this you will be prompted to enter your login and password.
## why I wrote it like this or twoo ways of writting this script.
There are two ways of getting online friends by VK API. The first way is to call get.friends.getOnline() for getting friends ids and then pass it to get.users() method which give us info from user id.    
   def get_friends_online_list(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope="friends"
    )
    api = vk.API(session)
    online_friends_ids = api.friends.getOnline()
    return api.users.get(user_ids=online_friends_ids)

Second way is call only one API method:  with parametres perform get.users with parametres = "online".
      def get_friends_online_list(login, password):
    friends_online_list = []
    online = 1
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    all_friends_info = api.friends.get(fields="online", order="name")
    for friend in all_friends_info:
        if friend["online"] == online:
            friends_online_list.append(friend)
    return friends_online_list

This script is written in a second way because friends.get() online allows to order the friends list by name. It is more convenient, but it is slower and a bit longer. 
As it aren't any additional conditions at the task I have choosen the second way.
