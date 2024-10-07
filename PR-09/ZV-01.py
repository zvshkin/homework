technical_school = {
    'ИС-23А' : '24',
    'ИС-23Б' : '25',
    'ИС-22А' : '22',
    'ИС-22Б' : '21',
    'ИС-21А' : '20',
    'ИС-21Б' : '23'}

x = input("Введите группу, в которой хотите узнать кол-во учеников: ")
print(technical_school.get(x), "человек, учится в группе", x)

print("\nНа третьем курсе изменилось кол-во студентов.")
technical_school['ИС-22А'] = int(input("ИС-22А: "))
technical_school['ИС-22Б'] = int(input("ИС-22Б: "))

print("\nВ техникуме появились две новые группы:")
y = input("1-ая новая группа: ")
yy = input("Поступило студентов: ")
z = input("2-ая новая группа: ")
zz = input("Поступило студентов: ")
technical_school[y] = yy
technical_school[z] = zz

q = input("\nПроизошёл расформ одной группы, это была: ")
technical_school.pop(q)

print("\nДанные групп и студентов в них:", technical_school)