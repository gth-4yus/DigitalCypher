# 🔐 D-Cypher - Password Strength Checker

A simple web-based Password Strength Checker built using **Python** and **Flask**. This project analyzes the strength of a password based on common security rules and provides users with feedback to create stronger passwords.

## 🚀 Features

- ✅ Checks password strength
- ✅ Detects weak, medium, and strong passwords
- ✅ Validates:
  - Minimum password length
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- ✅ Simple and user-friendly interface
- ✅ Built using Flask for the backend

---

## 🛠️ Technologies Used

### Backend
- Python
- Flask

### Python Libraries
- `Flask`
- `hashlib`
- `re` (Regular Expressions)

### Frontend
- HTML5
- CSS3

---

## 📂 Project Structure

```
D-Cypher/
│
├── passcheck.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── README.md
└── requirements.txt
```

---

## 📦 Python Modules Used

| Module | Purpose |
|---------|---------|
| Flask | Creates the web application |
| render_template | Renders HTML pages |
| request | Receives user input from forms |
| hashlib | Generates password hashes |
| re | Validates password patterns using Regular Expressions |

---

## 🔍 How It Works

1. User enters a password.
2. Flask receives the input.
3. Python checks the password using Regular Expressions.
4. Password strength is analyzed.
5. The result is displayed on the webpage.

---

## 💻 Installation

Clone the repository

```bash
git clone https://github.com/your-username/D-Cypher.git
```

Move into the project directory

```bash
cd D-Cypher
```

Install Flask

```bash
pip install flask
```

Run the application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 🎯 Future Improvements

- Password breach detection
- Password generator
- Dark/Light mode
- Password entropy calculation
- Copy password feature
- Better UI/UX
- User authentication

---

## 📸 Preview



---

## 👨‍💻 Author

**Aditya Purty**

Cybersecurity Enthusiast | Python Developer | Learning Ethical Hacking

---

## 📜 License

This project is created for learning purposes and is open for educational use.
