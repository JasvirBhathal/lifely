""" Recommendation engine. Takes input as a python object of the format
described in the API and returns a python object with recommendations in the
format described by the API. """
"""
temporily comment the instance_recommendations out for testing
"""

import issue_checker
import issue_picker

def recommend(input):
    issues = issue_checker.process(input)
    suggestions = issue_picker.process(issues)
    return suggestions
