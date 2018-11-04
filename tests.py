import datetime
import unittest

from notebook import Note


class TestNote(unittest.TestCase):
    def test_create(self):
        """Note must have id, memo, tags (optional), creation date"""
        note = Note('any memo', tags='one two')
        self.assertIsNotNone(note.id)
        self.assertIsNotNone(note.memo)
        self.assertIsNotNone(note.tags)
        self.assertIsInstance(note.creation_date, datetime.datetime)

    def test_create_different(self):
        """Notes must have different ids and creation dates"""
        n1 = Note('first')
        n2 = Note('second')
        self.assertNotEqual(n1.id, n2.id)
        self.assertNotEqual(n1.creation_date, n2.creation_date)

    def test_match(self):
        """Note must match string present in its memo and tags"""
        n1 = Note('first note', 'one')
        self.assertTrue(n1.match('first'))
        self.assertTrue(n1.match('note'))
        self.assertTrue(n1.match('one'))

    def test_match_bad(self):
        """Must not match when filter is not present in memo or tags"""
        n1 = Note('first note', 'one')
        self.assertFalse(n1.match('second'))
        self.assertFalse(n1.match('two'))
        self.assertFalse(n1.match('notebook'))
