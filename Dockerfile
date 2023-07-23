FROM python:3.7

WORKDIR /app

#COPY requirements.txt ./
RUN pip install PyQt5 PyPDF2 pyttsx3

COPY . .

CMD [ "python", "Semi-final.py" ]