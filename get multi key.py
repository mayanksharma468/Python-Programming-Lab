'''student_details = {'name':'kirti','age':18,'location':'Bengal','Country':'Indian'}
new_dict = {key: student_details[key] for key in ['name', 'age']}
print(new_dict)'''
student_details = {'name':'kirti','age':18,'location':'Bengal','Country':'Indian'}
new_dict={}
for key in student_details.items():
    new_dict.update({'name':student_details['name']})
    new_dict.update({'age':student_details['age']})
print(new_dict)
