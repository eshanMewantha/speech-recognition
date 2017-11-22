# Any text typed will be turned in to speech
# To shutdown the program type "turn off".

from windows_text_to_speech import speech
import sys

print("\nText to Speech engine started.Type Anything below")
print("To shutdown the program type 'turn off'.")

while True:
    text = input("> ")
    if text == "turn off":
        speech.say("Good Bye..")
        print("Good Bye..")
        sys.exit()
    else:
        speech.say(text)

