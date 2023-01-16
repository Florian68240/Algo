student_info = {}

first_name = input("Entrez votre prénom: ")
last_name = input("Entrez votre nom: ")
promotion = input("Entrez votre promotion: ")
group = input("Entrez votre groupe de TP: ")


student_info["first_name"] = first_name
student_info["last_name"] = last_name
student_info["promotion"] = promotion
student_info["group"] = group



print("Votre prénom est {}".format(student_info["first_name"]))
print("Votre nom est {}" .format(student_info["last_name"]))
print("Votre promotion est {}" .format(student_info["promotion"]))
print("Votre groupe est {}" .format(student_info["group"]))