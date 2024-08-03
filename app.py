from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Function to load responses from a text file
def load_responses(file_path):
    responses = {}
    with open(file_path, 'r') as file:
        for line in file:
            if ':' in line:
                key, value = line.strip().split(':', 1)
                responses[key.strip().lower()] = value.strip()
    return responses

# Load responses from the text file
responses = load_responses('responses.txt')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message'].strip().lower()
    response = responses.get(user_input, "I'm sorry, I don't understand that.")
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
