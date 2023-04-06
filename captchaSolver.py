from twocaptcha import TwoCaptcha
import os

def solveCaptcha(sitekey, url, captchakey) :
    api_key = os.getenv('APIKEY_2CAPTCHA', captchakey)

    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(
            sitekey=sitekey,
            url=url)

    except Exception as e:
        print(e)

    else:
        return result
