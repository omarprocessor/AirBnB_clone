import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Hii ni test kwa ajili ya darasa la Amenity"""

    def test_instance(self):
        """Hakikisha kwamba Amenity ni mfano wa BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_default_name(self):
        """Hakikisha kwamba jina la Amenity linakuwa tupu kwa default"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_attributes(self):
        """Hakikisha kuwa Amenity ina sifa zinazohitajika"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
