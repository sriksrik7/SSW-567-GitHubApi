import unittest
import requests
import HtmlTestRunner
from hwGitApi import getUserGitHubData
from unittest.mock import patch

class Test_getUserGitHubData(unittest.TestCase):

    # Test Blank data
    def test_getUserGitData(self):
        with patch('requests.get') as mockRequest:
                mockRequest.return_value.status_code = 400
                result = getUserGitHubData('')
        self.assertIsNone(result)

    # Test Invalid data
    def test_getGitInvalidData(self):
        with patch('requests.get') as mockRequest:
                mockRequest.return_value.status_code = 403
                result = getUserGitHubData('234')
        self.assertEqual(result,'Forbidden')

    # Test my git hub data
    def test_getMyUserGitData(self):
        with patch('requests.get') as mockRequest:
                mockRequest.return_value.status_code = 200
                mockRequest.return_value.json.return_value  = [{"name":"HelloWorld"},{"name":"SSW-567"},{"name":"SSW-567-GitHubApi"}]
                result=getUserGitHubData('sriksrik7')
        self.assertEqual(result, ['Repository: HelloWorld has 3 commits',
                                  'Repository: SSW-567 has 3 commits',
                                  'Repository: SSW-567-GitHubApi has 3 commits'])

if __name__ == '__main__':
    print('Run unit tests')
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
