CRISIS_KEYWORDS = [
    "suicide",
    "kill myself",
    "end my life",
    "hurt myself"
]

CRISIS_RESPONSE = """
I'm really sorry that you're feeling this way.
You are not alone, and help is available.

If you are in India, please contact:
Kiran Mental Health Helpline: 1800-599-0019

If you are in immediate danger, please call emergency services.

Would you like to talk about what’s making you feel this way?
"""

def check_crisis(user_input):
    for word in CRISIS_KEYWORDS:
        if word.lower() in user_input.lower():
            return True
    return False