class Anonymous():
    """Class created to simulate a anonymous survey"""

    def __init__(self,question):
        """Stores the question for the survey and list to store the responses"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Displays the question for the survey"""
        print(self.question)

    def store_response(self,response):
        """Stores the response in responses list"""
        self.responses.append(response)

    def show_results(self):
        """Shows the responses generated"""
        print("Survey results : ")
        for response in self.responses:
            print(f"- {response}")