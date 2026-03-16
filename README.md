📘 Peblo Quiz Engine

An **AI-assisted quiz generation and evaluation platform** that converts educational PDFs into interactive quizzes and automatically evaluates student answers.

The system demonstrates how **educational content ingestion, quiz generation, and automated scoring** can be implemented using modern backend technologies.


# 🚀 Project Overview

Peblo Quiz Engine is designed to **simplify quiz creation from educational material**.

Teachers and educational platforms often deal with large textbooks and PDFs. Creating quizzes manually from this content is time-consuming.

This project automates the process by:

📄 Extracting content from PDFs
🧠 Processing educational text
❓ Generating quiz questions
👨‍🎓 Allowing students to submit answers
📊 Automatically evaluating performance

The project demonstrates a **REST API based backend architecture** using **FastAPI**.

# 🎯 Problem Statement
Educational institutions frequently require quizzes for assessment and practice.
However:
❌ Creating quizzes manually from textbooks takes significant time
❌ Evaluating answers for many students is inefficient
❌ Traditional quiz systems cannot easily adapt to new learning material

Peblo Quiz Engine addresses these issues by building a **content processing pipeline** that converts educational content into quizzes automatically.


# 🧠 Solution Approach

The system uses a **pipeline-based architecture** consisting of the following stages:

1️⃣ **Content Ingestion**
Upload educational PDFs.

2️⃣ **Text Extraction**
Extract raw text from the PDF.

3️⃣ **Content Chunking**
Break the text into smaller meaningful segments.

4️⃣ **Quiz Generation**
Create multiple-choice questions from the extracted content.

5️⃣ **Student Answer Submission**
Students submit their answers through an API.

6️⃣ **Automated Evaluation**
The backend compares answers and calculates scores.

# 🏗 System Architecture
```
PDF Upload
     │
     ▼
Content Extraction
     │
     ▼
Text Chunking
     │
     ▼
Quiz Generation
     │
     ▼
Quiz Retrieval
     │
     ▼
Student Answer Submission
     │
     ▼
Score Evaluation
The system follows a **modular backend architecture** consisting of:

• API Layer
• Service Layer
• Data Layer

---

# 🛠 Technologies Used

| Technology        | Purpose                            |
| ----------------- | ---------------------------------- |
| 🐍 Python         | Core programming language          |
| ⚡ FastAPI         | High-performance backend framework |
| 🚀 Uvicorn        | ASGI server                        |
| 📚 Swagger UI     | Interactive API documentation      |
| 📄 PDF Processing | Content extraction                 |

---

# 📂 Project Structure

```
Peblo/
│
├── app/
│   │
│   ├── main.py
│   │
│   ├── routers/
│   │   ├── ingest_router.py
│   │   ├── quiz_router.py
│   │   └── student_router.py
│   │
│   ├── services/
│   │   ├── ingest_pdf.py
│   │   ├── quiz_service.py
│   │   └── student_service.py
│   │
│   └── models/
│
├── sample_pdfs/
│   ├── peblo_pdf_grade4_english_grammar.pdf
│   └── peblo_pdf_grade3_science_plants_animals.pdf
│
├── requirements.txt
│
└── README.md
```
---

# 📄 File Explanation

### main.py

Entry point of the FastAPI application.

Responsible for:

• creating the FastAPI app
• registering routers
• starting the backend server

---

### routers/

Contains API endpoints.

#### ingest_router.py

Handles **PDF ingestion**.

Endpoint:

```
POST /ingest
```

Uploads PDF and processes educational content.

---

#### quiz_router.py

Handles **quiz generation and retrieval**.

Provides quiz questions based on extracted content.

---

#### student_router.py

Handles **student answer submission**.

Endpoint:

```
POST /student/submit
```

Evaluates answers and calculates the score.

---

### services/

Contains core application logic.

#### ingest_pdf.py

Responsible for:

• PDF text extraction
• content chunking
• preparing data for quiz generation

---

#### quiz_service.py

Generates **multiple choice questions** from content chunks.

---

#### student_service.py

Evaluates student responses and computes scores.

---

# 💾 Data Storage

In this prototype implementation, the system uses **in-memory storage** for:

• quiz questions
• correct answers
• content chunks

During runtime, these objects are stored inside the **service layer**.

For production systems, the architecture can easily integrate with databases such as:

• MongoDB
• PostgreSQL
• Vector Databases (for semantic search)

---

# ⚙ Installation & Setup

## 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/peblo-quiz-engine.git
cd peblo-quiz-engine
```

---

## 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

Required packages include:

```
fastapi
uvicorn
python-multipart
pydantic
```

---

## 3️⃣ Run the Server

```
uvicorn app.main:app --reload --port 8001
```

---

## 4️⃣ Open API Documentation

```
http://127.0.0.1:8001/docs
```

Swagger UI will open where all APIs can be tested.

---

# 🔌 API Endpoints

---

## 📄 Upload Educational Content

```
POST /ingest
```

Uploads a PDF file and processes its content.

---

## ❓ Generate Quiz

```
GET /quiz
```

Returns generated quiz questions.

---

## 👨‍🎓 Submit Student Answers

```
POST /student/submit
```

Evaluates answers and returns the score.

Example response:

```
{
 "score": 2,
 "total": 3
}
```

---

# 🎬 Demo Workflow

The typical workflow is:

1️⃣ Upload an educational PDF
2️⃣ Extract text from the document
3️⃣ Generate quiz questions
4️⃣ Student attempts the quiz
5️⃣ Student submits answers
6️⃣ Backend evaluates answers and returns score

---

# 📊 Example Quiz

Example generated question:

**Question:**
Choose the correct plural form of *child*.

Options:

A. Childs
B. Children
C. Childrens

Correct Answer:

```
Children
```

---

# 🔑 Key Concepts Demonstrated

This project demonstrates several important concepts:

• REST API design
• backend modular architecture
• educational content processing
• automated quiz generation
• student response evaluation
• scalable backend systems

---

# 🚀 Future Improvements

Potential enhancements include:

📊 Student performance analytics
🤖 AI-based question generation using LLMs
📱 Web or mobile quiz interface
🧠 semantic search using vector databases
📚 support for multiple document formats

---

# 🤝 Contribution

Contributions are welcome.

You can improve this project by:
• adding AI question generation
• integrating a database
• creating a frontend quiz interface

---
# ⭐ Final Note
Peblo Quiz Engine demonstrates how **educational content can be transformed into automated quizzes using backend APIs and content processing techniques**, providing a scalable foundation for intelligent learning systems.


