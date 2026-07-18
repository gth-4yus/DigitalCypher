#Dcypher (DIGITALCYPHER)
from flask import Flask, render_template, request
import hashlib
import re

app = Flask(__name__)

def check_strength(password):
    length = len(password)
    rewards = 0
    if length >= 8:
        rewards += 25
    if re.search(r'[A-Z]', password):
        rewards += 20
    if re.search(r'[a-z]', password):
        rewards += 15
    if re.search(r'[0-9]', password):
        rewards += 20
    if re.search(r"\d", password):
        rewards += 20
    if re.search(r"\w", password):
        rewards += 20
    if re.search(r"[!@#$%^&*]", password):
        rewards += 20
    
    return min(rewards, 100)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/', methods=['GET', 'POST'])
def index():
    hashed = ''
    decoded = ''
    strength = 0
    if request.method == 'POST':
        if "clear" in request.form:
            return render_template("index.html", hashed='', decoded='', strength=0)
        
        password = request.form["password"]
        strength = check_strength(password)
        hashed = hash_password(password)
        decoded = password

        if strength >= 70:
            with open("passwords.txt", "a") as f:
                f.write(f"Decoded: {decoded}, Encoded: {hashed}\n")

    return render_template("index.html", hashed=hashed, decoded=decoded, strength=strength)

if __name__ == '__main__':
    app.run(debug=True)


