import requests
import json

def get_content(topic):
    api_key = "AIzaSyCdZSZQK7_l5hwFqRy5dy2Vn2j5e_GGJnI"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": f'''
                    Provide 5 min lecure content on {topic} in text format and only give me matter about that topic, and nothing else
                    The topic should not at all deviate and should never sound like an AI gave it. The matter given by you
                    will be read in an online class by a bot. Don't give anything else.
                    '''}
                ]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)

        if response.status_code == 200:
            response_data = response.json()['candidates'][0]['content']['parts'][0]['text']
            
            with open('content.txt', 'w') as content_file:
                content_file.write(response_data)
            
            return True, "Content written successfully."
        else:
            return False, f"Failed to get response. Status code: {response.status_code}"
    
    except Exception as e:
        return False, f"An error occurred: {str(e)}"
