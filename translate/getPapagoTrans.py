import json
import urllib


def get_translate(text):

    with open("keys.json", "r") as f:
        client = json.load(f)

    url = "https://openapi.naver.com/v1/papago/n2mt"  # API url
    encText = urllib.parse.quote(text, encoding="utf-8")

    # 데이터 요청
    data = f"source=en&target=ko&text={encText}"
    request = urllib.request.Request(url)

    # PAPAGO API 계정 로그인
    # papago API Client ID
    request.add_header("X-Naver-Client-Id",
                       client["papago_api_key"]["client_id"])
    # papago API Client Secret
    request.add_header("X-Naver-Client-Secret",
                       client["papago_api_key"]["client_secret"])

    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        t_data = json.loads(response_body)
        return t_data['message']['result']['translatedText']
    else:
        print("n2mt Error Code:", rescode)
