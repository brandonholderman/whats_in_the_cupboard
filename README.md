# whats_in_the_cupboard

**Author**: Brandon Holderman

**Version**: 0.0.1

## Overview
What's in the cupboard is a wesbite giving users the ability to enter in food items they have at home and the Edamam recipe API will return results that include those items.

## Getting Started
Eventually this will simply be a URL that you can go to to use the website.
For developer use:
1. clone this repo
2. create a database in postgres called `cupboard_db`
3. create a virtualenv, once inside the virtualenv run `pip install -r requirements.txt`. You must be in the directory with the requirements.txt for this to work.
4. start the server by running `./manage.py runserver`
5. visit your localhost port 8000 to interact with the site
6. to create a superuser run `./manage.py createsuperuser` and add in your credentials.

## Architecture
This application utilizes the Django web framework, PostgreSQL for its database and the Edamam Recipe API

## Change Log
* 09-01-2019 - created templates, added styling, created models
