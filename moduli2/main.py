words = ("span", "inbox", "test121345678")
print(words[2])

person = ("Alice", 30, "Engineer")

name, age, profession = person

print(name, "profession is", profession, "and she is", age)

''' Dics '''
contact_info = {
    "Alice": "giywgefigwi",
    "Bob": "eopwhifiu",

}

print(contact_info["Alice"])

contact_info["ANA"] = "789-556"

del contact_info["Bob"]
print(contact_info)

print(contact_info.keys())

print(contact_info.items())

contact_information = {
    "Alice": {
    "phone-number": "889-654",
    "email": "ost@gmail.com",
    "birthday": "29/9/1899"
},
    "Mikal": {
    "phone-number": "889-654",
    "email": "ost563@gmail.com",
    "birthday": "29/9/1999"
},
    "Issac": {
    "phone-number": "889-654",
    "email": "ost654@gmail.com",
    "birthday": "29/9/2008"
},
}

print(contact_information["Alice"])

grades = {
    ("John", "Math"): 5,
    ("Alice", "Bio"): 4,
    ("Bob", "Pys"): 2
}

print(grades[("John", "Math")])

grades[("Bob, Math")] = 5

print(grades)