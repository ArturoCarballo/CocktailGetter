import requests
import json
from cocktail import Cocktail

base_url = "https://www.thecocktaildb.com/api/json/v1/1/"

def responseToFile(data):
    try:
        with open('cocktail_data.json', 'w') as file:
            json.dump(data, file, indent=4)
        
        print("Data saved to cocktail_data.json")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

def randomCocktail():
    # Fetch a random cocktail
    response = requests.get(base_url + "random.php")
    data = response.json()

    responseToFile(data)

    cocktail = data['drinks'][0]

    #print(cocktail['strDrink'])

    return cocktail

def searchByName():
    cocktail_name = "Margarita"
    response = requests.get(base_url + f"search.php?s={cocktail_name}")
    data = response.json()

    responseToFile(data)

    for drink in data['drinks']:
        print(drink['strDrink'])

def createCocktail(cocktailData):
    ingredients = []
    measures = []

    for i in range(1, 16):
        ingredient = cocktailData[f'strIngredient{i}']
        measeure = cocktailData[f'strMeasure{i}']

        if ingredient:
            ingAndMea = []
            ingAndMea.append(ingredient)
            ingAndMea.append(measeure)

            ingredients.append(ingAndMea)

    cocktail = Cocktail(cocktailData['strDrink'], cocktailData['strAlcoholic'], cocktailData['strInstructions'], ingredients)
    cocktail.display()


createCocktail(randomCocktail())