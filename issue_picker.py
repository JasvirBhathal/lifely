import random
import time
from collections import defaultdict

def process(issues):
    """ Finds the highest severity issue for each category that has an issue """
    # group issues by state
    issues_by_category = defaultdict(list)
    for issue in issues:
        issues_by_category[issue['category']].append(issue)
    # select issues with highest priority
    # top_issues = [highest_severity_issue(issues) 
                  # for category, issues in issues_by_category.items()]
    top_issues = [issue for issue in issues
                  if issue['severity'] != 0]
    
    return top_issues

def category(issues):
    issues_by_category = defaultdict(list)
    for issue in issues:
        issues_by_category[issue['category']].append(issue)
    # select issues with highest priority
    top_issues = [highest_severity_issue(issues) 
                  for category, issues in issues_by_category.items()]
    return top_issues
    
def highest_severity_issue(issues):
    """ Selects an issue with the highest severity for a list of issues expects
    a list of dictionaries containing the issues in the same category"""
    max_severity = max([issue['severity'] for issue in issues])
    filtered_issues = [issue for issue in issues 
                       if issue['severity'] == max_severity]
    # since the issues are in the same category, they are very similar and
    # if there are more than more a random one can safely be selected
    selected_issue = random.choice(filtered_issues)
    return selected_issue