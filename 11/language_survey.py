from survey import AnonymousSurvey

#definition of a question with creature instance of AnonymousSurvey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

#Print question and save response
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

#Print results survey
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
