from discord_slash.utils.manage_components import create_actionrow, create_select, create_select_option
from category_embeds import Categories
from pollutant_embeds import Pollutants


class Selects:
    """
    Handles selects generation for the pollutants and category's all function return action row object
    """
    @staticmethod
    def generate_pollutant_select():
        select = create_select(options=[create_select_option(i, value=i) for i in list(Pollutants.pollutants.keys())],
                               placeholder="Select Pollutant",
                               custom_id='pollutant_select')
        action_row = create_actionrow(select)
        return action_row

    @staticmethod
    def generate_category_select():
        select = create_select(options=[create_select_option(i, value=i) for i in list(Categories.categories.keys())],
                               placeholder="Select Category",
                               custom_id='category_select')
        action_row = create_actionrow(select)
        return action_row
