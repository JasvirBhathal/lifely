import unittest
import pprint
import fixtures
import recommender

pp = pprint.PrettyPrinter(indent=4)

class TestRecommender(unittest.TestCase):
    
    def test_recommender(self):
        print "============================="
        print "Recommendations for high sleep high activities"
        print "============================="
        pp.pprint(recommender.recommend(fixtures.input))


    def test_condition9(self):
        print "============================="
        print "Recommendations for Bloodpressure high"
        print "============================="
        pp.pprint(recommender.recommend(fixtures.input9))

        
    def test_condition53(self):
        print "============================="
        print "Recommendations for Low activity"
        print "============================="
        pp.pprint(recommender.recommend(fixtures.input53))

        
    def test_condition72(self):
        print "============================="
        print "Recommendations for Too much sleep"
        print "============================="
        
        pp.pprint(recommender.recommend(fixtures.input72))
