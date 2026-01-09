# Password Sentinel

A local, offline CLI tool for analyzing password strength using entropy, patterns, dictionary checks, and breach-style hash detection.

## Install
```bash
pip install .



# Password Sentinel 🔐  
**Offline Password Strength Analyzer (CLI)**

Password Sentinel is a production-ready command-line cybersecurity tool that evaluates password strength using entropy calculation, pattern analysis, dictionary checks, and breach-style hash detection — entirely offline.

This project is designed as a **portfolio-grade security tool** demonstrating secure coding practices and algorithmic thinking.

---

## Features

- Secure hidden password input
- Deterministic strength score (0–100)
- Entropy-based analysis
- Regex pattern detection
- Common password dictionary check
- Offline breach-style hash detection (SHA-1 prefix)
- Clear, actionable feedback
- Zero network usage

---

## Tech Stack

- Python 3.10+
- Regex
- hashlib
- argparse
- pytest

---

## Project Structure

password_sentinel/
├── app/
│ ├── cli.py
│ ├── analyzer.py
│ ├── entropy.py
│ ├── patterns.py
│ ├── dictionary_check.py
│ ├── breach_check.py
│ └── scoring.py
│
├── data/
│ ├── common_passwords.txt
│ └── breach_hashes.txt
│
├── tests/
│ ├── test_entropy.py
│ ├── test_patterns.py
│ └── test_scoring.py
│
├── setup.py
├── requirements.txt
└── README.md



---

## Installation & Usage (From Scratch)

### 1. Clone the Repository

```bash
git clone https://github.com/USERNAME/password-sentinel.git
cd password-sentinel


. Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate

pip install .

run : password-sentinel

enter a password to to check strenght

output example :   
Password Strength Analysis
--------------------------
Score: 78 / 100
Rating: STRONG

Details:
- Length: 12 characters
- Entropy: 71.4 bits
- Patterns detected: 0
- Common password: No
- Breach exposure: Not found






