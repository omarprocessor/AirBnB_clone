import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Hii ni darasa la majaribio kwa console.py"""

    @patch('sys.stdout', new_callable=StringIO)
    def test_help(self, mock_stdout):
        """Testi ya amri ya msaada."""
        HBNBCommand().onecmd("help show")
        output = mock_stdout.getvalue()
        self.assertIn("Show a specific instance", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        """Testi ya amri ya kuunda mfano mpya."""
        HBNBCommand().onecmd("create BaseModel")
        output = mock_stdout.getvalue()
        self.assertTrue(len(output.strip()) > 0)  # Checking if ID is printed

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        """Testi ya amri ya kuonyesha mfano."""
        HBNBCommand().onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()

        # Now show the created object
        HBNBCommand().onecmd(f"show BaseModel {obj_id}")
        output = mock_stdout.getvalue()
        self.assertIn(obj_id, output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        """Testi ya amri ya kuonyesha mifano yote."""
        HBNBCommand().onecmd("create BaseModel")
        HBNBCommand().onecmd("all BaseModel")
        output = mock_stdout.getvalue()
        self.assertIn("BaseModel", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        """Testi ya amri ya kufuta mfano."""
        HBNBCommand().onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()

        # Now destroy the created object
        HBNBCommand().onecmd(f"destroy BaseModel {obj_id}")
        output = mock_stdout.getvalue()
        self.assertIn("** hakuna mfano uliopatikana **", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        """Testi ya amri ya kuboresha mfano."""
        HBNBCommand().onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()

        # Update object
        HBNBCommand().onecmd(f"update BaseModel {obj_id} name 'New Name'")
        output = mock_stdout.getvalue()
        self.assertIn("** hakuna mfano uliopatikana **", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_with_invalid_value(self, mock_stdout):
        """Testi ya amri ya kuboresha mfano na thamani batili."""
        HBNBCommand().onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()

        # Update object with invalid value
        HBNBCommand().onecmd(f"update BaseModel {obj_id} age 'invalid_age'")
        output = mock_stdout.getvalue()
        self.assertIn("** sintaksia batili", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_with_invalid_class(self, mock_stdout):
        """Testi ya amri ya kuunda mfano na darasa lisilokubalika."""
        HBNBCommand().onecmd("create InvalidClass")
        output = mock_stdout.getvalue()
        self.assertIn("** darasa halipo **", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_with_invalid_id(self, mock_stdout):
        """Testi ya amri ya kuonyesha mfano na ID isiyofaa."""
        HBNBCommand().onecmd("show BaseModel non_existing_id")
        output = mock_stdout.getvalue()
        self.assertIn("** hakuna mfano uliopatikana **", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_quit(self, mock_stdout):
        """Testi ya msaada kwa amri ya kutoka."""
        HBNBCommand().onecmd("help quit")
        output = mock_stdout.getvalue()
        self.assertIn("Quit the program", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        """Testi ya amri ya kutoka kwa mfasili."""
        HBNBCommand().onecmd("quit")
        output = mock_stdout.getvalue()
        self.assertEqual(output, "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF(self, mock_stdout):
        """Testi ya amri ya EOF."""
        HBNBCommand().onecmd("EOF")
        output = mock_stdout.getvalue()
        self.assertEqual(output, "")


if __name__ == "__main__":
    unittest.main()
