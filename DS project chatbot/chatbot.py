import re
import random

class RuleBot:
    negative_responses=("no","nah","not a chance","sorry","oops!")
    exit_commands=("quit","pause","goodbye","Bye","later")
    random_question=("hi, how can I help you?","Suffering from anything..?","Want to find a solution?","Help ,needed!")

def __init__(self):
    self.alienbabble={''}
