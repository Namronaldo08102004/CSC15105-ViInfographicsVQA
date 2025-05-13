# 📊 Metrics: Evaluating Answer Quality

To assess the performance of our models on the **ViInfographicsVQA** dataset, we employ a comprehensive set of evaluation metrics that capture both lexical and semantic similarity between predicted answers and ground truths.

## 1. 🔵 BLEU-4 (Bilingual Evaluation Understudy)

+ We compute the **BLEU-4** score, a widely used metric in machine translation and text generation tasks.

+ BLEU measures **the n-gram overlap** between the predicted and reference answers.

+ In our case, **BLEU-4** focuses on **4-gram precision**, helping evaluate whether longer, coherent segments in the predicted answers match the reference.

> ⚠️ Note: While BLEU is effective for measuring exact match and surface similarity, it may be less sensitive to paraphrasing or synonyms.

## 2. 🔴 ROUGE (Recall-Oriented Understudy for Gisting Evaluation)

We use three variants of the ROUGE metric:

+ **ROUGE-1**: Measures unigram (word-level) overlap.

+ **ROUGE-2**: Measures bigram (two-word sequence) overlap.

+ **ROUGE-L**: Captures the **Longest Common Subsequence** (LCS) between prediction and reference, useful for evaluating fluency and sentence-level structure.

> ROUGE provides a **recall-oriented** view of how much of the reference answer is captured by the prediction.

## 3. 🟢 BERTScore

+ **BERTScore** goes beyond surface-level matching by using **pretrained contextual embeddings** from a BERT model.

+ It evaluates semantic similarity between answers based on meaning, not just token overlap.

+ We report three metrics:

    + **Precision**: How much of the predicted content is semantically relevant to the reference.

    + **Recall**: How much of the reference meaning is captured by the prediction.

    + **F1-Score**: Harmonic mean of precision and recall — used as the **main indicator** of semantic alignment.

> ✅ BERTScore is particularly valuable for the ViInfographicsVQA dataset, where answers may involve paraphrasing, synonyms, or stylistic variations.