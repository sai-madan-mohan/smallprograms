import re

def format_text(text):
    # Remove extra spaces
    text = ' '.join(text.split())

    # Capitalize first letter of each sentence
    sentences = re.split(r'(?<=[.!?]) +', text)
    sentences = [s.strip().capitalize() for s in sentences]
    formatted = '. '.join(sentences)

    # Ensure final punctuation
    if not formatted.endswith(('.', '!', '?')):
        formatted += '.'

    return formatted

# Example Usage
raw_text = input("📝 Enter your messy text: ")
formatted_text = format_text(raw_text)

print("\n✅ Formatted Text:\n")
print(formatted_text)
