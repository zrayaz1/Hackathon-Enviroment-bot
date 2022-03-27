from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle


class Buttons:
    """
    Wrapper for button generation functions, all return an action row object
    """
    @staticmethod
    def generate_watch_buttons(category: str, pollutant: str):
        buttons = [
            create_button(
                style=ButtonStyle.green,
                label="AQI",
                custom_id='aqi'),

            create_button(
                style=ButtonStyle.blurple,
                label=category,
                custom_id=category),
            create_button(
                style=ButtonStyle.red,
                label=pollutant,
                custom_id=pollutant
            ),
            create_button(
                style=ButtonStyle.blue,
                label="Added!",
                custom_id="added"
            )
        ]
        action_row = create_actionrow(*buttons)
        return action_row

    @staticmethod
    def generate_main_buttons(category: str, pollutant: str):
        buttons = [
            create_button(
                style=ButtonStyle.green,
                label="AQI",
                custom_id='aqi'),

            create_button(
                style=ButtonStyle.blurple,
                label=category,
                custom_id=category),
            create_button(
                style=ButtonStyle.red,
                label=pollutant,
                custom_id=pollutant
            ),
            create_button(
                style=ButtonStyle.blue,
                label="Watch",
                custom_id="watch"
            )
        ]
        action_row = create_actionrow(*buttons)
        return action_row

    @staticmethod
    def generate_aqi_buttons(category: str, pollutant: str):
        buttons = [
            create_button(
                style=ButtonStyle.green,
                label="Home",
                custom_id='home'),

            create_button(
                style=ButtonStyle.blurple,
                label=category,
                custom_id=category),
            create_button(
                style=ButtonStyle.red,
                label=pollutant,
                custom_id=pollutant
            )
        ]
        action_row = create_actionrow(*buttons)
        return action_row

    @staticmethod
    def generate_category_buttons(pollutant: str):
        buttons = [
            create_button(
                style=ButtonStyle.green,
                label="AQI",
                custom_id='aqi'),

            create_button(
                style=ButtonStyle.blurple,
                label='Home',
                custom_id='home'),
            create_button(
                style=ButtonStyle.red,
                label=pollutant,
                custom_id=pollutant
            )
        ]
        action_row = create_actionrow(*buttons)
        return action_row

    @staticmethod
    def generate_pollutant_buttons(category: str):
        buttons = [
            create_button(
                style=ButtonStyle.green,
                label="AQI",
                custom_id='aqi'),

            create_button(
                style=ButtonStyle.blurple,
                label=category,
                custom_id=category),
            create_button(
                style=ButtonStyle.red,
                label="Home",
                custom_id='home'
            )
        ]
        action_row = create_actionrow(*buttons)
        return action_row
