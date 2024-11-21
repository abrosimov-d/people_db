from random import randint

class Helper():
    
    @staticmethod
    def random_year():
        return randint(1900, 2024)
    
    @staticmethod
    def random_name():
        names = ['Alice', 'Bob', 'Charlie', 'David', 'Frank', 'George', 'Henry', 'Isaac', 'Jack']
        surnames = ['Adams', 'Brown', 'Carter', 'Davis', 'Evans', 'Foster', 'Green', 'Harris', 'Irving', 'Johnson']
        return f'{names[randint(0, 8)]} {surnames[randint(0, 8)]}'

    @staticmethod
    def random_title():
        verbs = [ 'Run', 'Jump', 'Read', 'Write', 'Speak', 'Eat', 'Sleep', 'Sing', 'Swim', 'Laugh']
        adjectives = [ 'Beautiful', 'Quick', 'Bright', 'Silent', 'Happy', 'Tall', 'Old', 'Strong', 'Wise', 'Friendly']
        nouns = [ 'Book', 'House', 'Dog', 'Car', 'Tree', 'River', 'Mountain', 'Computer', 'Phone', 'Chair' ]
        return f'{verbs[randint(0, 9)]} {adjectives[randint(0, 9)]} {nouns[randint(0, 9)]}'
    
    @staticmethod
    def random_id():
        return randint(100000000, 900000000)
    
    @staticmethod
    def random_age():
        return randint(10, 75)
