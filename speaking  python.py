from gtts import gTTS
import os

# The text to convert to speech (in Thai)
text = "สวัสดีค่ะ"

# Create a gTTS object
tts = gTTS(text=text, lang='th')

# Save the speech to a file
tts.save("Sound_record.mp3")

# Play the speech
os.system("Sound_record.mp3")
