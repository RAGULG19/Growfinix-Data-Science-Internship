# 📊 Growfinix Data Science Internship Portfolio

Welcome to my official Data Science Internship repository! This comprehensive repository showcases a structured series of core industry-level tasks completed during my internship tenure at **Growfinix Technology**. The projects span across exploratory data analysis, automated data extraction, interactive analytical dash-boarding, relational database manipulation, and advanced statistical validation.

---

## 🛠️ Repository Architecture
* **`Task-1-Real-Estate-EDA/`**: Synthetic data generation, comprehensive cleaning pipeline, and statistical visual distributions.
* **`Task-2-Web-Scraping/`**: Automated HTML parsing workflows exporting real estate market listings.
* **`Task-3-Tour-Dashboard/`**: Reactive multi-widget analytical web engine engineered using Streamlit.
* **`Task-4-SQL-Extraction/`**: Relational infrastructure pipeline mapping transactional database queries to Pandas DataFrames.
* **`Task-5-AB-Testing/`**: High-volume conversion hypothesis modeling and UI variant evaluation using SciPy.

---

## 📋 Comprehensive Task Breakthroughs & Core Frameworks

### 📊 Task 1: Real Estate Exploratory Data Analysis (EDA)
* **Objective:** Source, clean, and statistically analyze raw property data logs to isolate valuation drivers.
* **Implementation:** Programmed a custom simulation script generating noisy housing matrices (null data profiles, negative bounds, structural outliers). Handled structural anomalies via Pandas interpolation logic and visualized target valuation fields utilizing Seaborn density plots and location boxplots.
* **Real-World Impact:** Powering foundational data verification layers for modern aggregators (e.g., MagicBricks) to standardize raw distributed broker entries before analytics ingestion.

### 🌐 Task 2: Automated Data Extraction (Web Scraping)
* **Objective:** Construct a programmatic scraper to systematically parse unstructured web markup into operational data logs.
* **Implementation:** Deployed an automated extraction crawler using BeautifulSoup to target modular HTML containers (`div`, specific `class_` labels). Extracted text strings for property titles, location arrays, and pricing fields, formatting the output into a clean `scraped_properties.csv` file.
* **Real-World Impact:** Core enterprise methodology utilized by meta-search systems like Trivago to dynamically crawl and aggregate live distributed competitor pricing charts.

### 🧳 Task 3: Interactive Tour Enquiry Dashboard
* **Objective:** Engineer a real-time reactive analytical interface for commercial travel agencies.
* **Implementation:** Formulated a local web application server using the Streamlit framework. Built cross-reactive UI components and integrated interactive sidebar selection matrices allowing end-users to dynamically sort tour booking frequencies across multiple geographical zones.
* **Real-World Impact:** Implemented by strategic operation desks at MakeMyTrip to track regional seasonal traffic spikes and direct hyper-targeted marketing capital.

### 🗄️ Task 4: Relational SQL Database Data Extraction Pipeline
* **Objective:** Interface relational relational database architecture with active data science processing layers.
* **Implementation:** Instantiated a lightweight SQLite engine environment using the `sqlite3` library. Formulated safe data schema structures, populated rows with test transactional matrices, and executed fine-tuned query statements (`SELECT * WHERE order_amount > 5000`) to pipe critical targets directly into analytical DataFrames.
* **Real-World Impact:** Standard analytical procedures used by e-commerce pioneers like Amazon to isolate high-value user profiles for premium customer retention operations.

### 📊 Task 5: A/B Testing & Statistical Analysis
* **Objective:** Mathematically evaluate user experience layout changes to back data-driven product decisions.
* **Implementation:** Modeled high-volume user behavior matrices comparing a legacy Table Layout (Control Group) against a new Card Layout (Variant Group). Conducted a categorical Chi-Square Contingency analysis via the `SciPy` library to determine the system **p-value (0.017)**. Because the p-value fell below the 0.05 alpha threshold, the conversion lift was verified as statistically significant.
* **Real-World Impact:** Deployed globally by media companies like Netflix to test video preview thumbnail variants scientifically before scaling updates to production servers.

---

## 🚀 Execution, Dependencies & Setup
To activate any operational code module locally, initialize your virtual terminal environment and run the following pip setup dependencies:

```bash
pip install pandas numpy matplotlib seaborn streamlit scipy