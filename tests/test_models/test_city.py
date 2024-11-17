import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """Hii ni test kwa ajili ya darasa la City"""

    def test_instance(self):
        """Hakikisha kwamba City ni mfano wa BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_default_state_id(self):
        """Hakikisha kwamba state_id la City linakuwa tupu kwa default"""
        city = City()
        self.assertEqual(city.state_id, "")

    def test_default_name(self):
        """Hakikisha kwamba jina la City linakuwa tupu kwa default"""
        city = City()
        self.assertEqual(city.name, "")

    def test_attributes(self):
        """Hakikisha kuwa City ina sifa zinazohitajika"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
