import webbrowser
import pyttsx3
import speech_recognition as sr

from pyttsx3 import voice


class OpenVkOrYouTube:
    """
    Открываем Вк или Ютюб голосом
    """
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voice.Voice(id=1))

    def __speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def __listen(self):
        """
        Input: Принимает вашу речь от микрофона

        Output: Возвращает расшифрованную строку с нашими словами
        """

        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.__speak('Я вас слушаю')
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Распознавание...")
            query = r.recognize_google(audio, language='ru')
            print(f"Вы сказали: {query}\n")
        except Exception as e:
            print("Повтори это еще раз, пожалуйста...")
            return "None"

        return query

    def commands(self):
        if 'youtube' in self.__listen().lower():
            webbrowser.open('https://www.youtube.com/')
        elif 'вк' in self.__listen().lower():
            webbrowser.open('https://www.vk.com/')


if __name__ == '__main__':
    run = OpenVkOrYouTube()
    run.commands()
