date_1={'Как дела?': 'Хорошо',  'Что делаешь?': 'Программирую'}

def user(date_1):
    while True:
        try:
            question=input('Задайте свой вопрос: ')
            if question in date_1:
                print(date_1.get(question))
                break
            else:
                print('Такого вопроса нет')

        except KeyboardInterrupt:
            print ('\nПока')
            break

        
user(date_1)