from django.core.management.base import BaseCommand, CommandError
from app.models import Quote
import requests
import json
import random
import pprint

class Command(BaseCommand):

    def login(self, username, password):
        login_params = { 'username' : username, 'password' : password, 'grant_type' : 'password'}
        r = requests.post('https://create.kahoot.it/rest/authenticate', json.dumps(login_params), headers={'content-type' : 'application/json'})
        return r.json()['access_token']

    def generate_quiz(self, num_questions, title):
        if num_questions == 0:
            num_questions = Quote.objects.count()
        #generate quiz metadata
        quiz_dict = {
                'title' : title,
                'quizType' : 'quiz',
                'type' : 'quiz',
                'visibility' : 1,
                'language' : 'English',
                'description' : 'Generated by quotebook.me',
                'difficulty' : 500,
                'audience' : 'University',
                'questions' : list()
            }
        all_quotes = list(Quote.objects.all())
        distinct_set = Quote.objects.values('attribution').distinct()
        distinct_names = [x['attribution'] for x in distinct_set]
        random.shuffle(all_quotes)
        for quote in all_quotes[:num_questions]:
            question_dict = {
                    'points' : True,
                    'time' : 20000,
                    'numberOfAnswers' : 4,
                    'questionFormat' : 0,
                    'choices' : list(),
                    'question' : 'Who said: ' + quote.quote
                }
            correct_answer = { 'answer' : quote.attribution, 'correct' : True }
            incorrect_names = self.get_random_names_excluding(quote.attribution, distinct_names)
            incorrect_answers = list()
            for name in incorrect_names:
                incorrect_answers.append({ 'answer' : name, 'correct' : False})
            question_dict['choices'].append(correct_answer)
            question_dict['choices'].extend(incorrect_answers)
            quiz_dict['questions'].append(question_dict)
        return quiz_dict

    def get_random_names_excluding(self, name, name_list):
        while True:
            sample = random.sample(name_list, 3)
            if name not in sample:
                break
        return sample

    def handle(self, *args, **options):
        #login
        username = input('Enter Kahoot username: ')
        password = input('Enter Kahoot password: ')
        try:
            access_token = self.login(username, password)
        except KeyError:
            self.stdout.write('Login error.')
            return
        num_questions = int(input('Enter the number of questions you want (enter 0 to use all the quotes): '))
        title = input('Enter the title of your quiz: ')
        quiz_dict = self.generate_quiz(num_questions, title)
        #upload the quiz
        r = requests.post("https://create.kahoot.it/rest/kahoots", json.dumps(quiz_dict), 
                          headers={'content-type' : 'application/json', 'authorization' : access_token})
        r.raise_for_status()


        