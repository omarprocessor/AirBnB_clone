import unittest
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    """Hii ni test kwa ajili ya darasa la Place"""

    def test_instance(self):
        """Hakikisha kwamba Place ni mfano wa BaseModel"""
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_default_attributes(self):
        """Hakikisha kwamba Place ina sifa za msingi"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_attributes(self):
        """Hakikisha kuwa Place ina sifa zinazohitajika"""
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))
