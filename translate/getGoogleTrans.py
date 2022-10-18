from googletrans import Translator


def get_translate(texts, src, tgt):

    translator = Translator()
    text = translator.translate(texts, src=src, dest=tgt).text
    extra_data = translator.translate(texts, src=src, dest=tgt).extra_data

    # 번역 결과로 이미 주어져서 사용안해도 될듯 X

    if extra_data["all-translations"] is not None:
        # 모든 번역 결과
        allTranslations = {}
        for translations in extra_data["all-translations"]:
            wordType = translations[0]
            possibleTranslations = translations[1]

            allTranslations[wordType] = possibleTranslations
    else:
        allTranslations = None

    return create_response_return(texts, text, src, tgt, allTranslations)


def create_response_return(orgText, translatedText, src, tgt, allTranslations):
    return {
        "source": src,
        "target": tgt,
        "text": {
            "origin": orgText,
            "translated": translatedText
        },
        "allTranslations": allTranslations,
    }
