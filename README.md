>#clicv

# Overview
This is a small Uber Hacks university hackathon project. `clicv` allows you to create an interactive cli with your resume

# Prerequisites/Requirements
See requirements.txt; this project was built with Click: http://click.pocoo.org/5/

# Installing
1. clone this repo (`git clone https://github.com/loyaltyarm/uberhacks-clicv.git`)
2. `pip install virtualenv`
3. `cd uberhacks-clicv`
4. `virtualenv venv`
5. `. venv/bin/activate`
6. `pip install --editable .`
7. `clicv --help`

# Usage
```
$ clicv --help
Usage: clicv [OPTIONS]

  clicv enables my resume as an interactive command line tool

Options:
  --certifications  See a list of my certifications.
  --education       See my educational achievements.
  --experience      Print a list of my past/present companies and roles.
  --patents         Check out my patents!
  --skills          Check out my key skills.
  --help            Show this message and exit.
```

# Future enhancements
- Don't hardcode resume results, pull from an API like Angelist or LinkedIn
- Accept multiple arguments at once, like an `--all` command that will dump the entire resume

# Acknowledgements
@dawsbot
@AnaMMedina21
Uber University Recruiting team!

