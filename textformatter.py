text = input("Input a text or a message: ") 

def lowercase(func):
    def low(msg):
        mod_text = msg.lower()
        return func(mod_text)
    return low

def word_count(text):
    return "text length:", len(text)

@lowercase
def low_text(text):
    return text

print(word_count(text))
print(low_text(text))
