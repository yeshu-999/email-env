from transformers import pipeline

# Load model once
generator = pipeline("text-generation", model="gpt2")

def run_inference(text):
    text_lower = text.lower()

    # 🔴 Spam detection
    spam_keywords = ["win money", "free", "click here", "urgent", "lottery"]
    is_spam = any(word in text_lower for word in spam_keywords)

    # 🟢 Score calculation
    score = 5
    if len(text) > 50:
        score += 2
    if "please" in text_lower:
        score += 1
    if "thank" in text_lower:
        score += 1
    if "regards" in text_lower:
        score += 1
    score = min(score, 10)

    # 📂 Category detection
    if is_spam:
        category = "Spam/Promotion"
    elif "meeting" in text_lower or "project" in text_lower:
        category = "Work"
    else:
        category = "General"

    # 📊 Confidence level
    if score > 7:
        confidence = "High"
    elif score > 4:
        confidence = "Medium"
    else:
        confidence = "Low"

    # 🤖 GPT reply generation
    if is_spam:
        reply = "This appears to be spam. No response is recommended."
    else:
        prompt = f"Write a professional email reply:\n{text}\nReply:"
        output = generator(prompt, max_length=120, num_return_sequences=1)
        reply = output[0]["generated_text"].replace(prompt, "").strip()

    # 📤 Final output
    return f"""
📂 Category: {category}
🚫 Spam: {is_spam}
📊 Score: {score}/10
📈 Confidence: {confidence}

🤖 AI Reply:
{reply}
"""