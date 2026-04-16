from github import Github
from config import GITHUB_TOKEN

class GitHubClient:
    def __init__(self):
        self.client = Github(GITHUB_TOKEN)

    def get_repo_details(self, repo_name):
        repo = self.client.get_repo(repo_name)
        return {
            "name": repo.name,
            "description": repo.description,
            "stars": repo.stargazers_count,
            "files": [f.path for f in repo.get_contents("")]
        }
