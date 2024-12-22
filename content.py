from flask import Flask, request, jsonify, json
from flask_cors import CORS
import os
from get_content import get_content
from write_questions import write_questions

app = Flask(__name__)

CORS(app)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/get_maal', methods=['POST'])
def get_maal():
    try:
        data = request.get_json()
        topic = data.get('topic')

        if not topic:
            return jsonify({"message": "Topic is required"}), 400
        get_content(topic)
        write_questions(topic)
        with open('questions.json', 'r') as file:
            questions = json.load(file)
        with open('content.txt', 'r') as file:
            content = file.readlines()
        response_data = {
            "content" : content,
            "questions": questions
        }
        
        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({"Message": str(e)}), 500
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000)) 
    app.run(host='0.0.0.0', port=port, debug=True)