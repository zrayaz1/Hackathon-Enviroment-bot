from discord import Embed
from bot_enums import Urls
"""
Embeds for all the different pollutants
"""
carbon_embed = Embed(title=f'Carbon Monoxide',
                     description='colorless and odorless gas that is toxic to inhale and highly flammable.',
                     color=0xececa3)

carbon_embed.add_field(name='Effects',
                       value='High levels for prolonged periods of time can cause dizziness, confusion, unconsciousness, and even death. High levels are not as common outdoors.',
                       inline=True)
carbon_embed.set_thumbnail(
    url='https://images.fosterwebmarketing.com/718/The%20Dangers%20of%20Carbon%20Monoxide%20Poisoning.png')

carbon_embed.set_footer(text='Powered by Ambee', icon_url=Urls.AMBEE_IMAGE.value)

nitrogen_embed = Embed(title=f'Nitrogen Dioxide',
                       description='a reddish-brown poisonous gas occurring commonly as an air pollutant. It forms when fossil fuels such as coal, oil, gas or diesel are burned at high temperatures',
                       color=0xb5e550)

nitrogen_embed.add_field(name='Effects',
                         value="NO2 particularly attacks the body's respiratory system causing: increased inflammation of the airways, worsened cough and wheezing, reduced lung function, and increased asthma attacks",
                         inline=True)

nitrogen_embed.set_thumbnail(
    url='https://tse1.mm.bing.net/th?id=OIP.jW9AOjtyjt36r5xaSzv_nwHaFj&pid=Api&P=0&w=236&h=177')

nitrogen_embed.set_footer(text='Powered by Ambee', icon_url=Urls.AMBEE_IMAGE.value)

ozone_embed = Embed(title=f'Ozone',
                    description="a colorless unstable toxic gas with a pungent odor and powerful oxidizing properties, formed from oxygen by electrical discharges or ultraviolet light. Is a natural part of earths atmosphere for expunging sunlight but is harmful in Earth's lower atmosphere",
                    color=0xabc32f)

ozone_embed.add_field(name='Effects',
                      value="An overabundance in Earth's lower atmosphere can cause breathing issues for sensitive humans but mostly harms the growth of plants.",
                      inline=True)

ozone_embed.set_thumbnail(
    url='https://tse3.mm.bing.net/th?id=OIP.07VvcgtHLnH7IOknOnTSwAHaIO&pid=Api&P=0&w=145&h=162')

ozone_embed.set_footer(text='Powered by Ambee', icon_url=Urls.AMBEE_IMAGE.value)

dust_embed = Embed(title=f'Particulate Matter 10 and 2.5',
                   description='a complex mixture of extremely small particles and liquid droplets; commonly referred to as dust',
                   color=0x809c13)

dust_embed.add_field(name='Effects',
                     value='Inhalation of these particles can cause many issues. Some particles less than 10 micrometers in diameter can get deep into your lungs and some may even get into your bloodstream. Obviously, this poses many health risks.',
                     inline=True)

dust_embed.set_thumbnail(
    url='https://tse4.mm.bing.net/th?id=OIP.KuqzrOkBzbeOF-sKdwvwlQHaFK&pid=Api&P=0&w=258&h=180')

dust_embed.set_footer(text='Powered by Ambee', icon_url=Urls.AMBEE_IMAGE.value)

sulfur_embed = Embed(title=f'Sulfur Dioxide',
                     description='a colorless pungent toxic gas formed by burning sulfur in air',
                     color=0x607c3c)

sulfur_embed.add_field(name='Effects',
                       value='SO2 harms the human respiratory system and increases the amount of PM in the air. It also damages the growth and lifespan of plants.',
                       inline=True)
sulfur_embed.set_thumbnail(
    url='https://tse1.mm.bing.net/th?id=OIP.w_5ISg3AKEV1456SqypPrAHaDq&pid=Api&P=0&w=381&h=188')

sulfur_embed.set_footer(text='Powered by Ambee', icon_url=Urls.AMBEE_IMAGE.value)


class Pollutants:
    pollutants = {"CO": carbon_embed, "NO2": nitrogen_embed, "O3": ozone_embed, "PM10": dust_embed, "PM2.5": dust_embed,
                  "SO2": sulfur_embed}
