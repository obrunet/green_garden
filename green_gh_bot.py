# Coded by Olivier Brunet, 2020 -  released under the GNU General Public License (GPL)
# that guarantees end users the freedom to run, study, share, and modify this piece of code.


"""
This python 3 script automates a random number of commits on a daily basis in order to turn your GitHub page green
it uses bash commands, in a future version github APIs will be added.

HOW TO:
    - First, you've to clone a private repository in the same folder where this script is run.
    - It checks if the configuration file is correct, otherwise creates it based on user inputs (user & repo names)
    - It also prompt the user for the github password (this password is erased at the end and not saved).
    - Crontab -----------------------

ALTERNATIVES:
    - An other version with more professional options (see the non-free edition)
        https://github.com/alexandersideris/github-gardener-bot
    - Using selenium webdriver :
        https://github.com/rehasantiago/Green-Garden/blob/master/commits.py
    - A complete bot that greets the person who created issues and thanks them when a pull request has been closed:
        https://github.com/Mariatta/github-bot-tutorial
    - If you want some nice ascii art:
        https://github.com/gelstudios/gitfiti
"""


import configparser
import os.path
import requests
from requests.exceptions import HTTPError
import subprocess
from random import randint
import time


CONFIG_FILE = 'config.ini'
GITHUB_BASE_URL = 'https://github.com/'


def request_web_page(url):
    """Make a request for a specific URL, returns False if the web page doesn't exist"""
    try:
        req_response = requests.get(url)
        req_response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return False
    except Exception as err:
        print(f'Other error occurred: {err}')
        return False
    else:
        return True


def verify_user_repo(username, repo):
    """Check if the username exists, and if repo is public or private"""
    if request_web_page(GITHUB_BASE_URL + username):
        if request_web_page(GITHUB_BASE_URL + username + '/' + repo):
            print("This repository seems to be public. Advice: make it private so that commits can't be seen...")
        return True
    else:
        print("This username doesn't exist... Recreating a config file")
        return False


def get_user_infos():
    """Ask user for his/her username, name of the repo, and password"""
    username = input('Enter your GitHub username: ')
    repo = input('Enter the name of the repository where commits will be made: ')
    email = input('Enter your email associated with your github account (otherwise commits won\'t be counted): ')
    return username, repo, email


def create_config():
    """Create a configuration file based on the user inputs (username, repo's name"""
    username, repo, email = get_user_infos()
    verify_user_repo(username, repo)
    config = configparser.ConfigParser()
    config['Github'] = {'Username': username, 'Repo': repo, 'Email': email}
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)


def read_config():
    """Read the configuration file and return the infos it holds"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    if 'Github' not in config.sections():
        print('No configuration for GitHub... The config file is malformed... Recreating it !')
        return False, False
    username, repo, email = config['Github']['Username'],  config['Github']['Repo'], config['Github']['Email']
    return username, repo, email


def make_commit(username, repo, pw, email="you@example.com", commit_msg="Update README.md"):
    """Launch bash commands to make commits"""
    sh_script = (f"""
            # !/usr/bin/env bash
            REPO={repo}
            if [ -d $REPO ] 
            then
                rm -rf  $REPO 
            fi
            git clone https://{username}:{pw}@github.com/{username}/{repo}.git  
            cd $REPO
            touch file.py
            echo '{randint(0, 1000)}' > file.py 
            git add .
            # omit --global to set the identity only in this repository.
            git config user.email {email}
            git config user.name {username}
            git commit -m "{commit_msg}"
            git push https://{username}:{pw}@github.com/{username}/{repo}.git master
            """)
    # execute the bash commands
    output = subprocess.check_output(['bash', '-c', sh_script])


def fake_commit_msg():
    """Choose randomly in a list & return a msg for your commit"""
    fake_md_files = ['README', 'doc', 'translation', 'references', 'how_to', 'goals', 'todo' ]
    fake_py_files = ['main', 'sockets', 'network', 'django', 'flask', 'strings', 'calculation', 'machine_learning',
                     'tensorflow_model', 'scikit_model', 'metric', 'plots', 'data_visualization']
    messages = ['Initial commit',
                f'Update {fake_md_files[randint(0, len(fake_md_files)-1)]}.md',
                f'Add {fake_py_files[randint(0, len(fake_py_files)-1)]}.py',
                'Fix broken links / typo errors',
                'Translation made more accurate',
                'Reorganize folders and files',
                f'Add documentation for chapter #{randint(1, 5)}',
                'Translation update',
                f'Refactor code of {fake_py_files[randint(0, len(fake_py_files)-1)]} for readability',
                f'Remove deprecated methods in {fake_py_files[randint(0, len(fake_py_files)-1)]}',
                f'Release version {randint(0, 4)}.{randint(0, 6)}.{randint(0, 10)}',
                f'Merge pull request #{randint(0, 50)} from user/branch',
                'Update homepage for launch']
    return messages[randint(0, len(messages)-1)]


def main():
    # if no configuration file, creates it
    if not os.path.isfile(CONFIG_FILE):
        create_config()
        # add startup method to launch script -------------------------------------------

    # check if the configuration is correct
    username, repo, email = read_config()
    if not username or not verify_user_repo(username, repo):
        create_config()

    # prompt user for pw then remove it at the end for security reasons
    pw = input('Enter your GitHub password: ')

    # check nb of commits already made yesterday & today: ---------------------------------------

    # determine nb of commits that will be automatically made by the script
    print(username, repo, pw, email, fake_commit_msg())
    for _ in range(1, randint(1, 25)):
        make_commit(username, repo, pw, email, fake_commit_msg())
        time.sleep(randint(0, 10))
    pw = "Erase Password in Memory for Security Reasons"


if __name__ == '__main__':
    main()