import speech_recognition as sr
import os
import sys

r = sr.Recognizer()

try:
	while True:
		with sr.Microphone() as source:
			print("komut gir")
			ses = r.listen(source)
			komut = str(r.recognize_google(ses , language = "tr"))

			komut = komut.lower()
		if komut == "hesap makinesi aç":
			os.system("calc")
		if komut == "hesap makinesi	kapat":
			os.system("TASKKILL /F /IM calculator.exe")
		if komut == "chrome aç":
			os.system("start chrome")
		if komut == "chrome kapat":
			os.system("TASKKILL /F /IM chrome.exe")
		if komut == "youtube aç":
			os.system("start www.youtube.com")
		if komut == "git hap aç":
			os.system("start www.github.com")


except KeyboardInterrupt:
	sys.exit()
