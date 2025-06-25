# First Class Function

def greet(name):
    print("Hello, ",name)

s=greet
s("Keerthana")

# High-order classes

def shout(text):
    return text.upper()

def whisper (text):
    return text.lower()

def speak(style_func,message):
    return style_func(message)

print(speak(shout,"I'm angry......"))
print(speak(whisper,"I love you....."))