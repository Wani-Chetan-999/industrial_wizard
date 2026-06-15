
```markdown
# IronEye AI // Industrial Maintenance Wizard 🏭🤖

An enterprise-grade, AI-powered intelligent maintenance decision-support platform built exclusively with Python, Django, and free/open-source technologies. Designed explicitly for steel manufacturing environments, this platform simulates a real-time SCADA Operations Control Center, executing predictive maintenance analytics, multi-agent AI diagnostics, and semantic RAG knowledge retrieval.

---

## 🚀 Core Architectural Highlights

* **SCADA Operations Control Center UI:** A responsive, high-performance dark theme dashboard utilizing Bootstrap 5 and Chart.js to stream live asset telemetry, tracking failure trends and anomalous process variations.
* **Unsupervised Machine Learning Engine:** Powered by a `Scikit-Learn` Isolation Forest algorithm that performs behavioral anomaly detection on real-time sensor streams ($\text{Temperature}$, $\text{Vibration}$), establishing dynamic health indices without relying on rigid, hardcoded thresholds.
* **Zero-Dependency Semantic Vector Space:** Features a custom deterministic embedding generator that creates normalized mathematical vector representations of document chunks without the resource overhead or DLL conflicts of local deep-learning frameworks like PyTorch or ONNX.
* **Groq Multi-Agent Orchestration Core:** Implements an advanced agentic reasoning pipeline leveraging `Llama 3 (70B)` on Groq to dynamically fuse live SCADA parameters with retrieved RAG context. The core routes execution sequentially through specialized virtual personas:
    1.  *Diagnosis Agent:* Isolates mechanical and physical root causes.
    2.  *Risk Agent:* Calculates structural risk scores and process downtime metrics.
    3.  *Recommendation Agent:* Issues itemized, action-oriented safety guidance.

---

## 🏗️ Project Architecture Layout

```text
industrial_wizard/
│
├── industrial_wizard/          # Configuration Root (settings, asgi, urls)
├── services/                   # Global Reusable Service Layer
│   ├── embedding_service.py    # Zero-Dependency Vector Generator
│   ├── groq_service.py         # Multi-Agent Cloud Core Orchestrator
│   ├── prediction_service.py   # Isolation Forest Analytics Core
│   └── rag_service.py          # ChromaDB Storage & Retrieval Layer
├── dashboard/                  # Main SCADA Operations App
├── chatbot/                    # Agentic Conversational Diagnosis App
├── rag_engine/                 # Technical PDF Processing Ingestion App
├── predictive/                 # Machine Learning Visualization App
├── reports/                    # Operational Shift Log Export App
├── alerts/                     # Internal Relational Asset Notification App
├── templates/                  # Base Layout Frames
├── manage.py                   # Global Execution Script
└── requirements.txt            # System Dependency Manifest

```

---

## 🛠️ Installation & Setup Blueprint

### 1. Clone & Isolate the Environment

Navigate to your working directory, initialize a clean Python 3.11 virtual environment, and activate it:

```bash
# Clone the repository and enter the directory
cd industrial_wizard

# Build your Python virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

```

### 2. Install Core Dependencies

Upgrade your local package manager and install the exact verified open-source dependency matrix:

```bash
pip install --upgrade pip
pip install -r requirements.txt

```

### 3. Configure Environment Variables (`.env`)

Create a `.env` file at the root level of your workspace:

```env
DEBUG=True
SECRET_KEY=django-insecure-hackathon-winning-secret-key-matrix
GROQ_API_KEY=your_actual_groq_api_key_here
CHROMA_DB_DIR=./chroma_db

```

### 4. Build Database Schema & Run Population Scripts

Initialize your fresh `db.sqlite3` system files and execute the automated seed data generator to register industrial assets:

```bash
# Generate database blueprints and apply migrations
python manage.py makemigrations dashboard alerts predictive rag_engine
python manage.py migrate

# Populate the control room with initial steel machinery nodes
python manage.py seed_industrial_data

```

### 5. Fire Up the Mission Control Center

Launch the local asynchronous ASGI operational server:

```bash
python manage.py runserver

```

Open up your browser and navigate straight to: **`http://127.0.0.1:8000/`**

---

## 🎯 Live Demonstration Narrative Walkthrough

Maximize your presentation score by guiding the judging panel through this high-impact operational story:

1. **Step 1: The Event Flag (`/dashboard/`)** – Show the live **SCADA Matrix**. Point out that the **Coke Ore Supply Line Conveyor Engine** has thrown a critical status notification.
2. **Step 2: Machine Learning Isolation (`/predictive/`)** – Open the **ML Diagnostics** panel. Demonstrate how the background *Isolation Forest* automatically isolated the high-temperature outlier and calculated a 65% failure risk.
3. **Step 3: Document Intelligence (`/rag/`)** – Jump to **Knowledge Ingestion** and upload a machinery guide or SOP PDF. Watch the engine parse text chunks and index them into ChromaDB seamlessly.
4. **Step 4: Agentic Co-Pilot Fix (`/chatbot/`)** – Pinned the active asset profile inside **AI Troubleshooting**. Query *"Conveyor motor vibration increasing."* Show the panel how Groq merges the live context and RAG context to supply an explainable, multi-stage repair layout.
5. **Step 5: Handover Reporting (`/reports/export/`)** – Hit **Export Shift Log** in the sidebar to download a structured text file, completing a clean, closed-loop maintenance run.

---

## 🐳 Docker Deployment Support

For containerized cloud deployment environments (Render, Railway, or AWS), build and run using the optimized configuration setup:

```bash
# Build the container
docker-compose build

# Boot the app services container stack
docker-compose up

```

---

