# 🧠 Knowledge Crew

> A multi-agent AI research assistant powered by [crewAI](https://crewai.com) that reads academic PDFs and produces structured, factual summaries.

![Python](https://img.shields.io/badge/Python-3.10%E2%80%933.13-blue?logo=python&logoColor=white)
![crewAI](https://img.shields.io/badge/crewAI-1.9.3-orange)
![License](https://img.shields.io/badge/License-Unlicensed-lightgrey)

---

## ✨ What It Does

Knowledge Crew automates the process of reading and summarizing research papers using AI agents. Give it a PDF and a query, and it will:

1. **Read** — Parse and search through the provided PDF using `PDFSearchTool`
2. **Understand** — Interpret your query and retrieve relevant sections from the document
3. **Summarize** — Generate a well-structured Markdown report with factual bullet points

### Example

Out of the box, it processes a survey paper on In-Context Learning (ICL) and answers:

> *"What is scoring function and what are the different scoring functions used in the paper?"*

The output is saved to `report.md` with structured findings on Direct Method, Perplexity (PPL), and Channel Model scoring functions.

---

## 📁 Project Structure

```
knowledge_crew/
├── knowledge/                          # Knowledge sources for the crew
│   ├── survey_on_icl.pdf               # Research paper (Survey on ICL)
│   └── user_preference.txt             # User preference context
├── src/
│   └── knowledge_crew/
│       ├── config/
│       │   ├── agents.yaml             # Agent role, goal & backstory definitions
│       │   └── tasks.yaml              # Task descriptions & expected outputs
│       ├── tools/                      # Custom tools (extensible)
│       ├── __init__.py
│       ├── crew.py                     # Crew orchestration & agent/task wiring
│       └── main.py                     # Entry point — define your query here
├── report.md                           # Generated output report
├── pyproject.toml                      # Project metadata & dependencies
├── uv.lock                            # Locked dependency versions
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

- **Python** >= 3.10, < 3.14
- **[uv](https://docs.astral.sh/uv/)** — fast Python package manager
- An **OpenAI API key** (or compatible LLM provider)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/imdwnyn/knowledge_crew.git
   cd knowledge_crew
   ```

2. **Install uv** (if not already installed)

   ```bash
   pip install uv
   ```

3. **Install dependencies**

   ```bash
   crewai install
   ```

4. **Set up your environment**

   Create a `.env` file in the project root:

   ```env
   OPENAI_API_KEY=your-api-key-here
   ```

---

## ▶️ Usage

### Run the crew

```bash
crewai run
```

This will execute the research summarization crew and output the results to `report.md`.

### Available Commands

| Command | Description |
|---------|-------------|
| `crewai run` | Run the crew with the default query |
| `crewai train` | Train the crew agents |
| `crewai replay` | Replay the last crew execution |
| `crewai test` | Test the crew |

---

## ⚙️ Customization

### Change the Research Query

Edit the query in `src/knowledge_crew/main.py`:

```python
inputs = {
    'query': 'Your custom research question here'
}
```

### Use a Different PDF

1. Place your PDF in the `knowledge/` directory
2. Update the tool path in `src/knowledge_crew/crew.py`:

   ```python
   tools=[PDFSearchTool(pdf="knowledge/your_paper.pdf")]
   ```

### Modify Agents

Edit `src/knowledge_crew/config/agents.yaml` to adjust agent roles, goals, and backstories.

### Modify Tasks

Edit `src/knowledge_crew/config/tasks.yaml` to change task descriptions and expected outputs.

---

## 🔧 Tech Stack

| Dependency | Purpose |
|------------|---------|
| [crewAI](https://github.com/crewAIInc/crewAI) `1.9.3` | Multi-agent orchestration framework |
| [crewai-tools](https://github.com/crewAIInc/crewAI-tools) | PDF search & other agent tools |
| [NumPy](https://numpy.org/) `>=2.2.6` | Numerical computing (embedding support) |
| [Qdrant Client](https://github.com/qdrant/qdrant-client) `>=1.17.0` | Vector database for knowledge retrieval |
| [Hatchling](https://hatch.pypa.io/) | Build system backend |

---

## 🗺️ Roadmap

- [ ] Add support for multiple PDF sources simultaneously
- [ ] Enable knowledge sources via `PDFKnowledgeSource` with Qdrant vector storage
- [ ] Add more agent types (e.g., fact-checker, citation extractor)
- [ ] Implement a CLI for interactive query input
- [ ] Add support for additional document formats (DOCX, HTML, etc.)

---

## 🤝 Acknowledgments

- **[crewAI](https://crewai.com)** — The multi-agent framework powering this project
- **Survey on In-Context Learning** — The included research paper used as a knowledge source

---

## 📚 Resources

- [crewAI Documentation](https://docs.crewai.com)
- [crewAI GitHub](https://github.com/crewAIInc/crewAI)
- [crewAI Discord Community](https://discord.com/invite/X4JWnZnxPb)