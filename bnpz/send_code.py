import random
import requests
import json
import uuid


def send_code(phone: object, message: object, sender: object = "4546") -> object:
    dispatch_id = str(uuid.uuid4()).split('-')[0]
    sms_id = str(uuid.uuid4()).split('-')[0]

    from bnpz.models import Eskiz
    token = Eskiz.objects.all()[0]

    try:
        url = "http://notify.eskiz.uz/api/message/sms/send-batch"
        payload = json.dumps(
            {
                "messages": [
                    {
                        "user_sms_id": sms_id,
                        "to": int(phone),
                        "text": message
                    }
                ],
                "from": sender,
                "dispatch_id": dispatch_id
            })
        headers = {
            'Authorization': f'Bearer {token.token}',
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        from bnpz.models import SmsCode
        SmsCode.objects.create(phone=phone, message=message)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    print(response.json(), "sms code ___________________________________________")
    return {"message_status": response.json(), "phone": phone, "dispatch_id": dispatch_id}


def check_phone(phone, code, sender="4546"):
    dispatch_id = str(uuid.uuid4()).split('-')[0]
    sms_id = str(uuid.uuid4()).split('-')[0]
    from bnpz.models import Eskiz
    token = Eskiz.objects.all()[0]

    rand_list = random.sample(range(1, 10), 4)
    rand_str = ''.join(map(str, rand_list))
    print(token.token)
    try:
        url = "http://notify.eskiz.uz/api/message/sms/send-batch"
        payload = json.dumps({
            "messages": [
                {
                    "user_sms_id": sms_id,
                    "to": phone,
                    "text": f"{code} {rand_str}"
                }
            ],
            "from": sender,
            "dispatch_id": dispatch_id
        })
        headers = {
            'Authorization': f'Bearer {token.token}',
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        from bnpz.models import SmsCode
        SmsCode.objects.create(phone=phone, code=rand_str)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    print(f"{code} {rand_str}")
    print(response.json())
    return {"message_status": response.json(), "phone": phone, "dispatch_id": dispatch_id, "code" : rand_str }


def refresh_token():
    from bnpz.models import Eskiz
    token = Eskiz.objects.all()[0]
    print(token.token)
    try:
        url = "http://notify.eskiz.uz/api/auth/refresh"

        headers = {
            'Authorization': f"Bearer {token.token}",

        }
        response = requests.request("PATCH", url, headers=headers)

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    token.token = response.json()['data']['token']
    token.save()
    print(response.json()['data']['token'], "refresh code")
    return {"message": "Okdaaaa"}
