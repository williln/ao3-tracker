# ao3-tracker

Making my dream AO3 text-to-Notion pipeline 

This project uses: 

- Python 3.10 
- Django 4.1

## What is this? 

This is all [Simon's](https://twitter.com/simonw) fault, is what it is. 

I have a fear of coding in public! Coding for work? No problem. Constructive feedback on PRs? Bring it on. But personal projects? Eh, that seems pretty scary. 

But I also read a *lot* of fanfiction, and I have yet to cobble together a way to keep track of the things I am reading, the things I want to read, and the things I have read. [AO3](https://archiveofourown.org/) is the platform I read most works on, but it doesn't have an app or an API, and its built-in tools for keeping track of all this stuff don't meet my needs. 

So I'm going to build something. Simon gave an [awesome talk at DjangoCon US 2022 about personal projects](https://github.com/simonw/djangocon-2022-productivity) that really inspired me to get over myself, work in public, and build the thing I want. 

# Local Development 

Copy `env.template` to a local `.env` file 

    cp env.template .env 

# Just Commands

I use [just](https://github.com/casey/just) to help standardize working with
this project. If you don't have it installed, for MacOS, run `brew install just`.

To help manage dependencies, this project uses:
-  Docker and [docker-compose](https://docs.docker.com/compose/reference/overview/) to maintain a consistent development/runtime environment
-  [pip-tools](https://pypi.org/project/pip-tools/) to help dependencies stay up to date IN that environment

The summaries here are for basic "what/when" guideance. Please read `Justfile` or the  documentation for a specific package if more detail is needed.

## just pip-compile
Creates a `web` container, running `pip-compile` inside it. This creates a fresh `requirements.txt` based on `requirements.in`.
This should be run after changes are made to the `requirements.in`(so, each time a package the project depends on is added, removed, or changed). Please see the `pip-tools` documentation for more detail on `pip-compile` and related tools.

## just rebuild
Removes the `web` container, then rebuilds `web`.
This should be used after each `just pip-compile`, as the project dependencies should have changed.

## just shell
Provides a bash prompt insided the `web` container. Useful for debugging and manual testing/investigation.

## just django-shell
Same as above but with `python manage.py shell` added, so you can start trying Django things more easily.

## just test
Runs `pytest` and `interrogate` in the `web` container.  Please: write, run, and document your tests.

## just coverage

Runs `pytest` generating an HTML coverage report and opens it in your local browser.

## just {makemigrations or migrate}
Runs the corresponding [Django command](https://docs.djangoproject.com/en/3.0/topics/migrations/) in the `web` container.

Migrations are "_Django’s way of propagating changes you make to your models_", so these commands should be run then.

## just lint
Runs `black .` to format the codebase. 

# Can I help? 

This repo is technically open source, but y'all... I know myself. I'm going work on this as I have time. I suck at responding to PRs and issues for non-work projects. So please don't PR to this repo, because your PR will languish for too long and it will frustrate you how uncommunicative I am. Don't say I didn't warn you. 

Anyway, maybe this will be my last commit to this project! Who knows! I'm doing this for fun and you're welcome to follow along. 

