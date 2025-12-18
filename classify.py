def classify(text):
    text = text.lower()
    chain = ""
    if "hydrogen" in text or "nuclear" in text:
        chain += "☢️"
    if "quantum" in text:
        chain += "⚛️"
    if "market" in text or "value" in text:
        chain += "♦️"
    else:
        chain += "♠️"
    chain += "🧱"
    return chain

if __name__ == "__main__":
    import sys
    phrase = sys.argv[1] if len(sys.argv) > 1 else "hydrogen entropy research"
    print("Emoji Classification:", classify(phrase))
