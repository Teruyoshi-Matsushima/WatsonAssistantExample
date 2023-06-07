

import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
 
# Create Assistant service object.
authenticator = IAMAuthenticator('xxxxxxxxxxxxxxxxxx') # replace with API key  資格情報
assistant = AssistantV2(
    version = '2023-05-20',
    authenticator = authenticator
)
assistant.set_service_url('https://api.jp-tok.assistant.watson.cloud.ibm.com/instances/xxxxxxxxxxxxxxxxxx') # replace with service instance URL  資格情報
assistant_id = 'xxxxxxxxxxxxxx' # replace with environment ID
 
response = assistant.message(
    assistant_id,
    session_id = 'xxxxxxxxxxxxxx',
    input={
        'message_type': 'text',
        'text': '今日',
        'options': {
            'return_context': True
        }
    }
).get_result()
 
print(json.dumps(response, indent=2, ensure_ascii=False))  #「enseure_ascii = false」の指定の有無で、以下のようにUnicodeエスケープあり・なしの日本語が出力されます。