from googletrans import Translator

text = '''ମୁଁ ସର୍ବୋତ୍ତମ''' #odia

#creating an instance of Translator to use Google Translator ajax API
translator = Translator()

#detect- auto detects language of input text 
dt = translator.detect(text)
print(dt)

#translate() - traslates the text from source language to
#destination language
#traslate(self, text, dest='en',src='auto)
translated = translator.translate(text)

print(translated.text)