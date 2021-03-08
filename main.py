user_response = input("Enter a row: ")
a_list = user_response.split(' ')
print(str(a_list) + "\n")


data = [['Name: ', 'Job: ',  '    Student Number: '],
['Kevin:     ',  12332 , '      Student'],
['Emmanuel:  ',  43321 , '      Philosopher'],
['Philomena: ',  4552112, ' Saint']]

dash = '-' * 40

for i in range(len(data)):
    if i == 0:
      print(dash)
      print('{:<10s}{:>4s}{:>12s}'.format(data[i][0],data[i][1],data[i][2]))
      print(dash)
    else:
      print('{:<10s}{:>4d}{:^12s}'.format(data[i][0],data[i][1],data[i][2]))
a_list.append(data)
while user_response.strip().lower() != "done":
  a_list.append(data)
