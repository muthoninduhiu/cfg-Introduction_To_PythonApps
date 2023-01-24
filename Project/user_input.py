from recipe_search import recipe_search

# Ask the user to enter an ingredient that they want to search for, ask extra question
has_diet = input('Are you On A Diet?? ')
if has_diet == 'yes':
    diet_restriction = input(
        'Select an option from the following list:'
        '\n - balanced'
        '\n - high-fiber'
        '\n - high protein'
        '\n - low-carb'
        '\n - low-fat'
        '\n - low-sodium'
        '\n >'
    )
else:
    diet_restriction = None
has_meal_type = input('Are you looking for a particular meal type?? ')
if has_meal_type == 'yes':
    meal_type = input(
        'Select an option from the following list:'
        '\n - breakfast'
        '\n - lunch'
        '\n - snack'
        '\n - teatime'
        '\n - dinner'
        '\n > '
    )
else:
    meal_type = None
ingredient = input('Enter an ingredient: ')


# Get the returned recipes from the API response
def user_input():
    """
        :Purpose: Get user input and use it to pull data from the API
        :return: has no return type
        Function that asks for user  input and uses that to search for the value in the API
        then save the results to a file
        """
    list_of_recipes = recipe_search(ingredient, diet_restriction, meal_type)

    if not list_of_recipes:
        print("No recipe matches your search!")
    else:
        for result in list_of_recipes:
            recipes = result['recipe']
            # print(recipes)
            # Save the results to a file recipe_names.txt
            with open('recipe_names.txt', 'a+', encoding='utf-8') as recipe_details:
                recipe_details.write("Name: {}\nThe Ingredients: {}\nWeight: {}\nCuisine Type: {}\nHealth Label: {}\n"
                                     .format(recipes['label'],
                                             (recipes['ingredientLines']),
                                             (recipes['totalWeight']),
                                             recipes['cuisineType'],
                                             recipes['healthLabels']))
                recipe_details.write("\n")


# Display the recipes for each search result
def read_text():
    """
            :Purpose: Read data in the text file and display it
            :return: has no return type
            """
    with open('recipe_names.txt', 'r') as text_file:
        contents = text_file.read()
        print(contents)
