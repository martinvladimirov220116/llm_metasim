import requests

API_URL = "http://localhost:8000/chat"

def display_conversation(history):
    print("\n--- Conversation ---")
    for i, line in enumerate(history):
        speaker = "Buyer" if i % 2 == 0 else "Seller"
        print(f"{speaker}: {line}")
    print("--------------------")


def main():
    print("🧾 Buyer-Seller Chat (type 'Bye' to exit)")
    history = ["Hello! I'm looking to buy something, but only if it meets my needs."]

    while True:
        display_conversation(history)
        seller_input = input("\nYou (Seller): ")
        if seller_input.strip().lower() == "bye":
            print("💬 Conversation ended.")
            break

        history.append(seller_input)

        try:
            response = requests.post(API_URL, json={"history": history}, timeout=None)
            if response.status_code == 200:
                buyer_response = response.json().get("response", "")
                history.append(buyer_response.strip())
            else:
                print(f"❌ Error from LLM API ({response.status_code}): {response.text}")
                break
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Could not connect to the API: {e}")
            break


if __name__ == "__main__":
    main()