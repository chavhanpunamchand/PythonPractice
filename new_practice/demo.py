

import json

resp=dialog_state_out {
  supplemental_display_text: "It\'s 12:22 pm."
  conversation_state: "\n&C#669d81ac-c62e-09e4-6f34-fee4b033b4ad\022\217\003Kh9vMF9QWkhkbnhSZ1QwT1pQbW80YzJhdU01N21JbUJjOJKOmIUGejcKFAgBEhAwMDAwMDAzZDNiZmFlM2MwEh9vMF9QWkhkbnhSZ1QwT1pQbW80YzJhdU01N21JbUJjggGvATIxNj1tMDQ2NlNSN2NQTU9FWU1WN015M1psWXgxR05ZQ2Q3S1JmV19GZ1FvYkJPSlpnZlU2eThBOUI3dDdrS0lqbjJsbWJQUHF5Qi1zRFpZZ3FiQVlCeWpWNGhUbzZiRVhMQzIyZU12amx6XzNLZXhCTldFSDQxQ29YMDl4Q3MzZVAwVUZDQkJTVFVDQ1I5bTRRb1BZZzZDVW1HS25PRzBpX19oRnBNb19MN2lsdWuKARUSEwiw4OqK1tfwAhWTXCsKHdfPAOI"
  microphone_mode: CLOSE_MICROPHONE
}

data=str
new_dict=dict(data)
# json_data=json.loads(data)

print(type(new_dict))
# print(type(data))