# Customer Support Ticket Analysis Project

📌 **Project Overview**

This project analyzes 376 customer support tickets to identify common issues, measure response efficiency, and recommend process improvements. The workflow includes:

* Python (Google Colab) for data cleaning & NLP-based text analysis
* Tableau for interactive dashboarding
* Key Insights to optimize support operations

🛠️ **Tools Used**

| Tool                 | Purpose                                       |
| :------------------- | :-------------------------------------------- |
| Python (Pandas, NLTK)| Data cleaning, text mining, statistical analysis |
| Google Colab         | Cloud-based Python execution                  |
| Tableau              | Interactive dashboard visualization           |
| Excel                | Supplemental data validation                |

📂 **Repository Structure**

📂 customer-support-analysis/ ├── 📄 raw_data/ # Original dataset │ └── customer_support_tickets.csv
├── 📄 processed_data/ # Cleaned data for Tableau │ └── cleaned_support_tickets.csv
├── 📄 notebooks/ # Jupyter/Colab notebooks │ └── support_ticket_analysis.ipynb
├── 📄 tableau/ # Tableau workbook & exports │ ├── support_dashboard.twbx
│ └── dashboard_screenshots/
└── 📄 README.md


🔍 **Key Insights from Analysis**

1.  **Most Common Issues**
    * **Top 3 Problem Categories:**
        * Technical Issues (38%)
            * Frequent keywords: "not turning on", "network problem", "setup failed"
            * Worst-affected products: Microsoft Office, HP Pavilion
        * Billing Inquiries (22%)
        * Refund Requests (18%)

2.  **Response Time Metrics**
    * **Metric** | **Average Time**
    * -------------------- | ----------------
    * First Response Time  | 4.2 hours
    * Resolution Time      | 8.7 hours
    * *Critical tickets take 12+ hours (needs prioritization).*

3.  **Customer Satisfaction (CSAT)**
    * Average Rating: 3.1/5
    * **Lowest-rated areas:**
        * Slow resolution for hardware issues
        * Unclear refund processes

📊 **Tableau Dashboard Features**

**Key Visualizations:**

* Ticket Volume Trends (by product/month)
* Response Time Distribution (priority-wise)
* CSAT Score Distribution
* Resolution Time Distribution
* Tickets Over Time

📬 **Contact**

Made with 💻 by AFIGA BEGUM

📩 Email: afiga97@gmail.com
