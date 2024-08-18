import requests
import json


def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    print(response.status_code)

    if response.status_code == 200:
        emotion_score = formatted_response["emotionPredictions"][0]["emotion"]
        return {
            "anger": emotion_score["anger"],
            "disgust": emotion_score["disgust"],
            "fear": emotion_score["fear"],
            "joy": emotion_score["joy"],
            "sadness": emotion_score["sadness"],
            "dominant_emotion": max(emotion_score, key=emotion_score.get),
        }

    elif response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }
