🚀 EMPLEATRONIX - Streamlit Dashboard
EMPLEATRONIX is a Python-based web application developed with Streamlit. It provides an interactive interface to visualize employee salary data from a CSV file using customizable charts.

[Click here](https://empleatronix-app-aw8duovqmwsgkgwkca5p24.streamlit.app/) to view the app running.

✨ Features
Data Loading: Automatically reads employee data from a local CSV file.

Interactive Customization:

🎨 Color Picker: Change the bar chart color in real-time.

🏷️ Toggle Names: Hide or show the names of the employees on the Y-axis.

💰 Toggle Salaries: Display exact salary values directly on the bars.

Dynamic Visualization: Responsive horizontal bar chart built with Matplotlib.

🛠️ Installation & Setup
To run this project locally, follow these steps:

Clone the repository:

```Bash
git clone https://github.com/shism04/empleatronix-app.git
cd empleatronix
Create a virtual environment (Optional but recommended):
```
```Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies: Make sure you have pip installed.
```
```Bash
pip install streamlit pandas matplotlib
Prepare the data: Ensure your CSV file is located at ./resources/employees.csv with at least the following columns: full name and salary.
```
🚀 How to Run
Launch the application by running the following command in your terminal:

```Bash
streamlit run app.py
```
📁 Project Structure
Plaintext

.
├── app.py                # Main Streamlit application code
├── resources/
│   └── employees.csv     # Dataset containing employee info
└── README.md             # Project documentation
📊 Technical Stack
Language: Python

Web Framework: Streamlit

Data Manipulation: Pandas

Visualization: Matplotlib

👤 Author
Ismael Sihammou Anahnah - CPIFP Alan Turing