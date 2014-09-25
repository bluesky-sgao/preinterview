# update useage:
# result:
# <type 'dict'>
# {'name': 'sgao', 'id': '0001'}
# {'name': 'GG', 'id': '0001'}
# {'a': 'b', '1': '2', 'name': 'GG', 'id': '0001'}
# {'a': 'b', '1': '2', 'name': 'GG', 'title': 'title1', 'id': '2'}

dict = {'name':'sgao', 'id':'0001'}
print type(dict)
print dict
dict.update(name="GG")
print dict
a = (('a', 'b'), ('1', '2'))
dict.update(a)
print dict
dict.update({'title':'title1', 'id':'2'})
print dict