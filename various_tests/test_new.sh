# !/usr/bin/env bash
REPO=green_garden_bot
if [ -d $REPO ] 
then
    rm -rf  $REPO 
fi
git clone https://obrunet:REdY6w6GPyg3pXJoYnJR@github.com/obrunet/green_garden_bot.git

cd $REPO
touch file.py
echo 'random_stringfffffffffffffff' >> file.py 
git add .
# omit --global to set the identity only in this repository.
git config user.email o.brunet@outlook.com
git config user.name obrunet
git commit -m "Add sdfsdfsd #1"
git push https://obrunet:REdY6w6GPyg3pXJoYnJR@github.com/obrunet/green_garden_bot.git master
