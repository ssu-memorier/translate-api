from translate import getGoogleTrans, getPapagoTrans


def lambda_handler(event, context):
    msg = event['message']
    src = event['source']
    tgt = event['target']

    # translated_text = getPapagoTrans.get_translate(msg)
    result = getGoogleTrans.get_translate(msg, src, tgt)

    return {
        'statusCode': 200,
        'body': result
    }
