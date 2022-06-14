import webbrowser
from is_assistant import play_voice_assistant_speech


def search_for_video_on_youtube(text_to_find):
    search_term = text_to_find.replace('ютубе', 'youtube').replace('ютуб', 'youtube').replace('ютюбе', 'youtube')
    result_search = search_term[search_term.find('youtube') + 8:]
    url = "https://www.youtube.com/results?search_query=" + result_search
    webbrowser.get().open(url)

    play_voice_assistant_speech("Вот что я нашла по запросу " + search_term)