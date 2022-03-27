import sqlite3


class WatchList:
    """
    Database for storing what countires users are watching
    """
    def __init__(self):
        self.conn = sqlite3.connect('WatchList.db')
        self.c = self.conn.cursor()

    def insert(self, user_id: int, country: str, region: str):
        with self.conn:
            self.c.execute("""INSERT INTO users VALUES (:id , :country , :region)""", {'id': user_id,
                                                                                       'country': country,
                                                                                       'region': region})

    def add_update(self, user_id: int, country: str, region: str):
        response = self.get_user_by_id(user_id)
        if not response:
            self.insert(user_id, country, region)

    def get_user_by_id(self, user_id):
        with self.conn:
            self.c.execute("""SELECT * FROM users WHERE id=:id""", {'id': user_id})
            response = self.c.fetchall()
            return response

    def remove_user(self, user_id):
        with self.conn:
            self.c.execute("""DELETE from users WHERE id=:id""", {'id': user_id})

    def test_db(self):
        with self.conn:
            self.c.execute("""SELECT * from users""")
            response = self.c.fetchall()
            print(response)

    def get_watches(self):
        """

        :return: list of all users in database with their watches
        """
        with self.conn:
            self.c.execute("""SELECT * from users""")
            response = self.c.fetchall()
            return response
