<a id="readme-top"></a>

# 🧠 Question Type Checker (Prompt-Based Classification)

This notebook uses **Gemini** (Google’s large language model) to classify the **type of questions** in a dataset. It is mainly used to evaluate the filtering accuracy by distinguishing between `text` and `non-text` questions.

---

## 📋 What It Does

- Takes input questions (typically in natural language).
- Uses the **Gemini API** to classify each question into one of two types: `text` or `non-text`.
- Applies a **custom prompt** to ensure output consistency (only `text` or `non-text` is accepted).
- Calculates the classification accuracy across the dataset.

---

## 🤖 Why Gemini?

We use **Gemini 2.0 Flash** (by Google) because:

- ✅ It excels at **reasoning and following natural language instructions** (such as classifying question types).
- 💸 It offers a **generous free tier**, making it great for small-scale or experimental workloads.
- 🪶 It delivers **concise and structured outputs**, ideal for integration into automated pipelines.

---

## ✍️ Prompt Engineering

Prompt design plays a **critical role** in how the LLM interprets and responds.

This notebook includes:
- A tailored prompt to enforce strict classification: only `text` or `non-text`.
- Logic for rate-limiting and retrying requests to ensure reliable API usage.

Effective prompting improves:
- Consistency in classification across large datasets
- Compatibility with downstream processing or filtering logic

---

## 🧰 Dependencies

- `google.generativeai`: Gemini SDK for API access
- `pandas`: For reading and writing structured data
- *(Optional)* `tqdm`: For visual progress tracking

## ⚠️ Notes
- Gemini has API rate limits — avoid sending too many requests in rapid succession.
- As with any LLM, avoid batching too many inputs at once, which could reduce accuracy.
- Always validate the output format to ensure it matches the expected classification.
- Prompt effectiveness greatly influences output reliability — iterative tuning is recommended.

