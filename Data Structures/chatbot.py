# we define a dictionary to store
responses = {
      "hi": "Hello! Welcome to TechGadget Support. How can I assist you today?",
      "do you have smartwatches": "Yes, we have a variety of smartwatches. You can check them out on our products page.",
      "shipping time": "Shipping usually takes 3-5 business days.",
      "shipping methods": "We offer standard, expedited, and overnight shipping.",
      "return policy": "You can return products within 30 days of receipt for a full refund.",
      "how to return": "To return a product, please visit our returns page for a step-by-step guide.",
      "won’t turn on": "Make sure your gadget is charged. If it still won’t turn on, you can visit our troubleshooting page.",
      "reset device": "To reset your device, hold down the power button for 10 seconds. If that doesn't work, please check the manual for a factory reset.",
      "bye": "Thank you for visiting TechGadget. If you have more questions, feel free to ask. Goodbye!"
}

def get_bot_response(user_input):
    user_input = user_input.lower()

    # Using a loop to iterate through the dictionary checking for keys and returning the respective response
    for keys, response in responses.items():
        if keys in user_input:
            return response
        
    # using return out of the loop to ensure the loop doesnt evaluate to false when it runs
    return "I am not sure how to respond to that message"

while True:
    user_input = input("You: ")

    if user_input in ["quit","exit", "bye"]:
        print("Thank you for your time,feel free to reach out if you have any inquiry")
        break

    # calling the function to get the bot response
    bot_response= get_bot_response(user_input)
    print(f"Bot: {bot_response}")

