import unittest
from yandex_translate import translate_en_ru


class YaTranslatorAPITestCase(unittest.TestCase):
    def test_translation_request(self):
        source_text = 'python'
        result = translate_en_ru(source_text)
        self.assertEqual(result['text'][0], 'питон')

    def test_request_problems(self):
        source_text = 'Hi'
        result = translate_en_ru(source_text)
        self.assertEqual(result['code'], 200)

    @unittest.expectedFailure
    def test_target_language_is_not_ru(self):
        source_text = 'Bonjour'
        result = translate_en_ru(source_text)
        self.assertEqual(result['text'][0], 'Привет')



if __name__ == '__main__':
    unittest.main()