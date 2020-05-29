import unittest
from unittest.mock import patch
import json
from os import path
from secretary import update_date, add_new_shelf, add_new_doc, move_doc_to_shelf

documents = []
directories = {}


@patch('secretary.documents', documents, create=True)
@patch('secretary.directories', directories, create=True)
class SecretaryTest(unittest.TestCase):
    def setUp(self):
        current_path = path.abspath('.')
        p_dirs = path.join(current_path, 'fixtures', 'directories.json')
        p_docs = path.join(current_path, 'fixtures', 'documents.json')

        with open(p_dirs, 'r', encoding='utf-8') as dirs:
            directories.update(json.load(dirs))
        with open(p_docs, 'r', encoding='utf-8') as docs:
            documents.extend(json.load(docs))

    def test_update_data(self):
        update_date()
        self.assertGreater(len(documents), 0)
        self.assertGreater(len(directories), 0)

    def test_add_new_shelf(self):
        start_len = (len(directories))
        test_value = '12'
        self.assertNotIn(test_value, directories.keys())
        add_new_shelf(test_value)
        self.assertNotEqual(start_len, len(directories))

    def test_move_doc_to_shelf(self):
        doc = '2207 876234'
        test_shelf = '3'
        self.assertIn(doc, [document['number'] for document in documents])
        with patch('secretary.input', side_effect=[doc, test_shelf]):
            move_doc_to_shelf()
        self.assertIn(doc, directories[test_shelf])

    def test_move_non_existing_doc_to_shelf(self):
        non_exist_doc = 'несуществующий документ'
        test_shelf = '3'
        self.assertNotIn(non_exist_doc, [document['number'] for document in documents])
        with patch('secretary.input', side_effect=[non_exist_doc, test_shelf]):
            move_doc_to_shelf()
        self.assertIn(non_exist_doc, directories[test_shelf])

    def test_add_new_document(self):
        with patch('secretary.input',
                   side_effect=['7005 808598', 'passport', 'Pupkin Ivan', '1']):
            result = add_new_doc()
        self.assertIn('7005 808598', directories['1'])
        self.assertEqual(result, '1')
