

import json   # 追加
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Create Assistant service object.
authenticator = IAMAuthenticator('1X8MaR2WUxUlHH7mrRURJ1JKJEPUKs4bfHEq5XkmVPxJ') # replace with API key  資格情報
assistant = AssistantV2(
    version = '2023-05-05',
    authenticator = authenticator
)
assistant.set_service_url('https://api.jp-tok.assistant.watson.cloud.ibm.com/instances/f205a3bf-e15d-4120-9e93-bb2281975e45') # replace with service instance URL  資格情報
assistant_id = 'e14f592f-4c0d-4428-92dc-a0c03ac0691b' # replace with environment ID
 
response = assistant.message(
    assistant_id, # replace with environment ID
    session_id = 'abe7657c-cea8-4c1a-a414-f43f61e87895',
    input={
        'message_type': 'text',
        'text': '今日の天気',
        'options': {
            'return_context': True
        }
    }
).get_result()
 
print(json.dumps(response, indent=2, ensure_ascii=False))  # 「enseure_ascii = false」の指定の有無で、以下のようにUnicodeエスケープあり・なしの日本語が出力されます。