""" Does time series based recommendations based on a lookup table as discussed
by the engine team on Apr 3rd 2014 """

import datetime
import math
import pandas
import stats
import time

table = pandas.read_csv("db/issues.csv", dtype={'age': object, 'gender': object})
table[['age', 'gender']] = table[['age', 'gender']].astype(str)

def process(inputs):
    """ Takes a python structure containing the input data from the REST API and
    returns a list of conditions based on the lookup table"""
    recommendations = []
    
    features = _build_features(inputs)
    dates = _build_dates(inputs)

    age = None
    gender = None
    pills = None

    if 'userinfo' in inputs:
       age = inputs['userinfo']['age']
       gender = inputs['userinfo']['gender']
       pills = inputs['userinfo']['pills']
    
    for _recommendation in table.iterrows():
        recommendation = _recommendation[1]
        # days = int(recommendation['days'])
        feature = recommendation['input'] # use only the last n days
        # values = features[feature][-days:]
        values = features[feature]
        days = dates[feature]
        for index in range(len(values)):
            value = values[index:index+1]
            date = days[index:index+1]
            conditions = [
				# _satisfiesFluctuation(values, recommendation['fluctuation']),
				# _satisfiesGradient(values, recommendation['gradient']),
				_satisfiesLessThen(value, recommendation['less then']),
				_satisfiesMoreThen(value, recommendation['more then']),
				# _satisfiesAvgLess(values, recommendation['avg less']),
				# _satisfiesAvgMore(values, recommendation['avg more']),
				# _satisfiesAge(age, recommendation['age']),
				# _satisfiesGender(gender, recommendation['gender'])
			]
            if all(conditions):
                recommendations.append(_recommendation_output(recommendation, date, feature, pills))
    return recommendations

def _recommendation_output(recommendation, date, feature, pills):
    """ Take in a pandas row and return the format for the output recommendation 
    """
    return {
		'feature': feature,
        'pills' : pills,
        'date' : date[0],
        'category': recommendation['category'],
        'condition': recommendation['condition'],
        'severity' : recommendation['severity']
        }
    
def _satisfiesFluctuation(input_val, fluctuation):
    if math.isnan(fluctuation): return True
    fluctuations = stats.count_fluctuations(input_val)
    return fluctuations >= fluctuation
    return False
    
def _satisfiesGradient(input_val, gradient):
    if math.isnan(gradient): return True
    #TODO: we are not using this right now but use padas or numpy to find
    # gradient using linear regression
    return True
    
def _satisfiesLessThen(input_val, less_then):
    if math.isnan(less_then): return True
    return all([value < less_then for value in input_val])
    
def _satisfiesMoreThen(input_val, more_then):
    if math.isnan(more_then): return True
    return all([value > more_then for value in input_val])
    
def _satisfiesAvgLess(input_val, avg_less):
    if math.isnan(avg_less): return True
    avg = sum(input_val)/len(input_val)
    return avg < avg_less
    
def _satisfiesAvgMore(input_val, avg_more):
    if math.isnan(avg_more): return True
    avg = sum(input_val)/len(input_val)
    return avg > avg_more
    
def _satisfiesAge(userage, age):
    if age == 'nan' or not age or not userage: return True
    return _in_range(userage, age)

def _satisfiesGender(usergender, gender):
    if gender == 'nan' or not gender or not usergender: return True
    inp = usergender.lower()[0] 
    gen = gender.lower()[0]
    return inp == gen

def _in_range(value, range):
    """ Checks if value is in range
    value - numeric value
    range - string in the format 'start_number-end_number'
    """
    min_val, max_val = (int(x) for x in "10-40".split("-"))
    return int(value) > min_val and int(value) < max_val
    
def _build_features(inputs):
    """ Generate dictionary containing a list of data sorted by date for each 
    time series input being used"""
    # Note the preprocessor was not used because it also returns dates
    
    #TODO: Lists should be sorted by date
    bp_systolic = bp_diastolic = pulse = sleep = activity = []

    if "bloodPressures" in inputs:
        bp_systolic = [bp["systolic"] for bp in inputs["bloodPressures"]]
        bp_disastolic = [bp["diastolic"] for bp in inputs["bloodPressures"]]
        bp_date = [bp["date"] for bp in inputs["bloodPressures"]]

    if "heartBeats" in inputs:
        pulse = [value["count"] for value in inputs["heartBeats"]]
        pulse_date = [bp["date"] for bp in inputs["heartBeats"]]

    if "activities" in inputs:
        activity = [value["duration"] for value in inputs["activities"]]
        activity_date = [bp["date"] for bp in inputs["activities"]]
        
    if "sleep" in inputs:
        sleep = [value["minutesAsleep"] for value in inputs["sleep"]]
        sleep_date = [bp["date"] for bp in inputs["sleep"]]
    
    features = {
        'bloodpressure': bp_systolic,
        'pulse': pulse,
        'activity': activity,
        'sleep': sleep,
    }
    return features

def _build_dates(inputs):
    bp_date = pulse_date = activity_date = sleep_date = []

    if "bloodPressures" in inputs:
        bp_date = [bp["date"] for bp in inputs["bloodPressures"]]

    if "heartBeats" in inputs:
        pulse_date = [bp["date"] for bp in inputs["heartBeats"]]

    if "activities" in inputs:
        activity_date = [bp["date"] for bp in inputs["activities"]]
        
    if "sleep" in inputs:
        sleep_date = [bp["date"] for bp in inputs["sleep"]]
    
    dates = {
        'bloodpressure': bp_date,
        'pulse': pulse_date,
        'activity': activity_date,
        'sleep': sleep_date,
    }
    return dates
