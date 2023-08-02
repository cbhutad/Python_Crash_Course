import unittest
from anonymous import Anonymous

class TestAnonymous(unittest.TestCase):

    def setUp(self):
        """Setups a object and other test data required by test methods"""
        question = "What are the languages do you know ?"
        self.survey = Anonymous(question)
        self.responses = ["lang1", "lang2", "lang3"]

        for response in self.responses:
            self.survey.store_response(response)

    def test_single_response_storage(self):
        """tests whether single response submitted is stored properly"""
        self.assertIn(self.responses[2], self.survey.responses)

    def test_multiple_response_storage(self):
        """tests whether multiple response submitted are stored properly"""
        for response in self.responses:
            self.assertIn(response, self.survey.responses)

if __name__ == "__main__":
    unittest.main()