from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/authorize', methods=['POST'])
def authorize():
    data = request.get_json()
    if not data or 'card' not in data or 'amount' not in data:
        return jsonify({'status': 'error'}), 400
    
    return jsonify({'status': 'OK', 'auth_code': 'AUTH123456'})

if __name__ == '__main__':
    app.run()