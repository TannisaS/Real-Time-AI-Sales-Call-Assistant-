# AI Sales Assistant

## Overview
The AI Sales Assistant is a tool that helps sales representatives analyze customer sentiment, provide product recommendations, handle objections, and generate post-call summaries. It integrates **NLP, sentiment analysis, and CRM data** to improve sales call efficiency.

## Features
1. **Real-Time Speech Analysis**  
   - Uses NLP to detect customer sentiment (positive, negative, or neutral).
   - Provides confidence scores for the sentiment detection.

2. **CRM-Integrated Product Recommendation System**  
   - Fetches customer past purchases and interests from a CRM.
   - Suggests relevant products based on customer preferences.

3. **Dynamic Objection Handling Prompt Generator**  
   - Uses a pre-trained GPT model to generate responses to customer objections.

4. **Post-Call Summary and Insights**  
   - Summarizes the sales call based on key concerns raised.
   - Provides actionable follow-up recommendations.

## Technologies Used
- **Python**
- **Transformers Library (Hugging Face)**
- **GPT-2 for Objection Handling**
- **Sentiment Analysis Pipeline**
- **CRM Data Storage (Mock Data)**

## Installation & Usage
### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-sales-assistant.git
cd ai-sales-assistant
```

### 2. Install Dependencies
```bash
pip install transformers torch
```

### 3. Run the Script
```bash
python ai_sales_assistant.py
```

## Example Usage
- **Input:**
  ```plaintext
  Enter customer name: John Doe
  Enter customer speech: I love the product, but the price is too high.
  ```

- **Output:**
  ```plaintext
  [Speech Analysis]
  Detected Sentiment: Positive (Confidence: 0.85)

  [Product Recommendations]
  Based on your interests in ['Electronics', 'Gaming'], we recommend checking out Gaming Headsets and Laptops!

  [Objection Handling Prompt]
  How to handle this objection: I love the product, but the price is too high.
  Suggested response: We offer flexible payment plans. Would you like to explore financing options?

  [Post-Call Summary]
  Customer expressed concerns about pricing. Suggested offering a discount or explaining financing options.
  ```

## Future Enhancements
- Upgrade objection handling to **GPT-3/GPT-4**.
- Connect with **real CRM systems** for personalized recommendations.
- Improve sentiment detection using **advanced ML models**.

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE.txt) file for details.

---

🚀 **AI Sales Assistant – Empowering Smarter Sales Conversations**
