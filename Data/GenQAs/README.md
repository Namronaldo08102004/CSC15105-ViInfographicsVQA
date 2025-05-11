<a id="readme-top"></a>

# 📊 Infographic QA Generator

This notebook uses Google Gemini to automatically generate question-answer (QA) pairs from infographic images. It is designed for Vietnamese-language infographics and focuses on count-based reasoning (e.g., counting items, visual elements, or text-based data).


## 🤖 Why Gemini?
Google Gemini is a **powerful multimodal language model** developed by Google DeepMind. It's used here for several key reasons:

**1. Multimodal Strength**\
Gemini is capable of interpreting both text and images, making it ideal for understanding the mixed visual-textual nature of infographics.

**2. Concise Task Execution**\
It excels at following well-defined instructions through prompt engineering, producing structured and coherent responses that suit automated pipelines.

**3. High-Quality Reasoning**\
Gemini can handle count-based reasoning, which is crucial when working with visual data that involves counting items, interpreting legends, or summarizing statistics.

**4. Free Tier Available**\
Gemini offers a generous free tier, allowing developers and researchers to experiment without upfront cost. This makes it accessible for prototyping and small-scale dataset generation.

<center>

| RPD | RPM | TPM |
|:-:|:-:|:-:|
| 1,500 | 15 | 1,000,000 |

</center>

**5. Developer-Friendly API**\
Easy-to-use Python SDK (google.genai) with image input support makes integration straightforward and scalable.




## ✨ Prompt Design and Strategy
At the core of this system is a custom-designed prompt tailored for count-based understanding. The prompt is written in Vietnamese and guides Gemini to:
- Generate exactly `n` QA pairs.
- Focus ~60% of the questions on textual elements (e.g., "Có bao nhiêu thành phố có trên 10 triệu dân?")
- Focus ~40% of the questions on non-textual elements (e.g., "Có bao nhiêu mũi tên nằm trong infographic?").
- Use only **visible and countable** content (no hallucinations, no outside knowledge).
- Return answers in a clear, structured format:
    - `Question`, `Answer`, `Explanation`, `Type`.  

The prompt also includes clear instructions on:
- **Answer structure** (must include question, short answer, and explanation).
- **Constraints** (e.g., no vague or general questions, no external knowledge).
- **Content tone** (precise, factual, countable).

This approach ensures the generated content is:
- **Consistent** in format.
- **Focused** on verifiable information from the infographic itself.
- **Useful** for applications such as dataset creation, model training, or educational QA systems.

