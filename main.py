class Queue:
    def __init__(self):
        self.list_queue = []
        self.con = 0

    def IsEmpty(self):
        return (True if len(self.list_queue) == 0 else False)

    def IsFull(self):
        return (True if len(self.list_queue) != 0 else False)

    def Engueue(self,value):
        self.list_queue.insert(self.con,value)
        self.con+=1

    def Dequeue(self):
        del self.list_queue[0]

    def Show(self):
        return self.list_queue

list_qu = Queue()

print("\t\t\t\t\t\t\t\t\t\tWELCOME!")
while True:
    print("\nКакую операцию хотите выбрать?\n"
          "1) Если хотите проверить на пустоту нажмите на 1\n"
          "2) Если хотите проверить на полноту нажмите на 2\n"
          "3) Если хотите добавить нажмите на 3\n"
          "4) Если хотите удалить нажмите на 4\n"
          "5) Если хотите увидеть очередь нажмите на 5\n"
          "6) Что бы выйти нажмите на 6\n")
    user = int(input("Выбирите пункт : "))
    if user == 1:
        print(list_qu.IsEmpty())
    elif user == 2:
        print(list_qu.IsFull())
    elif user == 3:
        user_add = input("Что хотите добавить?:")
        if user_add.isdigit():
            user_add = int(user_add)
        list_qu.Engueue(user_add)
        print("Элемент добавлен в очередь!")
    elif user == 4:
        try:
            list_qu.Dequeue()
            print("Первый элемент удален из очереди!")
        except:
            print("Очередь пустой!")
    elif user == 5:
        print(list_qu.Show())
    elif user == 6:
        break
#==============================================================
class PriorityQueue:
    def __init__(self):
        self.queue_with_priority = []
        self.con = 0
    def IsEmpty(self):
        return (True if len(self.queue_with_priority) == 0 else False)

    def IsFull(self):
        return (True if len(self.queue_with_priority) != 0 else False)

    def InsertWithPriority(self,value):
        self.queue_with_priority.insert(self.con,value)
        self.con+=1

    def PullHighestPriorityElement(self):
        del self.queue_with_priority[0]

    def Peek(self):
        try:
            return self.queue_with_priority[0]
        except:
            return "Очередь пустой!"

    def Show(self):
        return self.queue_with_priority

queue = PriorityQueue()

while True:
    print("\nКакую операцию хотите выбрать?\n"
          "1) Если хотите проверить на пустоту нажмите на 1\n"
          "2) Если хотите проверить на полноту нажмите на 2\n"
          "3) Если хотите добавить нажмите на 3\n"
          "4) Если хотите удалить нажмите на 4\n"
          "5) Если хотите увидеть элемент с высоким приоритетом нажмите на 5\n"
          "6) Если хотите увидеть очередь нажмите на 6\n"
          "7) Что бы выйти нажмите на 7\n")
    user_point = int(input())

    if user_point == 1:
        print(queue.IsEmpty())

    elif user_point == 2:
        print(queue.IsFull())

    elif user_point == 3:
        user_add = input("Что хотите добавить в очередь :")
        if user_add.isdigit():
            user_add = int(user_add)
        queue.InsertWithPriority(user_add)
        print("Элемент добавлен в очередь!")
        print(queue.Show())

    elif user_point == 4:
        try:
            queue.PullHighestPriorityElement()
        except:
            print("В очереди элемента нету!")
        print(queue.Show())

    elif user_point == 5:
        print(queue.Peek())

    elif user_point == 6:
        print(f"Число с высоким приоритетом {queue.Show()}!")

    elif user_point == 7:
        print("\t\t\t\t\t\t\t\t\t\t\t\tGood by! |^_^|")
        break

#==============================================================
print("\t\t\t\t\t\t\t\t\t\t\t\tWELCOME!")
slovar_for_users = {}
while True:
    print("\n1) Что бы добавить пользовотеля нажмите на 1\n"
          "2) Что бы удалить пользовотеля нажмите на 2\n"
          "3) Что бы проверить существует ли пользователь нажмите на 3\n"
          "4) Что бы изменить логин существующего пользователя нажмите на 4\n"
          "5) Что бы изменить пароль существующего пользователя нажмите на 5\n"
          "6) Что бы выйти нажмите на 6\n")
    user_point = int(input("Выбирите пункт:"))
    if user_point == 1:
        user_login = input("Логин:")
        user_password = input("Пароль:")
        slovar_for_users[user_login] = user_password

    elif user_point == 2:
        user_del = input("Введите логин пользователя:")
        try:
            del slovar_for_users[user_del]
            print(f"Пользователь \'{user_del}\' удален из словаря!")
        except:
            if slovar_for_users == {}:
                print("Словарь пустой!")
            elif user_del not in slovar_for_users and slovar_for_users != {}:
                print("Такого пользователя нету!")

    elif user_point == 3:
        user_for_exam = input("Введите логин пользователя для проверки на существования:")
        if user_for_exam in slovar_for_users:
            print(f"Пользователь \'{user_for_exam}\' существует в словаре!")
        elif user_for_exam not in slovar_for_users:
            print(f"Пользователь \'{user_for_exam}\' не существует в словаре!")

    elif user_point == 4:
        user_old_login = input("Введите логин пользователя:")
        if user_old_login not in slovar_for_users:
            print(f"Пользователь {user_old_login} не найден в словаре!")
            continue
        user_new_login = input("На что хотите изменять:")
        if user_old_login in slovar_for_users:
            slovar_for_users[user_new_login] = slovar_for_users[user_old_login]
            del slovar_for_users[user_old_login]
            print(slovar_for_users)


    elif user_point == 5:
        user_old_pass_login= input("Введите логин пользователь:")
        user_new_password = input("На что хотите поменять пароль:")
        if user_old_pass_login in slovar_for_users:
            slovar_for_users[user_old_pass_login] = user_new_password
            print(slovar_for_users)
            print(f"Пароль пользователя \'{user_old_pass_login}\' изменен на \'{user_new_password}\'!")

    elif user_point == 6:
        print("\t\t\t\t\t\t\t\t\t\t\t\tGood by :)")
        break