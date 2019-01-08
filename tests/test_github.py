import unittest

from github import query


class QueryTestCase(unittest.TestCase):
    def test_query(self):
        q = """
        query {
          meta { 
            gitHubServicesSha 
          }
        }
        """

        self.assertIsNotNone(query(q))
