def namelist(names):
    #your code here
    namelist = []
  #  for elem in names:
   #     namelist.append(elem['name'])
    if len(names) == 1:
        return names[0]['name']
    elif len(names) > 1:
        str = names[0]['name']
        for i in range(1,len(names)-1):
            if i<=len(names)-2:
                str+=", "
            str+=names[i]['name']
        str+=" & "
        str+=names[len(names)-1]['name']
        return str
    else:
        return ''

print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))
