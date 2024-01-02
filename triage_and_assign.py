# triage_and_assign.py

from github import Github
import os

def triage_and_assign(repo, issue):
    # Add your triaging and assignment logic here
    # For example, you can check issue labels, content, etc., and assign it accordingly
    labels = issue.labels
    assignees = [repo.get_user("ErArif01")]  # Replace "username" with the desired GitHub username

    # Add your triaging and assignment logic here based on issue labels, content, etc.

    # Assign the issue
    issue.edit(assignees=assignees)

if __name__ == "__main__":
    # Example of usage
    repository_name = "jack"
    issue_number = 1 

    github_token = os.getenv("GITHUB_TOKEN")
    g = Github(github_token)
    repo = g.get_repo(repository_name)
    issue = repo.get_issue(issue_number)

    triage_and_assign(repo, issue)
