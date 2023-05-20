

import json   # 追加
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Create Assistant service object.
authenticator = IAMAuthenticator('1X8MaR2WUxUlHH7mrRURJ1JKJEPUKs4bfHEq5XkmVPxJ') # replace with API key  資格情報
assistant = AssistantV2(
    version = '2023-05-15',
    authenticator = authenticator
)
assistant.set_service_url('https://api.jp-tok.assistant.watson.cloud.ibm.com/instances/f205a3bf-e15d-4120-9e93-bb2281975e45') # replace with service instance URL  資格情報
assistant_id = 'e14f592f-4c0d-4428-92dc-a0c03ac0691b' # replace with environment ID

 
response = assistant.create_session(
    assistant_id,
).get_result()
 
print(json.dumps(response, indent=2))

