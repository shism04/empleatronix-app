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

## 🛠️ Installation & Setup

The easiest way to run this project is using **Docker**, which handles all dependencies and environment configurations automatically.

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed.
- [Docker Compose](https://docs.docker.com/compose/install/) installed.

### Steps to Run

1. **Clone the repository:**

    ```Bash
    git clone https://github.com/shism04/empleatronix-app.git
    cd empleatronix-app
    ```
2. **Launch the application:**
Run the following command in the root directory:

    ```Bash
    docker-compose up --build
    ```
3. **Access the app:**
Once the containers are running, open your browser and go to:
`http://localhost:8501`

---

### 🛠 Alternative: Local Development (Manual)

If you prefer to run it without Docker, follow these steps:

1. **Create and activate a virtual environment:**
    ```Bash
    python -m venv venv
    ```
    On Windows: venv\Scripts\activate | On Unix: source venv/bin/activate`
    
2. **Install dependencies:**
    ```Bash
    pip install -r requirements.txt
    ```
3. **Run the Streamlit app:**
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