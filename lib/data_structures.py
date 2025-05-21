spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    """
    Return a list of names of all spicy foods.
    """
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """
    Return a list of spicy foods (dicts) with heat_level > 5.
    """
    return [food for food in spicy_foods if food.get("heat_level", 0) > 5]

def print_spicy_foods(spicy_foods):
    """
    Print each spicy food in the format:
    Name (Cuisine) | Heat Level: 🌶🌶🌶
    where the number of peppers corresponds to the heat_level.
    """
    for food in spicy_foods:
        peppers = "🌶" * food.get("heat_level", 0)
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {peppers}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """
    Find and return the first spicy food dict matching the given cuisine.
    If no match is found, returns None.
    """
    for food in spicy_foods:
        if food.get("cuisine") == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    """
    Print only the spiciest foods (heat_level > 5) in the same format as print_spicy_foods.
    """
    for food in get_spiciest_foods(spicy_foods):
        peppers = "🌶" * food.get("heat_level", 0)
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {peppers}")

def get_average_heat_level(spicy_foods):
    """
    Calculate and return the average heat level of the spicy foods as an integer.
    """
    total_heat = sum(food.get("heat_level", 0) for food in spicy_foods)
    count = len(spicy_foods)
    return total_heat // count if count else 0

def create_spicy_food(spicy_foods, spicy_food):
    """
    Add a new spicy food dict to the list and return the updated list.
    """
    spicy_foods.append(spicy_food)
    return spicy_foods

