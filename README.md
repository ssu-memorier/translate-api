# translate-api
---

## PAPAGO API, Google-Trans를 활용한 Translate API 입니다
현재 팀 프로젝트에서는 *Google-Trans* 를 사용하고 있습니다.



### 시나리오
사용자가 번역하고 싶은 텍스트와 원문/번역문의 언어를 선택하여 입력하면 API에서 해당 언어로 번역된 결과와 함께 추가적인 번역 결과 정보를 제공해줍니다.




### < 입력 예시 >
```json
{
  "message": "address",
  "source": "en",
  "target": "ko"
}
```


### < 출력 예시 >
```json
{
   "statusCode":200,
   "body":{
      "source":"en",
      "target":"ko",
      "text":{
         "origin":"address",
         "translated":"주소"
      },
      "allTranslations":{
         "명사":[
            "주소",
            "연설",
            "인사말",
            "청원",
            "사무 능력",
            "구혼",
            "타구 자세",
            "말하는 태도",
            "골프 자세"
         ],
         "동사":[
            "다루다",
            "말을 걸다",
            "제기하다",
            "주소를 쓰다",
            "성명을 쓰다",
            "본격적으로 착수하다",
            "타구 자세를 취하다",
            "골프 자세를 취하다"
         ]
      }
   }
}
```
