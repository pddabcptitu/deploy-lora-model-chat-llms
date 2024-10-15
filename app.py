from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    # Bạn có thể thêm logic xử lý để trả về câu trả lời của bot
    bot_response = f"Bot: Tôi đã nhận được yêu cầu của bạn: '{user_input}'"

    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
