import unittest
import json
import os
import external.audd as audd

ENV_FILE = "../env.json"


class AuddTests(unittest.TestCase):
    def setUp(self):
        with open(ENV_FILE, "r") as file:
            data = json.load(file)
            for key in data:
                os.environ[key] = data[key]

    def test_search_by_lyrics(self):
        self.assertEqual(audd.search_by_lyrics("one way ticket").song, 'One Way Ticket')


if __name__ == '__main__':
    unittest.main()
