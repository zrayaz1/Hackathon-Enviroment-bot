from discord import Embed
from typing import Union
from bot_enums import Regions, Country
from fuzzywuzzy import process
from aiohttp import ClientSession
from bot_enums import Urls, Keys
from typing import Dict
from storage import Storage


class PollutionData:
    def __init__(self, data):
        """
        separates data from ambee endpoints and puts em all nice and neatly as instance variables

        :param data: json from AMBEE call converted to dict only
        """
        self.data = data
        self.station_data = self.data["stations"][0]
        self.CO = self.station_data["CO"]
        self.NO2 = self.station_data["NO2"]
        self.OZONE = self.station_data["OZONE"]
        if "PM10" in list(self.station_data.keys()):
            self.PM10 = self.station_data["PM10"]
        else:
            self.PM10 = "No Data"
        self.PM25 = self.station_data["PM25"]
        self.SO2 = self.station_data["SO2"]
        self.AQI = self.station_data["AQI"]
        self.pollutant = self.station_data["aqiInfo"]['pollutant']
        self.concentration = self.station_data["aqiInfo"]['concentration']
        self.category = self.station_data["aqiInfo"]['category']


class PollutionCheck:
    def __init__(self, country: str, region: Regions = None, value: Union[int, str] = None):
        self.country = country
        self.country_code = None
        self.region = region
        self.value = value
        self.data = None
        self.valid_query = True

    async def set_pollution_data(self) -> None:
        """
        Generates all the pollution data and assigns it to the instance variable
        """
        if self.region == Regions.CITY:
            output = await Search.ambee_city(self.value)
            self.data = PollutionData(output)
        elif self.region == Regions.POSTAL_CODE:
            output = await Search.ambee_postal(self.country_code, self.value)
            self.data = PollutionData(output)
        else:
            output = await Search.ambee_country(self.country_code)
            if len(output['stations']) > 0:
                self.data = PollutionData(output)
            else:
                self.valid_query = False

    async def set_country_code(self) -> None:
        """
        Given a country code, country name, or partial country name sets the country code to the proper one,
        Fuzzy string matching on inputs.
        :return: None
        """
        country_dict = Country.COUNTRIES.value
        names = list(country_dict.keys())
        codes = list(country_dict.values())
        total_list = names + codes
        country_guess = process.extractOne(self.country, total_list)[0]
        if country_guess in codes:
            code = country_guess
        else:
            code = country_dict[country_guess]
            self.country = country_guess
        self.country_code = code

    async def generate_embed(self) -> Embed:
        """
        Uses the data to generate a main embed
        for user display
        :return: Discord.Embed
        """
        main_embed = Embed(
            color=0x607c3c,
            description=f"Air Status: **{self.data.category}**"
        )

        main_embed.add_field(name=f'AQI: `{self.data.AQI}`',
                             value=f"Pollutant: `{self.data.pollutant}`\n"
                                   f"Concentration: `{self.data.concentration}`\n"
                                   f" Category: `{self.data.category}`\n",
                             inline=True
                             )
        main_embed.add_field(name="More Info", value="Click Buttons Below\n"
                                                     "**Click Watch**\n"
                                                     "Watch your location and get alerts!", inline=True)
        main_embed.set_thumbnail(url=Urls.FLAGS.value + self.country_code)
        main_embed.add_field(name='Pollutants',
                             value=f'CO:`{self.data.CO}`\n'
                                   f"NO2: `{self.data.NO2}`\n"
                                   f"OZONE: `{self.data.OZONE}`\n"
                                   f"PM10: `{self.data.PM10}`\n"
                                   f"PM25: `{self.data.PM25}`\n"
                                   f"SO2: `{self.data.SO2}`\n",
                             inline=False
                             )

        if self.value:
            main_embed.title = f'Air Quality of {self.value.capitalize()}'
        else:
            main_embed.title = f'Air Quality of {self.country}'
        main_embed.set_footer(text='Powered by Ambee',
                              icon_url=Urls.AMBEE_IMAGE.value)
        return main_embed


class Search:
    """
    Handles different async searches needed for the bot
    """

    @staticmethod
    async def async_search(url: str, headers: dict, querystring: dict) -> dict:
        """ Handles Async searching and converting json to python types.
        :param querystring: Query parameters
        :param headers: Query headers
        :param url: Url to search
        :return: Data or if id dict[data, id]
        """
        async with ClientSession() as session:
            async with session.get(url, headers=headers, params=querystring) as search:
                if search.status == 200:
                    json_output = await search.json()
                    return json_output


    @classmethod
    async def ambee_city(cls, city: str) -> Dict:
        """
        Ambee citywise pollution search

        :param city: Str
        :return:
        """
        url = Urls.AMBEE_CITY.value
        querystring = {"city": city}
        headers = {
            'x-api-key': Keys.AMBEE.value,
            'Content-type': "application/json"
        }
        output = await cls.async_search(url, headers, querystring)
        return output

    @classmethod
    async def ambee_country(cls, country_code: str) -> Dict:
        url = Urls.AMBEE_COUNTRY.value
        querystring = {"countryCode": country_code}
        headers = {
            'x-api-key': Keys.AMBEE.value,
            'Content-type': "application/json"
        }
        output = await cls.async_search(url, headers, querystring)
        return output

    @classmethod
    async def ambee_postal(cls, country_code: str, postal_code: str) -> Dict:
        url = Urls.AMBEE_POSTAL.value
        querystring = {"postalCode": postal_code, "countryCode": country_code}
        headers = {
            'x-api-key': Keys.AMBEE.value,
            'Content-type': "application/json"
        }
        output = await cls.async_search(url, headers, querystring)
        return output

    @classmethod
    async def check_watchlist(cls, db):
        for user in db.get_watches():
            # caleb is stupid and inserted bad data and im too lazy to remove it
            if user[0] == 616301022939447336:
                continue

            response = await cls.ambee_country(user[1])
            formatted = PollutionData(response)
            if formatted.AQI > 50:
                Storage.watch_data[user[0]] = user
