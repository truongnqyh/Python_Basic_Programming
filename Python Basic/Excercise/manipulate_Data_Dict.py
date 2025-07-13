person = {"name": "Truong", "Age": "26", "Grade": "A"}
person["Address"] = "Quang Yen"
if "Grade" in person:
    del person["Grade"]

print(person)