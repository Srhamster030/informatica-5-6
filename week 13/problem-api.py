import requests
import json
API_KEY = "2604a9b3e4faeb6ee3672e7f6f8fa165"
API_ID = "f795d624"
food = input("Select an ingredient:")
response = requests.get("https://api.edamam.com/api/nutrition-data?app_id=" + API_ID + "&app_key=" + API_KEY + "&nutrition-type=logging&ingr=" + food)
list_nutrients = [
"RIBF", "THIA", "FAPU", "NIA", "ENERC_KCAL",
"FASAT", "VITA_RAE", "VITC", "PROCNT", "CHOLE",
"FAMS", "CHOCDF", "FAT", "VITB6A", "VITB12", "FIBTG",
"WATER", "K", "P", "NA", "ZN", "CA", "MG", "FE", "FOLFD", "FOLAC", "FOLDFE"
]

search = response.json()

for result in search["ingredients"]:
    print(f"{result['text']}")
    for a in result["parsed"]:
        print(f"Quantity: {a["quantity"]}\nGrams: {a["weight"]}")
        for nutrient in list_nutrients:
            print(f"{nutrient}: {a['nutrients'][nutrient]}")