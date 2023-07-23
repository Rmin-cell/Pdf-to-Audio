import PyPDF2
import pyttsx3
import PySimpleGUI as sg

sg.theme('BlueMono')

layout = [
    [sg.Text('PDF to Audio Converter')],
    [sg.Input(key='pdf'), sg.FileBrowse('Choose PDF')], 
    [sg.Button('Convert'), sg.Text('', key='status')],
    [sg.Input(key='audio'), sg.FileSaveAs(file_types=(('Audio Files', '.mp3'),))],  
]

window = sg.Window('PDF to Audio', layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
        
    if event == 'Convert':
        pdfFile = values['pdf']
        pdfReader = PyPDF2.PdfReader(pdfFile)
        text = ""
        for page in pdfReader.pages:
            text += page.extract_text()
            
        audio = pyttsx3.init()
        
        # Get audio path from GUI
        audioPath = values['audio']
        
        # Save audio using selected path
        audio.save_to_file(text, audioPath)
        audio.runAndWait()
        
        # Show popup that file was saved
        sg.popup(f'Audio saved to {audioPath}')
        
    if event == 'Save':
        audioFile = values['audio']
        sg.popup(f'Audio saved to {audioFile}')
        
window.close()