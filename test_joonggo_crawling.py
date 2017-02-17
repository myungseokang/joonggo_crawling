from joonggo_crawling import get_response_text
import unittest


class JoonggoCrawlingTest(unittest.TestCase):

    def test_get_response_with_correct_url(self):
        test_response = get_response_text(url='http://www.naver.com')
        self.assertEqual(test_response.__class__, ''.__class__)

    def test_get_response_with_wrong_url(self):
        self.assertEqual(get_response_text(url='http://sdlfkhndslkgjipoqenfkldsf.com'), 'Connection Failed!')


if __name__ == '__main__':
    unittest.main()
