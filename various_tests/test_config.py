import configparser
import os.path
import requests
from requests.exceptions import HTTPError


CONFIG_FILE = 'config.ini'
GITHUB_BASE_URL = 'https://github.com/'


def get_user_infos():
    """Ask user for his/her username, name of the repo, and password"""
    username = input('Enter your GitHub username: ')
    repo = input('Enter the name of the repository where commits will be made: ')
    return username, repo


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


def create_config():
    """Create a configuration file based on the user inputs (username, repo's name"""
    username, repo = get_user_infos()
    verify_user_repo(username, repo)
    config = configparser.ConfigParser()
    config['Github'] = {'Username': username, 'Repo': repo}
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)
    print("Warning: do not share or release this configuration file publicly as it contents sensitive infos !")


def read_config():
    """Read the configuration file and return the infos it holds"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    if 'Github' not in config.sections():
        print('No configuration for GitHub... The config file is malformed... Recreating it !')
        return False, False
    username, repo = config['Github']['Username'],  config['Github']['Repo']
    return username, repo


def main():
    # if no configuration file, creates it
    if not os.path.isfile(CONFIG_FILE):
        create_config()
        ############################## add startup method to launch script

    # check if the configuration is correct
    username, repo = read_config()
    if not username or not verify_user_repo(username, repo):
        create_config()

    # check if commits have already been made today, if not make some:


if __name__ == '__main__':
    main()



