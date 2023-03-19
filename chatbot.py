import re
import long_responses as long

def message_probability(user_messsage,recognized_words,single_response=False,required_words=[]):
    message_certainity =0
    has_required_words = False

    for word in user_messsage:
        if word in recognized_words:
            message_certainity+=1
    
    percentage = float(message_certainity)/float(len(recognized_words))

def get_response(user_input):
    split_message = re.split(r'\s+|[,:?!.-]\s*',user_input.lower())
    response = check_all_messages(split_message) 
    return response

while True:
    print('Bot: '+ get_response(input('You: ')))
