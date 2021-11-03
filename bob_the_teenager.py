"""
Bob is a lackadaisical teenager. In conversation, his responses are very limited.

Bob answers 'Sure.' if you ask him a question, such as "How are you?".
He answers 'Whoa, chill out!' if you YELL AT HIM (in all capitals).
He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
He says 'Fine. Be that way!' if you address him without actually saying anything.
He answers 'Whatever.' to anything else.

Implement the response function:

def response(hey_bob):
"""

def response(hey_bob=''):
    if hey_bob == '':
        return 'Fine. Be that way!'    
    elif hey_bob.isupper() and hey_bob[-1] != '?':
        return 'Whoa, chill out!'
    elif hey_bob.isupper() and hey_bob[-1] == '?':
        return "Calm down, I know what I'm doing!"
    elif hey_bob[-1] == '?':
        return 'Sure.'
    else:
        return 'Whatever.'

print(response("CAN I HAZ CHEEZ BURGER?"))
    
   

   

   
   
    

