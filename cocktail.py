class Cocktail:
    def __init__(self, name, isAlcoholic, instructions, ingredients, image):
        self.name = name
        self.isAlcoholic = isAlcoholic
        self.instructions = instructions
        self.ingredients = ingredients
        self.image = image
    
    def display(self):
        print("----------------------------------------")
        print(f"Name: {self.name}\n")
        print(f"Alcoholic: {True if self.isAlcoholic == 'Alcoholic' else False}\n")
        print("Ingredients:")
        for ing, measure in self.ingredients:
            print(f"{ing} - {measure}\n")
            
        print(f"Instructions:\n{self.instructions}")
        print("----------------------------------------\n")