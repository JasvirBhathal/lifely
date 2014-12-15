""" Recommendation engine. Takes input as a python object of the format
described in the API and returns a python object with recommendations in the
format described by the API. """
"""
temporily comment the instance_recommendations out for testing
"""

import issue_checker
import issue_picker
import issue_recommend

def recommend(input):
    issues = issue_recommend.process(input)
    suggestions = issue_picker.process(issues)
    recommend = issue_checker.process(input)
    recommendations = issue_picker.category(recommend)
    suggestions.extend(recommendations)
    return suggestions
