"""A translation system as part of the Python AI project"""

# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


class NullInputException(Exception):
    """Raised if input is null"""


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)
language_translator.set_service_url(url)


def english_to_french(english_text: str) -> str:
    """Translates English to French with Watson"""
    if english_text is None:
        raise NullInputException
    translation = language_translator.translate(
        text = english_text,
        model_id = 'en-fr'
    ).get_result()
    return translation.get("translations")[0].get("translation")


def french_to_english(french_text: str) -> str:
    """Translates French to English with Watson"""
    if french_text is None:
        raise NullInputException
    translation = language_translator.translate(
        text = french_text,
        model_id = 'fr-en'
    ).get_result()
    return translation.get("translations")[0].get("translation")
