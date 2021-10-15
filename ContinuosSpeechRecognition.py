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



# set result (variable to which recognized speech is stored) to blank and done (variable that when False keeps calling 
# azure speech recognition and when True stops listening session) to False

result = " "
done = False


# stop_cb() cuts off azure speech recognition session and set done to True -> in check() if done processes 
# the recognized text

def stop_cb(evt):
    print('CLOSING on {}'.format(evt))
    speech_recognizer.stop_continuous_recognition()
    global done
    done = True


# collectResult() stores recognized utterances into variable result

def collectResult(evt):
    global result 
    result += " {}".format(evt.result.text)

