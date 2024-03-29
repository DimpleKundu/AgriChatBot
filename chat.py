from hugchat import hugchat
from hugchat.login import Login

EMAIL = "kavitakundu04@gmail.com"
PASSWD = "ME#diya@04"
cookie_path_dir = "./cookies"
sign = Login(EMAIL, PASSWD)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

def interact_with_chatbot(input_text):
    # Introduction message
    if input_text.lower() in ["hi", "hello", "help", "hey"]:
        return "Hi, I'm an agriculture assistant chatbot. How may I assist you today?"

    # Define a list of agriculture-related keywords
    agriculture_keywords = ["hi", "help", "hello","crop", "farming", "agriculture", "pest", "weather", "market"]

    # Check if the input contains any agriculture-related keywords
    if any(keyword in input_text.lower() for keyword in agriculture_keywords):
        # If it does, proceed with sending the input to the chatbot
        query_result = chatbot.chat(input_text)
        print(query_result)
        return query_result.text
    else:
        # If it doesn't, provide a default response indicating that the chatbot is designed to answer agriculture-related questions
        return "This chatbot is designed to answer agriculture-related questions. Please ask a question related to agriculture."

# def interact_with_chatbot(input_text):
#     query_result = chatbot.chat(input_text)
    
#     return query_result.text

