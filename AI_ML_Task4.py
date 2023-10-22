from googletrans import Translator
from retrying import retry

def translate_to_hinglish(english_text):
    translator = Translator()
    hinglish_text = translator.translate(english_text, src='en', dest='hi').text
    return hinglish_text

# Statements to be translated
statements = [
    "Definitely share your feedback in the comment section.",
    "So even if it's a big video, I will clearly mention all the products.",
    "I was waiting for my bag."
]

# Translate and print the Hinglish versions
for statement in statements:
    hinglish_translation = translate_to_hinglish(statement)
    print(f"Statement: {statement}")
    print(f"Output required: {hinglish_translation}\n")