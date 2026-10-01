# Implementation of Simple Facts Using Python

# Knowledge Base
facts = {
    "sun": {
        "type": "Star",
        "color": "Yellow",
        "system": "Solar System"
    },

    "earth": {
        "type": "Planet",
        "color": "Blue",
        "system": "Solar System"
    },

    "moon": {
        "type": "Natural Satellite",
        "color": "Grey",
        "orbits": "Earth"
    },

    "python": {
        "type": "Programming Language",
        "creator": "Guido van Rossum",
        "purpose": "Software Development"
    },

    "india": {
        "capital": "New Delhi",
        "continent": "Asia",
        "currency": "Rupee"
    }
}


# Function to retrieve facts
def get_fact(subject, attribute):

    subject = subject.lower()
    attribute = attribute.lower()

    if subject in facts:

        if attribute in facts[subject]:
            return facts[subject][attribute]

        else:
            return "Fact not available."

    else:
        return "Subject not found in knowledge base."


# Main Program
print("SIMPLE FACTS KNOWLEDGE BASE")
print("---------------------------")

while True:

    subject = input("\nEnter subject (or exit): ").strip()

    if subject.lower() == "exit":
        print("Program terminated.")
        break

    attribute = input("Enter attribute: ").strip()

    result = get_fact(subject, attribute)

    print("Result:", result)