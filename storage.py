from discord import Embed


class Storage:
    """
    this should be a database. Too bad!
    Dumb Dumb bad clunky solution to storing all the embed and instances of Pollution objects
    aslong with the output of watch comparisons
    """
    place_embeds = {}
    instances = {}
    watch_data = {}

    @classmethod
    def get_instance(cls, message_id):
        return cls.instances[message_id]

    @classmethod
    def get_place_embed(cls, message_id) -> Embed:
        return cls.place_embeds[message_id]
