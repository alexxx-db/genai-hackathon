# GenAI Hackathon - Agentic AI Project

This repository contains the codebase for the Agentic AI Hackathon project. The project focuses on leveraging Large Language Models (LLMs) to create intelligent, agentic solutions for pharmaceutical research and development.

## Project Overview

This project aims to demonstrate the potential of agentic AI in pharmaceutical research and development through the implementation of intelligent systems that can:
- Process and analyze complex pharmaceutical data
- Assist in research decision-making
- Automate routine tasks in drug discovery
- Enhance collaboration between researchers

## Getting Started

### Prerequisites

- Databricks Serverless Runtime
- Git
- Databricks workspace access

### Environment Setup

1. **Notebook Configuration**
   - Create a new notebook in your Databricks workspace
   - Set the notebook language to Python
   - Configure notebook parameters:
     ```python
     # At the top of your notebook
     dbutils.widgets.text("input_param1", "default_value1")
     dbutils.widgets.text("input_param2", "default_value2")
     ```
   - Set up notebook-scoped libraries:
     ```python
     %pip install your-required-packages
     ```

### Installation

1. **Git Integration in Databricks**

   a. **Set up Git Credentials in Databricks:**
   - Go to User Settings (click on your username in the top-right)
   - Navigate to Git Integration
   - Click on "Generate New Token" or use existing GitHub token
   - Add your Git provider credentials

   b. **Link Repository to Databricks:**
   - In Databricks workspace, click on "Repos" in the sidebar
   - Click on "Add Repo"
   - Enter your repository URL: `https://github.com/yourusername/llm-hackathon.git`
   - Choose a name for the repo folder
   - Click "Create"
> Your Repo > ⋮ (menu) > Git Actions

2. **Clone repository locally (optional):**
```bash
git clone https://github.com/yourusername/llm-hackathon.git
cd llm-hackathon
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
