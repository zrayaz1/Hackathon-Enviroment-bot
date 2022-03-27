from discord import Embed
from bot_enums import Urls

"""
Embeds for all the category's of AQI
"""

hazardous_embed = Embed(title=f'API Index: Hazardous',
                        description='Index Value: 301-500',
                        color=0x800000)

hazardous_embed.add_field(name='Maroon',
                          value='Everyone should avoid all physical activity outdoors, unsafe for any kind of '
                                'physical activity',
                          inline=True)
hazardous_embed.set_footer(text='Powered by Ambee', icon_url=Urls.AMBEE_IMAGE.value)
hazardous_embed.set_thumbnail(url='https://media.discordapp.net/attachments/957156782994771971/957721795761438830/AQI-maroon.jpg')
bad_embed = Embed(title=f'Very Unhealthy',
                  description='Index Value: 201-300',
                  color=0xCA33FF)

bad_embed.add_field(name='Purple',
                    value='Sensitive groups should avoid all physical activity outdoors; the general public should avoid prolonged or heavy exertion',
                    inline=True)
bad_embed.set_footer(text='Powered by Ambee', icon_url=Urls.AMBEE_IMAGE.value)
bad_embed.set_thumbnail(url='https://media.discordapp.net/attachments/957156782994771971/957721796344414278/AQI-purple.jpg')
unhealthy_embed = Embed(title=f'Unhealthy',
                        description='Index Value: 151-200',
                        color=0xFF0000)
unhealthy_embed.set_thumbnail(url='https://media.discordapp.net/attachments/957156782994771971/957721796604489808/AQI-red.jpg')
unhealthy_embed.add_field(name='Red',
                          value='Sensitive groups should avoid prolonged or heavy exertion; the general public should '
                                'do the same',
                          inline=True)
unhealthy_embed.set_footer(text='Powered by Ambee', icon_url=Urls.AMBEE_IMAGE.value)

sensitive_embed = Embed(title=f'Unhealthy for Sensitive Groups',
                        description='Index Value: 101-150',
                        color=0xFF8000)

sensitive_embed.add_field(name='Orange',
                          value='Sensitive groups should reduce prolonged or heavy exertion',
                          inline=True)
sensitive_embed.set_footer(text='Powered by Ambee', icon_url=Urls.AMBEE_IMAGE.value)
sensitive_embed.set_thumbnail(url='https://media.discordapp.net/attachments/957156782994771971/957721796101156885/AQI-orange.jpg')
moderate_embed = Embed(title=f'Moderate',
                       description='Index Value: 51-100',
                       color=0xFBFF00)

moderate_embed.add_field(name='Yellow',
                         value='Usually sensitive people should reduce prolonged or heavy exertion',
                         inline=True)
moderate_embed.set_thumbnail(url='https://media.discordapp.net/attachments/957156782994771971/957721796914872360/AQI-yellow.jpg')
moderate_embed.set_footer(text='Powered by Ambee', icon_url=Urls.AMBEE_IMAGE.value)

good_embed = Embed(title=f'Good',
                   description='Index Value: 0-50',
                   color=0x13FF00)
good_embed.set_thumbnail(url='https://media.discordapp.net/attachments/957156782994771971/957721795455221890/AQI-green.jpg')
good_embed.add_field(name='Green',
                     value='Great Quality',
                     inline=True)
good_embed.set_footer(text='Powered by Ambee', icon_url=Urls.AMBEE_IMAGE.value)


class Categories:
    categories = {"Good": good_embed, "Moderate": moderate_embed, "Sensitive": sensitive_embed,
                  "Unhealthy": unhealthy_embed, "Bad": bad_embed, "Hazardous": hazardous_embed}
