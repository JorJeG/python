class AnonymousSurvey():
    """Collect anonymous response on survey"""

    def __init__(self, question):
        """Save question and prepend to save response"""
        self.question = question
        self.response = []

    def show_question(self):
        """Print question"""
        print(question)

    def store_response(self, new_response):
        """Save one of response on survey"""
        self.response.append(new_response)

    def show_results(self):
        """Print all responses"""
        print("Survey results:")
        for response in responses:
            print("- " + response)
