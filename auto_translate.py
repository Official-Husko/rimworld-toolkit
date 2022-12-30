import json
import requests
from time import sleep
import os

translated_dict = {}
# Set all target languages for auto translation
target_languages = ["de-de", "de-ch", "sq-al", "es-es", "fr-fr", "ru-ru", "zh-zh", "ja-ja", "it-it", "ko-ko"]

# load the corrections file for things that have been detected as wrong
with open("data/languages/translation_corrections.json", "r") as tc_file:
    translation_corrections = json.load(tc_file)

# check the languages folder and delete all except for en-us
languages_found = os.listdir("data/languages")
for language_file in languages_found:
    if language_file == "en-us.json" or language_file == "translation_corrections.json":
        pass
    else:
        os.remove(f"data/languages/{language_file}")

#load en-us to generate the new languages
with open("data\languages\en-us.json") as input_language:
    language_strings = json.load(input_language)
    for language in target_languages:
        for string in language_strings:
            url = f"https://api.mymemory.translated.net/get?q={language_strings[string]}&mt=0&langpair=en-us|{language}"
            sleep(3)
            response_data = requests.get(url)
            if response_data.status_code == 200:
                data = json.loads(response_data.text)
                translated_string = data["responseData"]["translatedText"]
                # try to get fixed from the translation corrections file else use the delivered one by the site
                try:
                    translated_string = translation_corrections[language][string]
                except:
                    pass
                # TODO: fix languages like russian, albanian and probably asian languages
            else:
                print("Translation Failed!")
                input()
                break
            
            translated_dict[string] = translated_string
        
        with open(f"data/languages/{language}.json", "w", encoding="utf-8") as output:
            json.dump(translated_dict, output, indent=4, ensure_ascii=False)
        
        translated_dict.clear()