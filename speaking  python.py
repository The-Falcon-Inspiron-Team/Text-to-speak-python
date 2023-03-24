from gtts import gTTS
import os


text = "สวัสดีค่ะ"


tts = gTTS(text=text, lang='th')


tts.save("Sound_record.mp3")


os.system("Sound_record.mp3")
