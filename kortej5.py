from collections import namedtuple
Student = namedtuple('Student', 'name age grade city')
students = (
     Student('Анастасия', '20', 4.5, 'Сочи'),
     Student('Ярослав', '14', 3.8, 'Москва'),
     Student('Алексей', '18', 4.8, 'Казань'),
     Student('Талалуша', '26', 3,5, 'Москва'),
     Student('Андрей', '17', 4,6, 'Екатеринбург'),
     Student('Ангелина', '17', 3,9, 'Норильск'),
     Student('Тараса', '23', 5.0, 'Омск'),
)
def gs(students):
    jh = 0

    for student in students:
       jh += student.grade
   o = jh / len(students)

   v = [student.name for student in students if student.grade >= o]
   print('Ученики ', ', '.join(v), ' в этом семестре хорошо учатся!')

gs(students)

    
    
