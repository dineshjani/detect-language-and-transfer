# import The IBM Watson Language Translator service 
from ibm_watson import LanguageTranslatorV3
# all supported model 
# ex. 'es-en' mean model for Spanish to english translation and 'en-es' model for english to Spanish
supportedLanguageModels=['ar-en', 'bg-en', 'bn-en', 'bs-en', 'ca-es', 'cnr-en', 'cs-en', 'cy-en', 'da-en', 'de-en', 
'de-fr', 'de-it', 'el-en', 'en-ar', 'en-bg', 'en-bn', 'en-bs', 'en-cnr', 'en-cs', 'en-cy', 'en-da', 'en-de', 'en-el',
'en-es', 'en-et', 'en-fi', 'en-fr', 'en-fr-CA', 'en-ga', 'en-gu', 'en-he', 'en-hi', 'en-hr', 'en-hu', 'en-id', 'en-it', 
'en-ja', 'en-kn', 'en-ko', 'en-lt', 'en-lv', 'en-ml', 'en-mr', 'en-ms', 'en-mt', 'en-nb', 'en-ne', 'en-nl', 'en-pa',
'en-pl', 'en-pt', 'en-ro', 'en-ru', 'en-si', 'en-sk', 'en-sl', 'en-sr', 'en-sv', 'en-ta', 'en-te', 'en-th', 
'en-tr', 'en-uk', 'en-ur', 'en-vi', 'en-zh', 'en-zh-TW', 'es-ca', 'es-en', 'es-eu', 'es-fr', 'et-en', 'eu-es', 
'fi-en', 'fr-CA-en', 'fr-de', 'fr-en', 'fr-es', 'ga-en', 'gu-en', 'he-en', 'hi-en', 'hr-en', 'hu-en', 'id-en', 
'it-de', 'it-en', 'ja-en', 'kn-en', 'ko-en', 'lt-en', 'lv-en', 'ml-en', 'mr-en', 'ms-en', 'mt-en', 'nb-en', 'ne-en',
 'nl-en', 'pa-en', 'pl-en', 'pt-en', 'ro-en', 'ru-en', 'si-en', 'sk-en', 'sl-en', 'sr-en', 'sv-en', 'ta-en', 'te-en', 'th-en', 
 'tr-en', 'uk-en', 'ur-en', 'vi-en', 'zh-TW-en', 'zh-en']
def translationToEnglish(text):
    # set up translator
    translator = LanguageTranslatorV3(
            '2018-05-01',
            url='https://api.us-east.language-translator.watson.cloud.ibm.com/instances/f6b9cb7c-5c75-4cac-ab90-59faf9d0000b',
           iam_apikey='x4AVDsjfsul5FsKLmsTg2XLp_28B-vgX0vAfNDLDl3zY',
            )
    # detect language
    response = translator.identify( text ).get_result()
    #print(response['languages'][0])
    #if the language detection accuracy is above threshold value then translate to Base Language
    if response and response['languages'][0]['confidence'] > 0.3:
                language = response['languages'][0]['language']
                
                #check language is not english and required model is present
                languageModel=language+"-"+"en"
                if  language !="en" and languageModel in supportedLanguageModels:
                    
                    # translate language to english language
                    translateresponse = translator.translate(
                                    text,
                            source=language,
                        target="en"
                        ).get_result()
                    text = translateresponse['translations'][0]['translation']
                    
    return text
 
path = 'Desktop\english.txt'
with open(path, 'r') as f:
    lines = f.readlines()
matches = []
    
for l in lines:
    matches.append(l)
for text in matches:
    inEnglish=translationToEnglish(text)
    print(inEnglish)
        
