import requests
import unittest
from app.commands import get_recent_releases, get_recent_prs
from io import StringIO
from unittest import mock

class TestGitHubCommandLineTool(unittest.TestCase):
    
    # test success response for get_recent_releases from a repo with >= 3 recent releases
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_get_recent_releases_success_0(self, mock_stdout):
        mock_res = mock.Mock()
        mock_res.status_code = 200
        mock_releases = [
            {'tag_name': 'v2.0'},
            {'tag_name': 'v1.1'},
            {'tag_name': 'v1.0'}
        ]
        mock_res.json.return_value = mock_releases

        with mock.patch('requests.get', return_value = mock_res):
            repo, num = 'mock_user/mock_repo', 3
            get_recent_releases(repo, num)

        expected_output = f'Hey! Getting {num} most recent releases from {repo}\n...\n' \
                          f'Here are the 3 most recent releases from {repo}:\n' \
                           'v2.0\n' \
                           'v1.1\n' \
                           'v1.0\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # test success response for get_recent_releases from a repo with < 3 && > 0 recent releases
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_get_recent_releases_success_1(self, mock_stdout):
        mock_res = mock.Mock()
        mock_res.status_code = 200
        mock_releases = [
            {'tag_name': 'v1.1'},
            {'tag_name': 'v1.0'}
        ]
        mock_res.json.return_value = mock_releases

        with mock.patch('requests.get', return_value = mock_res):
            repo, num = 'mock_user/mock_repo', 3
            get_recent_releases(repo, num)

        expected_output = f'Hey! Getting {num} most recent releases from {repo}\n...\n' \
                          f'Here are the 2 most recent releases from {repo}:\n' \
                           'v1.1\n' \
                           'v1.0\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # test success response for get_recent_releases from a repo with 0 recent releases
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_get_recent_releases_success_2(self, mock_stdout):
        mock_res = mock.Mock()
        mock_res.status_code = 200
        mock_releases = []
        mock_res.json.return_value = mock_releases

        with mock.patch('requests.get', return_value = mock_res):
            repo, num = 'mock_user/mock_repo', 3
            get_recent_releases(repo, num)

        expected_output = f'Hey! Getting {num} most recent releases from {repo}\n...\n' \
                          f'{repo} has no releases yet\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # test failed response for get_recent_releases from non-200 status code
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_get_recent_releases_failure_0(self, mock_stdout):
        mock_res = mock.Mock()
        mock_res.status_code = 500
        mock_error_msg = {'message': 'Internal Server Error'}
        mock_res.json.return_value = mock_error_msg

        with mock.patch('requests.get', return_value = mock_res):
            repo, num = 'mock_user/mock_repo', 3
            get_recent_releases(repo, num)

        expected_output = f'Hey! Getting {num} most recent releases from {repo}\n...\n' \
                          f'Error fetching releases for repository: {repo}\n' \
                           'Error message: Internal Server Error\n' \
                           'Please make sure the repo input follows the format {repo_owner}/{repo_name} and the repository is public\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # test success response for get_recent_pr from a repo with >= 3 recent pull requests
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_get_recent_prs_success_0(self, mock_stdout):
        mock_res = mock.Mock()
        mock_res.status_code = 200
        mock_prs = [
            {'number': '10', 'title': 'Add cool features'},
            {'number': '9', 'title': 'Fix cool bugs'},
            {'number': '8', 'title': 'Implement cool integrations'},
        ]
        mock_res.json.return_value = mock_prs

        with mock.patch('requests.get', return_value = mock_res):
            repo, num = 'mock_user/mock_repo', 3
            get_recent_prs(repo, num)

        expected_output = f'Hey! Getting {num} most recent pull requests from {repo}\n...\n' \
                          f'Here are the 3 most recent pull requests from {repo}:\n' \
                           'PR#10 Add cool features\n' \
                           'PR#9 Fix cool bugs\n' \
                           'PR#8 Implement cool integrations\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # test success response for get_recent_prs from a repo with < 3 && > 0 recent pull requests
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_get_recent_prs_success_1(self, mock_stdout):
        mock_res = mock.Mock()
        mock_res.status_code = 200
        mock_prs = [
            {'number': '2', 'title': 'Add cool features'},
            {'number': '1', 'title': 'Fix cool bugs'}
        ]
        mock_res.json.return_value = mock_prs

        with mock.patch('requests.get', return_value = mock_res):
            repo, num = 'mock_user/mock_repo', 3
            get_recent_prs(repo, num)

        expected_output = f'Hey! Getting {num} most recent pull requests from {repo}\n...\n' \
                          f'Here are the 2 most recent pull requests from {repo}:\n' \
                           'PR#2 Add cool features\n' \
                           'PR#1 Fix cool bugs\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # test success response for get_recent_prs from a repo with 0 recent pull requests
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_get_recent_prs_success_2(self, mock_stdout):
        mock_res = mock.Mock()
        mock_res.status_code = 200
        mock_prs = []
        mock_res.json.return_value = mock_prs

        with mock.patch('requests.get', return_value = mock_res):
            repo, num = 'mock_user/mock_repo', 3
            get_recent_prs(repo, num)

        expected_output = f'Hey! Getting {num} most recent pull requests from {repo}\n...\n' \
                          f'{repo} has no pull requests yet\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # test failed response for get_recent_prs from non-200 status code
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_get_recent_prs_failure_0(self, mock_stdout):
        mock_res = mock.Mock()
        mock_res.status_code = 500
        mock_error_msg = {'message': 'Internal Server Error'}
        mock_res.json.return_value = mock_error_msg

        with mock.patch('requests.get', return_value = mock_res):
            repo, num = 'mock_user/mock_repo', 3
            get_recent_prs(repo, num)

        expected_output = f'Hey! Getting {num} most recent pull requests from {repo}\n...\n' \
                          f'Error fetching pull requests for repository: {repo}\n' \
                           'Error message: Internal Server Error\n' \
                           'Please make sure the repo input follows the format {repo_owner}/{repo_name} and the repository is public\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()