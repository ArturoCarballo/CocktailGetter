import requests
import json
from cocktail import Cocktail

base_url = "https://www.thecocktaildb.com/api/json/v1/1/"

def responseToFile(data):
    try:
        with open('cocktail_data.json', 'w') as file:
            json.dump(data, file, indent=4)
        
        print("Data saved to cocktail_data.json")

    except IOError as e:
        print(f"An error occurred: {e}")

def randomCocktail():
    # Fetch a random cocktail
    response = requests.get(base_url + "random.php")
    data = response.json()

    responseToFile(data)

    return data['drinks'][0]

def searchByName(cocktail_name):
    response = requests.get(base_url + f"search.php?s={cocktail_name}")
    data = response.json()

    responseToFile(data)

    cocktails = []

    for drink in data['drinks']:
        cocktails.append(createCocktail(drink))
    
    return cocktails


def createCocktail(cocktailData):
    ingredients = []

    for i in range(1, 16):
        ingredient = cocktailData[f'strIngredient{i}']
        measure = cocktailData[f'strMeasure{i}']

        if ingredient:
            ingredients.append((ingredient, measure))

    cocktail = Cocktail(cocktailData['strDrink'], cocktailData['strAlcoholic'], cocktailData['strInstructions'], ingredients, cocktailData['strDrinkThumb'])
    
    return cocktail