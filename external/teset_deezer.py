import unittest
import json
import os
import external.deezer as deezer

ENV_FILE = "../env.json"


class DeezerTest(unittest.TestCase):
    def setUp(self):
        with open(ENV_FILE, "r") as file:
            data = json.load(file)
            for key in data:
                os.environ[key] = data[key]

    def test_search_by_artist_and_song(self):
        self.assertEqual(deezer.get_song_data("eminem", "fall").album, "Kamikaze")
        self.assertEqual(deezer.get_song_data("red hot chili peppers", "snow").author, "Red Hot Chili Peppers")


if __name__ == '__main__':
    unittest.main()
