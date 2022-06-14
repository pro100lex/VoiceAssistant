import webbrowser
from is_assistant import play_voice_assistant_speech


def search_for_video_on_youtube(text_to_find):
    """
    Поиск видео на YouTube с автоматическим открытием ссылки на список результатов
    :param args: фраза поискового запроса
    """
    search_term = text_to_find
    url = "https://www.youtube.com/results?search_query=" + search_term
    webbrowser.get().open(url)

    # для мультиязычных голосовых ассистентов лучше создать
    # отдельный класс, который будет брать перевод из JSON-файла
    play_voice_assistant_speech("Вот что я нашла по запросу " + search_term + "на ютубе")