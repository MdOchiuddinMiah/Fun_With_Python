import pyttsx3
import PyPDF2

friend = pyttsx3.init()
# friend.say('Hey Shakib, Ki Koro?')
# friend.runAndWait()

book = open('F:\\GRE\\5 lb_basa.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

for num in range(139, 150):
    page = pdfReader.getPage(num)
    text = page.extractText()
    friend.say(text)
    friend.runAndWait()
