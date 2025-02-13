# test_python_repos.py
import unittest
import requests

class TestPythonRepos(unittest.TestCase):

    def setUp(self):
        """Set up the test with the API request and store the response."""
        url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
        self.response = requests.get(url)
        self.response_data = self.response.json()

    def test_status_code(self):
        """Test if the response status code is 200."""
        self.assertEqual(self.response.status_code, 200, "Status code is not 200")

    def test_number_of_items(self):
        """Test that the number of items returned is 30 (default per page for GitHub API)."""
        self.assertEqual(len(self.response_data['items']), 30, "Number of items is not 30")

    def test_total_repositories(self):
        """Test that the total number of repositories is greater than a specified value."""
        total_repositories = self.response_data['total_count']
        self.assertGreater(total_repositories, 1000000, "Total repositories are not greater than 1,000,000")

    def test_items_structure(self):
        """Test that each repository item has specific keys like 'name', 'owner', and 'html_url'."""
        for repo in self.response_data['items']:
            self.assertIn('name', repo, "Key 'name' not found in repository data")
            self.assertIn('owner', repo, "Key 'owner' not found in repository data")
            self.assertIn('html_url', repo, "Key 'html_url' not found in repository data")

if __name__ == "__main__":
    unittest.main()
