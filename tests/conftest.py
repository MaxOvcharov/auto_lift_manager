import logging
import os
import sys

os.environ['PYTHONLOGGINLEVEL'] = str(logging.DEBUG)
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

pytest_plugins = ['lift_fixtures']
