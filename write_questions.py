import requests
import json
def write_questions(topic):
    api_key = "AIzaSyCdZSZQK7_l5hwFqRy5dy2Vn2j5e_GGJnI"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": f'''
                    Provide 10 multiple-choice questions on {topic} in JSON format. 
                    Each question should have four options and a correct answer. The JSON format should 
                    be a list of objects, where each object contains the question, options, and the correct answer.
                    Give the answer as text but still in the JSON format. The object notations should be 'question', 
                    'options', and 'answer'.
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
            with open('questions.json', 'w') as json_file:
                json_file.write(response_data[8:-5]) 
            
            return True, "Questions generated successfully."
        else:
            return False, f"Failed to get response. Status code: {response.status_code}"
    
    except Exception as e:
        return False, f"An error occurred: {str(e)}"