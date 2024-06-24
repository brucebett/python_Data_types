# 1.List
# names = ['john', 'Smith', 'andrew']
# 2.Tuple
# names = ('john', 'smith', 'andrew')
# 3.Sets
# names = ('john', 'smith', 'andrew')
# 4.Dictionary
# students = {'john':100, 'smith':300, 'andrew':200}


# 1.List

employees = ['Peter', 'John', 'Smith', 'Ruth', 'Esther', 'Annstacia']
print(employees)
print(employees[2])
print(employees[1:5])
print(employees[0:2])
employees[1] = 'Alex'
print(employees)
employees[3] = 'Moses'
print(employees)
employees.append('Zack')
print(employees)
employees.append('Pauline')
print(employees)
employees.insert(0, 'jack')
print(employees)
employees.extend(['kamau', 'Mutua', 'Wafula'])
print(employees)

marks = [200, 350, 420, 308]
print(max(marks))
print(min(marks))
print(sum(marks))

# 2.Tuple
Languages = ('python', 'java', 'php', 'kotlin')
print(Languages)
print(Languages[1])
print(Languages[3:6])
mytuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(max(mytuple))
print(min(mytuple))
print(sum(mytuple))

# 3.Set
mysets = {1, 2, 4, 5, 6, 7, 8, 9}
print(mysets)
number = 6
if number in mysets:
    output = number
    print('output')

majina = {'john', 'smith', 'ruth', 'esther'}
name = 'esther'
if name in majina:
    jina = name
    print(jina)

maneno = {'john', 'smith', 'ruth', 'esther'}
name = 'smith'
if name in maneno:
    neno = name
    print(neno)

majina.add('charles')
print(majina)
majina.update(['njoroge', 'collins', 'peter'])
print(majina)

# 4.Dictionary
Books = {
    'Title': 'The code',
    'Author': 'John Doe',
    'Year Published': 2000
}
print(Books)
Books['version'] = 'version 1'
print(Books)

if 'Title' in Books:
    print('yes it is in the dictionary')
else:
    print('No it is not in the dictionary')

Students = {
    'Uniform color': 'Black & Red',
    'Classes': '10 streams',
    'Total': 4000
}
print(Students)
Students['lunch'] = 'githeri'
print(Students)

if 'lunch' in Students:
    print('yes it is in the dictionary')
else:
    print('No it is not in the dictionary')
