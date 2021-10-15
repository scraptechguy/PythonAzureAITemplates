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


    
# code from here to the three hashes must be called only once as it would otherwise create
# multiple listening sessions and the variable result would store doubled or tripled (based on how many
# times have you started the session) results. 

# create a listening session on Azure for speech recognition
        
speech_recognizer.recognized.connect(lambda evt: collectResult(evt))
speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED:    {}'.format(evt)))
speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))

speech_recognizer.session_stopped.connect(stop_cb)
speech_recognizer.canceled.connect(stop_cb)
