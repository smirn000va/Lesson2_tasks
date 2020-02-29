dict_1 =[
{'school_class': '4a', 'scores': [3,4,4,5,2]},
{'school_class': '4b', 'scores': [5,3,4,5,5]},
{'school_class': '4d', 'scores': [5,4,5,5,4]},
{'school_class': '4c', 'scores': [3,4,3,5,3]}
    
]

#print(school)

sum_average_class=0
sum_len=0

for class_1 in dict_1:
  #print (school_class.get('scores'))
  average_class=float(sum(class_1.get('scores')))/len(class_1.get('scores'))
  #print(school_class.get(school_class))

  print('Средняя оценка по классу',class_1.get('school_class'),':', average_class)

  sum_average_class += sum(class_1.get('scores'))

  sum_len=sum_len+len(class_1.get('scores'))
#print(sum_average_class)
#print(sum_len)
average_school=sum_average_class/sum_len
  
print(average_school)
