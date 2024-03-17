Arthur PoonMPCS57200 - Generative AIProfessor Michael SpertusMar 6, 2024Final Project Video:
Arthur Poon - GenAI Final Project.mp4

The FinanceBench dataset can be found at:
https://huggingface.co/datasets/PatronusAI/financebench/viewer/default/train?f[question_type][value]=%27metrics-generated%27

FinanceBench original paper:
https://uploads-ssl.webflow.com/64e655d42d3be60f582d0472/65558c28757acd0fa312c5ec_FinanceBench__ACL_%20(3).pdf

Keys for APIs:
keys.env

The python scripts to retreive the 10-Ks in XBRL-JSON format:
10-K_pdf_downloads.py
XBRL_JSON_converter.py

The files can be found in the directories:
10-K_PDFs/
XBRL_JSON_files/

RAG systems using PDF and XBRL as well as the together models can be found in the following files:
small_RAG_SEC_Filings_XBRL_JSON.ipynb
small_RAG_SEC_Filings_XBRL_Together_Embeddings.ipynb
small_RAG_SEC_Filings_XBRL_Together.ipynb
small_RAG_SEC_Filings.ipynb


Outputs of the RAG systems can be found in the following files:
pdf_query_answers.xlsx
XBRL_json_query_answers.xlsx
XBRL_json_query_answers_Together.xlsx