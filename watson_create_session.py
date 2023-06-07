

import json   # 追加
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

 
response = assistant.create_session(
    assistant_id,
).get_result()
 
print(json.dumps(response, indent=2))

