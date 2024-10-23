import speech_recognition

recognizer = speech_recognition.Recognizer()
r = speech_recognition.Recognizer()

async def recognize_audio(vice_name):
        try:
            with speech_recognition.AudioFile(vice_name) as source:
                 audio = r.record(source)
            recognized_data = recognizer.recognize_google(audio, language="ru")

        except speech_recognition.UnknownValueError:
            pass

        except speech_recognition.RequestError:
            return "Check your Internet Connection, please"

        return recognized_data