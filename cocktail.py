class Cocktail:
    def __init__(self, name, isAlcoholic, instructions, ingredients):
        self.name = name
        self.isAlcoholic = isAlcoholic
        self.instructions = instructions
        self.ingredients = ingredients
    
    def display(self):
        print("----------------------------------------")
        print(f"Name: {self.name}\n")
        print(f"Alcoholic: {True if self.isAlcoholic == 'Alcoholic' else False}\n")
        print("Ingredients:")
        for ing in self.ingredients:
            print(f"{ing[0]} - {ing[1]}\n")
            
        print(f"Instructions:\n{self.instructions}")
        print("----------------------------------------")