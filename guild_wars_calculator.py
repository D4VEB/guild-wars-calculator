import requests


class Items:

    def __init__(self):
        self.user_input = None

    @staticmethod
    def item_check(item_number):
        self.user_input("Enter the ID # for an item you want to look up.")
        if int(self.use_input) not in item_number:
                print("\nSorry. Invalid ID.")
                self.id_input = None
        return int(self.user_input)

    @staticmethod
    def item_search(user_input):
        item_lookup = requests.get("https://api.guildwars2.com/v2/items/{}".format(user_input))
        item = item_lookup.json()
        return item


class Item_Listing:

    def __init__(self, item_id, listing):
        self.item_id = item_id
        self.listing_search = listing

    @staticmethod
    def listing_lookup(user_input):
        listing_search = requests.get("https://api.guildwars2.com/v2/commerce/listings/{}".format(user_input))
        listing = listing_search.json()
        return listing

    @staticmethod
    def prices_search(listing_search):

        highest_price = listing_search['buys'][-1]['unit_price']
        lowest_price = listing_search['sells'][0]['unit_price']

        price_diff = lowest_price - highest_price
        print("Difference: {}".format(price_diff))

class Prices:

    def __init__(self, item_id):
        self.id = item_id

    @staticmethod
    def price_lookup(item_id):
        price_query = requests.get("https://api.guildwars2.com/v2/commerce/prices/{}".format(item_id))
        price = price_query.json()
        return price['buys']['unit_price']


class Recipes:

    def __init__(self):

        self.input_recipe = None

    def input_recipe(self):
        self.recipe_input = input("Enter an item ID # to search for a recipe: ")

        if int(self.recipe_input) not in **:
            print("That doesn't look like a valid ID.")
            self.recipe_input = None
        return int(self.input_recipe)

    @staticmethod
    def recipe_lookup(item_id):
        recipe_search = requests.get("https://api.guildwars2.com/v2/recipes/{}".format(item_id))
        recipe = recipe_search.json()
        return recipe


if __name__ == '__main__':

    item_fields = ['name', 'id', 'description', 'type','rarity', 'level', 'vendor_value','game_types', 'restrictions', 'details']
    recipe_fields = ['id', 'type', 'output_item_count', 'min_rating']
    listings = requests.get("https://api.guildwars2.com/v2/commerce/listings/")
    items_with_ids = listings.json()
    recipes = requests.get("https://api.guildwars2.com/v2/recipes/")
    recipes_with_ids = recipes.json()

