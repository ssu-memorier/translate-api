from translate import getGoogleTrans, getPapagoTrans


def create_papago_return(text1, text2):
    return {
        "source": "en",
        "target": "ko",
        "text": {
            "origin": text1,
            "translated": text2
        }
    }


def lambda_handler(event, context):
    print(event)
    print(context)
    msg = event['message']

    translated_text = getPapagoTrans.get_translate(msg)
    # translated_text = get_google_trans(msg)

    return {
        'statusCode': 200,
        'body': create_papago_return(msg, translated_text)
    }
