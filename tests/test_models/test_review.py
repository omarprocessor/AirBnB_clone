import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Hii ni test kwa ajili ya darasa la Review"""

    def test_instance(self):
        """Hakikisha kwamba Review ni mfano wa BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_default_attributes(self):
        """Hakikisha kwamba Review ina sifa za msingi"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_attributes(self):
        """Hakikisha kuwa Review ina sifa zinazohitajika"""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))
