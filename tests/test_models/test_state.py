import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """Hii ni test kwa ajili ya darasa la State"""

    def test_instance(self):
        """Hakikisha kwamba State ni mfano wa BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_default_name(self):
        """Hakikisha kwamba jina la State linakuwa tupu kwa default"""
        state = State()
        self.assertEqual(state.name, "")

    def test_attributes(self):
        """Hakikisha kuwa State ina sifa zinazohitajika"""
        state = State()
        self.assertTrue(hasattr(state, 'name'))
