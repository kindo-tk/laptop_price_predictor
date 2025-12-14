# Laptop Price Predictor

This project implements a machine learning-based system to estimate the market price of laptops based on their technical specifications. It is an end-to-end data science project, covering data cleaning, extensive feature engineering, model comparison, and deployment using a **Streamlit** web application.

---

## Overview

The laptop market is saturated with various brands and specifications, making it difficult for consumers to estimate the fair value of a device. The goal of this project is to solve this opacity by predicting prices based on features such as:

- **Brand** (Apple, Dell, HP, etc.)
- **Processor** (Intel i5/i7, AMD, etc.)
- **RAM & Storage** (SSD/HDD)
- **GPU** (Nvidia, Intel Iris, etc.)
- **Screen Type** (IPS, Touchscreen, Resolution)

The project follows a complete Data Science lifecycle and provides a **modern web interface** for users to get instant price estimates.

---

##  Methodology & Workflow

This project was executed in the following detailed steps:

### 1. Data Cleaning & Preprocessing
The raw dataset required significant cleaning to be usable for modeling:
- **Unit Handling:** Removed non-numeric characters (e.g., "GB" from RAM, "kg" from Weight) and converted columns to numeric types.
- **Missing Values:** Handled null values in critical columns to ensure data consistency.

### 2. Exploratory Data Analysis (EDA)
- **Target Variable:** Analyzed the distribution of the `Price` column. It was found to be right-skewed, so a **Log Transformation** was applied to normalize the distribution for better regression performance.
- **Correlation:** Analyzed how features like RAM and Screen Resolution correlated with Price.

### 3. Feature Engineering
This was the most critical phase, where raw text data was converted into meaningful features:
- **Screen Resolution:** Extracted detailed specs to create new binary columns for `TouchScreen` and `IPS Panel`, and calculated `PPI` (Pixels Per Inch).
- **CPU & GPU:** Parsed complex text strings to categorize processors (e.g., "Intel Core i5") and Graphics cards into generalized categories.
- **Storage:** Split mixed storage types (e.g., "128GB SSD + 1TB HDD") into separate columns for `SSD` and `HDD` capacities to capture the premium value of solid-state drives.

---

##  Model Selection & Results

Multiple regression algorithms were trained and evaluated using the R² Score metric. Below is the comparative analysis of their performance based on our testing:

| **Model** | **R² Score** |
| :--- | :--- | 
| **XGBoost Regressor** | **0.839459** | 
| Random Forest Regressor | 0.819675 | 
| Voting Regressor | 0.803241 |
| Linear Regression | 0.759321 |
| Ridge Regression | 0.758772 | 
| Lasso Regression | 0.748790 |
| Decision Tree Regressor | 0.747561 | 
| SVR | 0.737686 | 
| KNN | 0.712115 | 
| Gradient Boosting | 0.704107 | 
| AdaBoost Regressor | 0.596751 |

### XGBoost gave the highest R2 score
---

## Project Structure

```text
laptop-price-predictor/
│
├── app.py                         # Streamlit application
├── models/
│   └── best_laptop_price_model.pkl  # Trained ML pipeline
│
├── notebooks/
│   └── laptop_price_predictor.ipynb # EDA, preprocessing, training & evaluation
│
├── datasets/
│   ├── laptop_data.csv             # Original dataset
│   └── cleaned_data.csv            # Cleaned & feature-engineered dataset
│
├── .gitignore                      # Files & folders ignored by Git
├── LICENSE                         # Project license
├── requirements.txt                # Project dependencies
└── README.md                       # Project documentation
```
---

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/kindo-tk/laptop_price_predictor.git
   ```
2. **Navigate to the project directory:**

    ```sh
    cd laptop_price_predictor
    ```

3. **Create a virtual environment:**

    ```sh
    python -m venv .venv
    ```

4. **Activate the virtual environment:**

   ```sh
   .venv\Scripts\activate
   ```

5. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

6. **Run the Streamlit application:**

    ```sh
    streamlit run streamlit_app.py
    ```
---
## Usage

1. Enter the required laptop details:

   - Brand (e.g., Dell, Apple)
   - Processor & GPU
   - RAM & Storage configuration
   - Screen Size & Resolution

2. Click **Predict Price** to see the estimated market value.

---

## Technologies Used

- Python
- Streamlit
- scikit-learn
- XGBoost
- Pandas & NumPy
> See [`requirements.txt`](requirements.txt) for the full list of dependencies.
---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Contact

For any inquiries or feedback, please contact:

- [Tufan Kundu (LinkedIn)](https://www.linkedin.com/in/tufan-kundu-577945221/)
- Email: tufan.kundu11@gmail.com

---

### Demo

Visit the live app:<a href="https://ipldataanalysisproject.streamlit.app/" > Click here </a>

<img src="https://github.com/kindo-tk/images/blob/main/ui.png" width="600">
<img src="https://github.com/kindo-tk/images/blob/main/ui2.png" width="600">
