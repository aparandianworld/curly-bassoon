#!/usr/bin/env python3

from textblob import TextBlob

def get_response(user_input, intent):
    input = user_input.lower()

    for key, value in intent.items():
        for keyword in value["keywords"]:
            if keyword in input:
                return value["response"]

    return None

def main():

    intent = {
            "hours": {
                "keywords": ["hours", "open", "close", "time"],
                "response": "We are open from 9am to 5pm, Monday to Friday."
            },
            "return": {
                "keywords": ["return", "refund", "exchange", "policy"],
                "response": "We accept returns within 30 days of purchase with no questions asked."
            },
            "shipping": {
                "keywords": ["shipping", "delivery", "ship", "send"],
                "response": "We offer free shipping on orders over $50. Standard delivery takes 3-5 business days."
            },
            "support": {
                "keywords": ["support", "help", "contact", "assistance"],
                "response": "You can reach our support team at support@example.com or call us at (555) 123-4567."
            },
            "location": {
                "keywords": ["location", "where", "address", "store"],
                "response": "Our store is located at 123 Main Street"
            },
            "payment": {
                "keywords": ["payment", "methods", "pay", "credit", "debit"],
                "response": "We accept all major credit cards, debit cards, and PayPal."
            },
            "membership": {
                "keywords": ["membership", "rewards", "loyalty", "program"],
                "response": "Join our loyalty program to earn points on every purchase and enjoy exclusive discounts."
            }
        }

    print("Welcome! Type your query or `quit to exit.")
    print("Example queries: `What are your hours?` or `Can I return my item?`")

    try:
        while True:
                user_input = input("Your query: ").strip()
                if user_input.lower() == "quit":
                    print("Goodbye!")
                    break

                response = get_response(user_input, intent)
                if response:
                    print(response)
                else:
                    print("Unknown reponse. Please try again.")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()