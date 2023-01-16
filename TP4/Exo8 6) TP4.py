student_info = {}

first_name = input("Entrez votre prénom: ")
last_name = input("Entrez votre nom: ")
promotion = input("Entrez votre promotion: ")
group = input("Entrez votre groupe de TP: ")


student_info["first_name"] = first_name
student_info["last_name"] = last_name
student_info["promotion"] = promotion
student_info["group"] = group

print("Les clés du dictionnaires sont:")
for key, value in student_info.items():
  print(key)

print("Les valeurs du dictionnaires sont:")
for key, value in student_info.items():
  print(value)

print("Les tuplets du dictionnaires sont:")
for key, value in student_info.items():
  print(key+value)