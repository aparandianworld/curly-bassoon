#!/usr/bin/env python3

from textblob import TextBlob

def main():

    intent = {
        "hours": {
            "keywords": ["hours", "open", "close"],
            "response": "We are open from 9am to 5pm, Monday to Friday."
        },
        "return": {
            "keywords": ["return", "refund", "exchange"],
            "response": "We accept returns within 30 days of purchase with no questions asked."
        }
    }

if __name__ == "__main__":
    main()