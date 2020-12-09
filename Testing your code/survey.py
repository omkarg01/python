class AnonymousSurvey():
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_result(self):
        print('Result of the survey: ')
        for response in self.responses:
            print(f'- {response}')

