import discord as discord
from discord import Embed
from discord.ext import commands
from discord_slash.context import ComponentContext
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils import manage_commands
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
from selects import Selects
from bot_enums import Keys, Regions
from pollution_check import PollutionCheck, Search
from category_embeds import Categories
from pollutant_embeds import Pollutants
from storage import Storage
from buttons import Buttons
from database import WatchList

TOKEN = Keys.TOKEN.value  # discord bot token
client = commands.Bot(command_prefix='$', activity=discord.Game(name='/'))  # setup discord client
slash = SlashCommand(client)


@client.event
async def on_ready():
    print('up')


@slash.component_callback(components=["pollutant_select"])
async def pollutant_select_callback(ctx: ComponentContext) -> None:
    """
    Change embed to reflect pollutant selection
    :param ctx: Implicitly passed on callback
    :return: None
    """
    option = ctx.selected_options[0]
    if option in list(Pollutants.pollutants.keys()):
        await ctx.edit_origin(embed=Pollutants.pollutants[option])


@slash.component_callback(components=["category_select"])
async def category_select_callback(ctx: ComponentContext):
    """
    Change category to reflect category selection
    :param ctx:
    :return:
    """
    option = ctx.selected_options[0]
    if option in list(Categories.categories.keys()):
        await ctx.edit_origin(embed=Categories.categories[option])


@slash.component_callback(components=['aqi'])
async def aqi_callback(ctx: ComponentContext) -> None:
    """
    On AQI button press change embed to AQI embed
    :param ctx:
    :return:
    """
    aqi_embed = Embed(
        title='Air Quality Index',
        description='Air Quality Index (AQI) is the measurement of pollutants in the air and how severe they are',
        color=0x8fce00,
    )
    aqi_embed.set_image(url='https://www.epa.gov/sites/default/files/2019-07/aqitableforcourse.png')
    aqi_embed.set_footer(text='Powered by Ambee', icon_url='https://docs.ambeedata.com/favicon.ico')
    instance = Storage.get_instance(ctx.origin_message_id)
    instance_category = instance.data.category
    instance_pollutant = instance.data.pollutant
    await ctx.edit_origin(embed=aqi_embed,
                          components=[Buttons.generate_aqi_buttons(instance_category, instance_pollutant)])


@slash.component_callback(components=['home'])
async def home_callback(ctx: ComponentContext) -> None:
    """
    On Home button press return back to orginal embed
    :param ctx:
    :return:
    """
    message_id = ctx.origin_message_id
    embed = Storage.get_place_embed(message_id)
    instance = Storage.get_instance(message_id)
    instance_category = instance.data.category
    instance_pollutant = instance.data.pollutant
    await ctx.edit_origin(embed=embed,
                          components=[Buttons.generate_main_buttons(instance_category, instance_pollutant)])


@slash.component_callback(components=['added'])
async def added_button_callback(ctx: ComponentContext) -> None:
    message_id = ctx.origin_message_id
    instance = Storage.get_instance(message_id)
    user_id = ctx.author_id
    instance_category = instance.data.category
    instance_pollutant = instance.data.pollutant
    watch_list.remove_user(user_id)
    watch_list.test_db()
    await ctx.edit_origin(components=[Buttons.generate_main_buttons(instance_category, instance_pollutant)])


@slash.component_callback(components=['watch'])
async def watch_list_callback(ctx: ComponentContext) -> None:
    message_id = ctx.origin_message_id
    instance = Storage.get_instance(message_id)
    user_id = ctx.author_id
    country = instance.country_code
    region = instance.value
    instance_category = instance.data.category
    instance_pollutant = instance.data.pollutant
    watch_list.add_update(user_id, country, region)
    watch_list.test_db()
    await ctx.edit_origin(components=[Buttons.generate_watch_buttons(instance_category, instance_pollutant)])


@slash.component_callback(components=list(Categories.categories.keys()))
async def category_callback(ctx: ComponentContext) -> None:
    if ctx.component_id in list(Categories.categories.keys()):
        instance = Storage.get_instance(ctx.origin_message_id)
        instance_pollutant = instance.data.pollutant
        await ctx.edit_origin(embed=Categories.categories[ctx.component_id],
                              components=[Buttons.generate_category_buttons(instance_pollutant),
                                          Selects.generate_category_select()])


@slash.component_callback(components=list(Pollutants.pollutants.keys()))
async def pollutant_callback(ctx: ComponentContext) -> None:
    if ctx.component_id in list(Pollutants.pollutants.keys()):
        instance = Storage.get_instance(ctx.origin_message_id)
        instance_category = instance.data.category
        await ctx.edit_origin(embed=Pollutants.pollutants[ctx.component_id],
                              components=[Buttons.generate_pollutant_buttons(instance_category),
                                          Selects.generate_pollutant_select()])


@slash.slash(name="CheckPollution", description="Get the pollution levels of an area",
             options=[manage_commands.create_option(name="country",
                                                    description='Country to check pollution level',
                                                    option_type=3,
                                                    required=True),
                      manage_commands.create_option(name="region",
                                                    description='Country to check pollution level of',
                                                    option_type=3,
                                                    required=False,
                                                    choices=["City", "Postal Code"]),

                      manage_commands.create_option(name="value",
                                                    description="Get the pollution level by postal code or city",
                                                    option_type=3,
                                                    required=False, )], guild_ids=[957156782994771968])
async def check_pollution(ctx: SlashContext, country, region=None, value=None):
    async def add_buttons(category: str, pollutant: str, sent_message):

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
                label="Add To Watch List",
                custom_id="watch"
            )
        ]
        action_row = create_actionrow(*buttons)
        await sent_message.edit(components=[action_row])

    await ctx.defer()  # responses that take longer than 3 seconds must be deferred
    if region is not None and value is not None:  # make sure all relevant data is present
        parsed_region = Regions.get_class(region)  # get enum for region
        pollution_instance = PollutionCheck(country, parsed_region, value)
    else:
        pollution_instance = PollutionCheck(country)
    await pollution_instance.set_country_code()
    await pollution_instance.set_pollution_data()
    if pollution_instance.valid_query is False:
        await ctx.send("No Data for Region")
        return
    embed = await pollution_instance.generate_embed()
    message = await ctx.send(embed=embed)
    Storage.instances[message.id] = pollution_instance  # store all the data for embed generation
    Storage.place_embeds[message.id] = embed  # Store embed itself so button can retrieve it
    await add_buttons(pollution_instance.data.category, pollution_instance.data.pollutant, message)


@client.command()
async def test(ctx):
    """
    General Test case for watchlist, Will look over all watched regions and return an alert if any region has moderate
     or above pollution levels
    :param ctx:
    :return:
    """
    await Search.check_watchlist(watch_list)
    user_id = ctx.message.author.id
    user_info = Storage.watch_data[user_id]
    await ctx.send(
        f"ALERT - Your Region {user_info[1]} has High Pollution take actions to protect yourself, and reduce emissions")


if __name__ == "__main__":
    watch_list = WatchList()  # initialize database
    client.run(TOKEN)  # start bot
