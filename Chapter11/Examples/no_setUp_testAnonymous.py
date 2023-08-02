import unittest
from anonymous import Anonymous

class TestAnonymous(unittest.TestCase):

    def test_single_response_storage(self):
        """Tests whether a single response submitted is stored properly"""
        survey = Anonymous("Which language do you know?")
        survey.store_response("English")
        self.assertIn("English", survey.responses)

    def test_multiple_response_storage(self):
        """Tests whether multiple responses submitted are stored properly"""
        survey = Anonymous("Which languages do you know ?")
        responses = ["lang1", "lang2", "lang3"]

        for response in responses:
            survey.store_response(response)

        for response in responses:
            self.assertIn(response, survey.responses)
        

if __name__ == "__main__":
    unittest.main()