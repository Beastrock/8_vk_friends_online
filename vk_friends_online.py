import vk
from getpass import getpass

APP_ID = 5723136  # app_id - unique code of this app


def get_user_login():
    return input("Input login:\n")


def get_user_password():
    return getpass.getpass(prompt="Input password:\n")


def get_friends(login, password):
    friends_online_list = []
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    all_friends_info = api.friends.get(fields="online", order="name")
    for friend in all_friends_info:
        if friend["online"] == 1:
            friends_online_list.append(online_friend)
    return friends_online_list


def output_online_friends_to_console(friends_online_list):
    from_one = 1
    print("Number of online friends: {}".format(len(friends_online_list)))
    for number, online_friend in enumerate(friends_online_list, from_one):
        if not online_friend:
            continue
        print("{}) {dict[first_name]} {dict[last_name]}".
              format(number, dict=online_friend))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_friends_online_list(login, password)
    output_online_friends_to_console(friends_online)
