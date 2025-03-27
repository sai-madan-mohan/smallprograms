from gensim.summarization import summarize

def text_summarizer():
    text = input("Enter a long paragraph:\n")

    if len(text.split())<50:
        print("Please enter a longer text to summarize.")
        return
    summary = summarize(text, ratio=0.3)
    print("\n  Summary:\n", summary)

text_summarizer()