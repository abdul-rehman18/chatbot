import re
import long_responses as long

def message_probability(user_messsage,recognized_words,single_response=False,required_words=[]):
    message_certainity =0
    has_required_words = False

    for word in user_messsage:
        if word in recognized_words:
            message_certainity+=1
    
    percentage = float(message_certainity)/float(len(recognized_words))

    for word in required_words:
        if word not in user_messsage:
            has_required_words=False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0   


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response,list_of_words,single_response=False,required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response]=message_probability(message,list_of_words,single_response,required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])




def get_response(user_input):
    split_message = re.split(r'\s+|[,:?!.-]\s*',user_input.lower())
    response = check_all_messages(split_message) 
    return response

while True:
    print('Bot: '+ get_response(input('You: ')))
