
import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType

users = ['642042147'] #id друзей, которые будут добавлены в беседу.

def main():
    vk_session = vk_api.VkApi(token='5164b90f5f4d6402be64502e34607931ed416e17c97a6f99b2ec95dee4cb5ee20fd4db3cbd2ab6bdc4941') #можно узнать на vkhost.github.io
    api = vk_session.get_api()
   
    try:
        chats = input('Кол-во создаваемых бесед: ')
        spot = 0
        while int(spot) < int(chats):
            api.messages.createChat(user_ids=users, title="Created By FleeFy")
            spot += 1
            time.sleep(80) #время через, которое будет создаваться новая беседа (может сработать флуд контроль, не ставьте меньше)
    except Exception as er:
        print(er)
           
           
main()
