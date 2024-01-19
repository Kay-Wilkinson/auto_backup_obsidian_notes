#!/usr/bin/env python3

from git import Repo
import os

def git_commit_push(repo_path, commit_message):
    try:
        repo = Repo(repo_path)

        if repo.is_dirty(untracked_files=True):
            repo.git.add(A=True)

            repo.index.commit(commit_message)

            origin = repo.remote(name='origin')
            origin.push()
            print("Changes pushed to remote repository.")
        else:
            print("No changes to commit.")

    except Exception as e:
        print(f"An error occurred: {e}")


repo_path = '/Users/kaywilkinson/Documents/Obsidian Vault'
commit_message = 'Automated commit to backup notes'
git_commit_push(repo_path, commit_message)
