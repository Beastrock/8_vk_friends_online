# 8_vk_friends_online
This script finds which of your friends are online in Vkontakte social network.
## launching
Type following command in console to launch script:`vk_friends_online.py`  
After this you will be prompted to enter your login and password.
## two ways of writing get_friends_online_list function
There are two ways of getting online friends by VK API. The first way is to call get.friends.getOnline() for getting friends ids and then pass it to get.users() method which give us info from user id. It is **shorter** then the second way.

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

Second way is call only one API method get.users with parametres = "online". Comparing from the first way it allows **to order friends list** by name, which is more convenient.

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
   
As it aren't any additional conditions at the task it was choosen to write it in a second way.
