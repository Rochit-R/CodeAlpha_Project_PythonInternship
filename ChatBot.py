import nltk
from nltk.chat.util import Chat, reflections

ChatBot = [

    [
        r"my name is (.*)",
        ["Hello %1, how can I assist you with your studies today?",]
    ],
    [
        r"what is your name?",
        ["My name is EduBot, and I'm here to help you with your educational queries.",]
    ],
    [
        r"how are you ?",
        ["I'm a virtual assistant, always ready to help!",]
    ],
    [
        r"can you help me with (.*)",
        ["Sure, I can help you with %1. What specifically do you need assistance with?",]
    ],
    [
        r"(.*) (subject|course|topic) (.*)",
        ["I'm familiar with that topic. What specific aspect of %3 do you need help understanding?",]
    ],
    [
        r"i'm (.*) studying (.*)",
        ["Great! Studying %2 is important. How can I assist you in your studies?",]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I can help with %2. What specifically do you need assistance with?",]
    ],
    [
        r"(.*) (assignments?|homework) (.*)",
        ["Do you need help understanding %3, or do you have specific questions about your %2?",]
    ],
    [
        r"(.*) exam (.*)",
        ["Preparing for exams is crucial. What specifically do you need help with regarding your %2?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello! How can I assist you with your studies today?", "Hey there! What educational queries do you have?",]
    ],
    [
        r"(.*) age?",
        ["I'm a virtual assistant, ageless and here to help!",]
        
    ],
    [
        r"(.*) want ?",
        ["I'm here to assist with your educational needs. How can I help you today?",]
        
    ],
    [
        r"bye",
        ["Goodbye! If you have more questions, feel free to ask.", "Bye! Have a great day.",]
    ],
]

def educational_Mychatbot():

    print("Hello! I'm EduBot, your educational assistant. How can I help you today?")
    chat = Chat(ChatBot, reflections)
    chat.converse()

if __name__ == "__main__":

    educational_Mychatbot()

