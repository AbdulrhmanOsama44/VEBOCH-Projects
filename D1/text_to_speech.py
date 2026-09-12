import PyPDF2
from gtts import gTTS

pdf_file_path = r"E:\Certificates & CV\Abdulrhman Osama Atwa Abu Jazar Resume.pdf"
text_list = []

with open(pdf_file_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        text = page.extract_text()
        if text:
            text_list.append(text)

full_text = " ".join(text_list).strip()

if full_text:
    tts = gTTS(text = full_text, lang = "en", slow = False)
    tts.save("Text_to_Speech.mp3")
    print("Saved!")
else:
    print("Error! - No Text Found")