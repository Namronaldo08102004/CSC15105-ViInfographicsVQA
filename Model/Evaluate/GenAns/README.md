# 🧠 GenAns: Generate Answers for Evaluation

To efficiently evaluate model performance on the **ViInfographicsVQA** dataset, we include a dedicated **answer generation** phase using pretrained models from different training approaches.

## 🎯 Why a Separate Generation Phase?

+ The **ViInfographicsVQA dataset** is **large and complex**, containing high-resolution infographic images.

+ To manage memory and performance, we load the dataset using the **streaming mode** from Hugging Face Datasets.

+ However, streaming mode prevents **random access**, making real-time evaluation across the entire dataset **slow and inefficient**.

+ To address this, we **generate answers ahead of time** for both the `validation` and `test` splits.

+ These precomputed results help **speed up the evaluation process**, especially when computing multiple metrics.

## 📦 Models Used for Answer Generation

We use trained checkpoints from both modeling strategies:

+ ✅ Visual-Only Model

+ ✅ Multimodal Text–Visual Fusion Model

The models have been trained and saved at:

🔗 https://huggingface.co/Namronaldo2004/ViInfographicsVQA

> 📌 Note: For details on how to load these checkpoints and generate answers using them, please refer to the scripts and examples provided in this section.