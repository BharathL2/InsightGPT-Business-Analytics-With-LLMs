# 🚀 InsightGPT – AI-Powered Business Insights from Unstructured Data

InsightGPT is an intelligent web application that blends **Data Science**, **AI/LLMs**, and **Prompt Engineering** to generate actionable business insights from both structured and unstructured data.

<p align="center">
  <img src="static/rating_distribution.png" width="500" alt="Insights Visualization">
</p>

---

## 🔍 Features

- 📊 Upload CSV or Excel datasets for Exploratory Data Analysis (EDA)  
- 🧠 Upload text transcripts (e.g., meeting notes, feedback) for summarization using **GPT**  
- 📈 Auto-generated charts and data visualizations  
- ✍️ AI-powered business insight reports exportable in:  
  - Markdown (`.md`)  
  - PDF (`.pdf`)  
  - PowerPoint (`.pptx`)  

---

## 🛠️ Tech Stack

- **Frontend:** HTML/CSS + Bootstrap  
- **Backend:** Python + Flask  
- **AI/NLP:** OpenAI GPT API  
- **Data Analysis:** Pandas, Matplotlib, Seaborn  
- **Exporting:** ReportLab, python-pptx, markdown2  

---

## 📁 Supported File Uploads

- `.csv`, `.xlsx` — structured tabular data for analysis  
- `.txt`, `.vtt` — transcript files for generating text insights  

---

## ⚙️ Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/BharathL2/InsightGPT.git
    cd InsightGPT
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Add your OpenAI API key in a `.env` file:
    ```bash
    OPENAI_API_KEY=your_key_here
    ```

4. Run the app:
    ```bash
    python app.py
    ```

---

## 📄 Sample Outputs

- Markdown report: `Business_Insights_Report.md`  
- PDF report: `Business_Insights_Report.pdf`  
- PowerPoint presentation: `Business_Insights_Report.pptx`  
- Visualizations (e.g., `static/rating_distribution.png`)  

---

## 💡 Example Use Case

Upload a customer feedback transcript, and InsightGPT will generate:  
- Key sentiment analysis  
- Actionable business suggestions  
- Identification of customer pain points  
- Visualized rating distributions  

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## ⭐ If you find this project useful, please give it a star!
