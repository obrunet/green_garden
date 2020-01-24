# Working example
import subprocess


def main():
    """Create a bash script and launch it """
    repo, username = "test_repo", "test_user"
    sh_script = (f"""# !/usr/bin/env bash
REPO={repo}
touch file.py
echo 'random_string' >> file.py
echo $REPO >> file.py
echo {username}
""")
    output = subprocess.check_output(['bash', '-c', sh_script])


if __name__ == '__main__':
    main()