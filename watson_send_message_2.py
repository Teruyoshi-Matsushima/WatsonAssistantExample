import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
 
# Create Assistant service object.
authenticator = IAMAuthenticator('KeeDBZ2zSdrDxeBgLEiOjXofCmyh1OPpj23y9IYJRB63') # replace with API key  資格情報
assistant = AssistantV2(
    version = '2023-05-20',
    authenticator = authenticator
)
assistant.set_service_url('https://api.jp-tok.assistant.watson.cloud.ibm.com/instances/4a935a11-2fdf-4d93-bde7-444776ec1052') # replace with service instance URL  資格情報
assistant_id = '04361d3b-f463-43ef-8ed4-93cb47c0de16' # replace with environment ID
 
response = assistant.message(
    assistant_id,
    session_id = '7dad8261-37ab-46b5-aae2-aaa24a2fa96b',
    input={
        'message_type': 'text',
        'text': '東京',
        'options': {
            'return_context': True
        }
    }
).get_result()
 
print(json.dumps(response, indent=2, ensure_ascii=False))  #「enseure_ascii = false」の指定の有無で、以下のようにUnicodeエスケープあり・なしの日本語が出力されます。