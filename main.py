from vosk import Model, KaldiRecognizer  # оффлайн-распознавание от Vosk
import speech_recognition  # распознавание пользовательской речи (Speech-To-Text)
import pyttsx3  # синтез речи (Text-To-Speech)
import wave  # создание и чтение аудиофайлов формата wav
import json
import os
from is_assistant import VoiceAssistant, setup_assistant_voice, play_voice_assistant_speech
from recognizer import record_and_recognize_audio, use_offline_recognition
from commands import commands
from folder_functions.search_video_on_youtube import search_for_video_on_youtube
from folder_functions.bot_greeting_user import bot_greeting_user
from folder_functions.bot_farewell_user import bot_farewell_user


def the_determinant_of_the_type_of_command(command, voice_text):
    if command == 'search_video_on_youtube':
        search_for_video_on_youtube(voice_text)
    elif command == 'greeting':
        bot_greeting_user()
    elif command == 'farewell':
        bot_farewell_user()


def search_command_in_commands(voice_text):
    dct_coincidence = {}
    for key in commands.keys():
        lst_command_words = commands[key]
        print(type(lst_command_words))
        print(lst_command_words, len(lst_command_words))
        for i in range(len(lst_command_words)):
            if lst_command_words[i] in voice_text:
                if key not in dct_coincidence.keys():
                    dct_coincidence[key] = 1
                else:
                    dct_coincidence[key] += 1
    sort_dct_coincidence = sorted(dct_coincidence.items(), key=lambda x: x[1])
    finder_dict_key = sort_dct_coincidence[-1][0]
    the_determinant_of_the_type_of_command(finder_dict_key, voice_text)


if __name__ == "__main__":
    # инициализация инструментов распознавания и ввода речи
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    # инициализация инструмента синтеза речи


    # настройка данных голосового помощника
    assistant = VoiceAssistant()
    assistant.name = "Alice"
    assistant.sex = "female"
    assistant.speech_language = "ru"

    # установка голоса по умолчанию
    setup_assistant_voice(assistant)

    while True:
        # старт записи речи с последующим выводом распознанной речи
        # и удалением записанного в микрофон аудио
        voice_input = record_and_recognize_audio(microphone=microphone, recognizer=recognizer)
        os.remove("microphone-results.wav")
        print(voice_input)

        # отделение комманд от дополнительной информации (аргументов)
        search_command_in_commands(voice_input)