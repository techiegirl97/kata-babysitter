# Babysitter Kata

## Background
This kata simulates a babysitter working and getting paid for one night.  The rules are pretty straight forward.

The babysitter:
- starts no earlier than 5:00PM
- leaves no later than 4:00AM
- gets paid $12/hour from start-time to bedtime
- gets paid $8/hour from bedtime to midnight
- gets paid $16/hour from midnight to end of job
- gets paid for full hours (no fractional hours)


## Feature
*As a babysitter<br>
In order to get paid for 1 night of work<br>
I want to calculate my nightly charge<br>*

## Prerequisites
You must have Python 3.6.4 installed to run this script. If you want to run the unit test, you will need to install PyTest.

To install PyTest run:

python -m pip install pytest

## Usage
The program will prompt the user for 3 parameters.
First, enter the Start Time of work.
Second, enter the work Stop Time/end of night.
Last, enter the Bedtime. 

The algorithm will calculate pay for one night of work.

**To run the script:**

python \your path to script\calculate.py

## Unit Tests

You will need to have Pytest installed with your Python to run the tests.

**To install Pytest, run:**

pip install -U pytest

or

python -m pip install pytest

**To run the unit tests:**

python -m pytest

or 

python -m pytest -v -s \your path to script\test_workdays.py



