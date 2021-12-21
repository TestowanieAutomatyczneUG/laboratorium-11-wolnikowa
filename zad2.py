import unittest

from unittest.mock import MagicMock


class NotesStorage(object):
    def __init__(self):
        self.notes = []

    def add(self, note):
        pass

    def clear(self):
        pass

    def getAllNotesOf(self, name):
        pass



class TestNotesStorage(unittest.TestCase):
    def test_notes_storage_add_not_note(self):
        notes_storage = NotesStorage()
        notes_storage.add = MagicMock(side_effect=TypeError)

        self.assertRaises(TypeError, notes_storage.add, 12332)

    def test_notes_storage_add_note_success(self):
        notes_storage = NotesStorage()
        notes_storage.add = MagicMock(return_value="Note added")

        self.assertEqual(notes_storage.add(1), "Note added")

    def test_notes_storage_clear(self):
        notes_storage = NotesStorage()
        notes_storage.clear = MagicMock(return_value="cleared notes")

        self.assertEqual(notes_storage.clear(), "cleared notes")

    def test_notes_storage_get_all_notes_of_non_existent(self):
        notes_storage = NotesStorage()
        notes_storage.getAllNotesOf = MagicMock(side_effect=ValueError)

        self.assertRaises(ValueError, notes_storage.getAllNotesOf, "Andrzej")

    def test_notes_storage_get_all_notes_of_successful(self):
        notes_storage = NotesStorage()
        notes_storage.getAllNotesOf = MagicMock(return_value=[1, 2, 3, 4])

        self.assertEqual(notes_storage.getAllNotesOf("Andrzej"), [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()