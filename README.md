# CSC15105-ViInfographicsVQA
This project focuses on Vietnamese Infographic Visual Question Answering (VQA), featuring a custom-built dataset and a tailored model designed to understand and answer questions based on Vietnamese infographic images.

## 📁 Folders Structure and Flow
```bash
CSC15105-ViInfographicsVQA/
  ├── App/
  ├── Data/
  │    ├── Crawl/
  │    │     ├── Infographics/
  │    │     └── Links/
  │    ├── GenQAs/
  │    └── Statistics/
  │          ├── Initial/
  │          ├── LCS/
  │          └── Vocab/
  └── Model/
       ├── Evaluate/
       │     ├── Gemini_Classification/
       │     ├── GenAns/
       │     └── Metrics/
       └── Train/
```

The folder is structured into a sequential pipeline to solve the Vietnamese Infographic Visual Question Answering task - from dataset creation to model deployment. Each major component is organized in its own folder and explained in more detail through sub-README files.

1. **Data Collection** (`Data/Crawl/`)
    - [`Infographics/`](./Data/Crawl/Infographics/): Crawling Vietnamese infographic images from crawled newspaper links.
    - [`Links/`](./Data/Crawl/Links/): Crawling links from well-known newspaper sources.
2. **Question-Answer Generation** ([`Data/GenQAs/`](./Data/GenQAs/))
    - Generate relevant QA pairs from the infographic content, using the advance Gemini model with refined prompting techniques.
3. **Dataset Statistics & Analysis** (`Data/Statistics/`)
    - [`Initial/`](./Data/Statistics/Initial/): Statistics including source distribution, question types, and length analysis.
    - [`LCS/`](./Data/Statistics/LCS/): Analysis on the linguistic complexity of LCS metrics for cross-dataset comparison.
    - [`Vocab/`](./Data/Statistics/Vocab/): The preprocessing pipeline and special tokens used to construct clean, task-relevant vocabularies for Vietnamese questions and answers.
4. **Model Development** (`Model/`)
    - [`Train/`](./Model/Train/): Model training scripts and configurations. We proposed 2 different approachs to tackle the problem.
    - `Evaluate/`: Scripts for evaluation and inference with metrics.
      - [`Gemini_Classification/`](./Model/Evaluate/Gemini_Classification/): Model classifier, to recognize the type of inputing question.
      - [`GenAns/`](./Model/Evaluate/GenAns/): Provides scripts for running inference over the entire dataset and preparing predictions for metric evaluation.
      - [`Metrics/`](./Model/Evaluate/Metrics/): Measure the infered text with BLEU, ROUGE, and BERTScore.
5. **Application Deployment** ([`App/`](./App/))
    - A web-based demo built with Streamlit and FastAPI to interactively test the VQA system.


📄 *For more detailed information on each part, please refer to the README.md file within the corresponding folder.*


## 🔗 External Links
Our dataset and trained model checkpoints are publicly available on [Hugging Face](https://huggingface.co), enabling easy access and reproducibility for the research community.

- 📊 **Dataset**: [`ViInfographicsVQA`](https://huggingface.co/datasets/Namronaldo2004/ViInfographicsVQA)  
  A custom-built dataset for Vietnamese Infographic Visual Question Answering, including annotated QA pairs across a variety of infographic styles and topics.

- 🧠 **Model**: [`Namronaldo2004/ViInfographicsVQA`](https://huggingface.co/Namronaldo2004/ViInfographicsVQA)  
  Trained VQA model fine-tuned specifically on the ViInfographicsVQA dataset, ready for inference or further fine-tuning.

Feel free to explore the links above to download the data, evaluate the model, or integrate them into your own VQA workflows.

## 🧑‍💻 Contributors
We thank all individuals who have contributed to this project:
- [Kiet-2004](https://github.com/Kiet-2004)
- [Melios22](https://github.com/Melios22)
- [Namronaldo08102004](https://github.com/Namronaldo08102004)
- [joecao0303](https://github.com/joecao0303)
- [nguyenvmthien](https://github.com/nguyenvmthien)

This project was part of NLP Application course, developed during Feb 2025 - May 2025.

### 🙏 Acknowledgement
We would like to express our sincere gratitude to:

- **Dr. Lê Thành Tùng** — for his invaluable guidance and support as our project advisor.  
- **HCMUS – University of Science, VNU-HCM**, and the **CSC15105 - Introduction to Artificial Intelligence** course for providing the academic foundation and environment for this project.  

Special thanks to everyone who contributed to the development of this Vietnamese VQA resource, helping to promote AI research for low-resource languages.
