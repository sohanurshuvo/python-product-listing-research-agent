# 🐍 Python E-Commerce Product Research & Listing Agent

A lightweight, **zero-dependency Python 3** automation tool with both a **Tkinter Desktop GUI** and CLI runner. Built for e-commerce Virtual Assistants and store managers to validate product profitability, check budget constraints, calculate conversion baselines, and generate ready-to-upload CSV catalogs.

## ✨ Key Features
- **Zero External API Costs:** Runs 100% locally using Python's built-in standard libraries (`tkinter`, `csv`, `json`).
- **Profit & ROI Calculator:** Evaluates unit cost, selling price, ad spend, and net profit against target budget thresholds.
- **Automated SKU & Listing Formatter:** Generates clean SKUs, SEO titles, and structured CSV exports for bulk store uploads.
- **Desktop GUI Runner (`gui_runner.py`):** User-friendly interface for non-technical VA teams to import CSVs and run batch evaluations with one click.

## 📂 Project Structure
- `main.py` – Core decision engine for profit validation, ROI scoring, and listing generation.
- `gui_runner.py` – Desktop graphical interface built with Tkinter.
- `test_cases.json` – Sample product evaluation dataset.

## ▶️ How to Run
```bash
# Run the Desktop GUI
python gui_runner.py

# Or run CLI batch test
python main.py
