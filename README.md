# 8_vk_friends_online
This script finds who is online in vkontakte social network. It returns list of your friends, which are on the site now.
## launching
Type following command in console to launch script:`vk_friends_online.py`  
After this you will be prompted to enter your login and password.
## Two ways of writting get_friends_online_list function this script.
There are two ways of getting online friends by VK API. The first way is to call get.friends.getOnline() for getting friends ids and then pass it to get.users() method which give us info from user id.    

   блок кода   

Second way is call only one API method:  with parametres perform get.users with parametres = "online".        
   блок кода    
   
This script is written in a second way because friends.get() online allows to order the friends list by name. It is more convenient, but it is slower and a bit longer. 
As it aren't any additional conditions at the task I have choosen the second way.
