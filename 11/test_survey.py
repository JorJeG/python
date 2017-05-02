import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for class AnonymousSurvey"""

    def setUp(self):
        """Create survey and set of answers for all test methods"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Check that a one response saved correct"""
        self.my_survey.store_response(self.responses[0])

        self.assertIn(self.responses[0], self.my_survey.response)

    def test_store_three_response(self):
        """Check that a three responses saved correct"""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.response)

unittest.main()
