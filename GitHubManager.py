from github import Github, GithubException
import os

class GitHubManager:
    def __init__(self, token, repo_name):
        self.github = Github(token)
        try:
            self.repo = self.github.get_user().get_repo(repo_name)
            print(f"Repository {repo_name} already exists, using existing repository.")
        except Exception:
            self.repo = self.github.get_user().create_repo(repo_name)
            print(f"Repository {repo_name} created.")
    
    def commit_file(self, file_path, content, commit_message):
        with open(file_path, 'w') as f:
            f.write(content)
        self.repo.create_file(file_path, commit_message, content)
    
    def read_file(self, file_path):
        return self.repo.get_contents(file_path).decoded_content.decode()

    def get_contents(self, file_path):
        return self.repo.get_contents(file_path)

    def update_file(self, file_path, commit_message, content, sha):
        self.repo.update_file(file_path, commit_message, content, sha)

    def create_file(self, file_path, commit_message, content):
        self.repo.create_file(file_path, commit_message, content)

    @property
    def GithubException(self):
        return GithubException