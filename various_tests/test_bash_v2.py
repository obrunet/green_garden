# simple test to show how to run a bash command from python without saving a script file
import os

command = os.popen('ls -al')
print(command.read())
print(command.close())


repo, username = "test_repo_it_works", "test_user"
sh_script = (f"""# !/usr/bin/env bash
REPO={repo}
touch file.py
echo 'it_works!!' >> file.py
echo $REPO >> file.py
echo {username}
""")
command = os.popen(sh_script)
command.read()
command.close()