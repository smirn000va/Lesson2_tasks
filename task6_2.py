date_1={'Как дела?': 'Хорошо',  'Что делаешь?': 'Программирую'}

while True:
    question=input('Задайте свой вопрос: ')
    if question in date_1:
        print(date_1.get(question))
        break

    else:
        print('Такого вопроса нет')
    
      
      
   

        