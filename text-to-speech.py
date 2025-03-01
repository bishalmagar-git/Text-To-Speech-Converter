import pyttsx3

engine = pyttsx3.init()

# Adjust speed
engine.setProperty('rate', 170)

# Change to female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Set volume
engine.setProperty('volume', 0.9)

# Speak
engine.say("Hello, I am your very own Python voice assistant!")

# Run
engine.runAndWait()
