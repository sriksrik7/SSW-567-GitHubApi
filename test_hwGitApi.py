import unittest
import requests
import HtmlTestRunner
from hwGitApi import getUserGitHubData

class Test_getUserGitHubData(unittest.TestCase):

    # Test Blank data
    def test_getUserGitData(self):
        self.assertIsNone(getUserGitHubData(''))

    # Test Invalid data
    def test_getGitInvalidData(self):
        self.assertIsNotNone(getUserGitHubData('234'))

    # Test my git hub data
    def test_getMyUserGitData(self):
        result=getUserGitHubData('sriksrik7')
        self.assertEqual(result, ['Repository: HelloWorld has 2 commits',
                                  'Repository: SSW-567 has 6 commits',
                                  'Repository: SSW-567-GitHubApi has 4 commits'])

if __name__ == '__main__':
    print('Run unit tests')
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
