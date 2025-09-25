capitals = {
    "México": "México City", #Keys:values = word: meaning
    "Canada": "Otawa",
    "Brazil": "Brazilia" #In the last doesn´t need a comma.
    # "Canada": "Montreal" //it would choose the new word. So it needs to be a unique word.
}
capitals["Italy"] = "Rome" #To add a new key and value.//Is not part of the dictonary, but we can asaign a value.
del capitals["Brazil"] #"del" is for delete keys and value xdxd.
capitals.pop("Canada") # another method to delete :v.
capitals.clear()#clear👍. Deleates all the list.

print(capitals) 
# print(capitals["Canada"]) # instead of just putting "capitals", we can put an specific country


#////////Harry Potter lists.
# students = {
#     "Hermione":"Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron":"Gryffindor",
#     "Draco": "Slytherin" 

# }    print(students["Draco"])

# for key in students:
#     print(f"{key}: {students[key]}") // 


students = [
        {"name": "Hermione",
        "house": "Gryffindor",
        "patronus": "Otter"
        },

    {"name": "Harry", "house": "Gryffindor","patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor","patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin","patronus": None}
]

for element in students:
    print(f"{element["name"]},{element["house"]},{element["patronus"]}")
