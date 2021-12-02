# Imtiaz Adar
# Phone : +8801778 767775
# Email : imtiaz-adar@hotmail.com
# Project : PDF Reader
# Language Used : Python

import pyttsx3 as audio
import PyPDF2 as PDF
path = open('books/Bangladesh.pdf', 'rb')
reader = PDF.PdfFileReader(path)
page = reader.getPage(0)
text = page.extractText()

engine = audio.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say(text)
engine.save_to_file(text, 'Bangladesh.mp3')
print(text)
engine.runAndWait()
engine.stop()