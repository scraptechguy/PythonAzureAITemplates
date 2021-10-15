# import elements from libraries for Microsoft Speech Services and credential authentication 

import azure.cognitiveservices.speech as speechsdk
from azure.core.credentials import AzureKeyCredential


# input of keys and endpoints from Microsoft Azure for service authentication and select a language 
# list of available languages: https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support

speech_key, service_region = "<key>", "<region>"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_config.speech_recognition_language="en-US"

# define speech recognizer 

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
