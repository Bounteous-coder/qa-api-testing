# QA API Testing Portfolio Project

This project demonstrates QA analyst readiness using API test design, automation, and defect-style artifacts.

## Stack

- Python 3.11+
- pytest
- requests

## Target API

- JSONPlaceholder: https://jsonplaceholder.typicode.com

## Scope

- Positive, negative, and edge-case tests
- Basic response schema checks
- Latency threshold checks for a sample endpoint
- 20-case matrix implemented with pytest parameterization

## Project Structure

- src/api_client.py: lightweight API wrapper
- tests/: test cases
- jira/: test artifacts for Jira ticket mapping

## Setup

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
pytest -q
```

## Recruiter Evidence Checklist

- 15-20 test cases tracked in Jira
- Defect examples documented
- Test execution proof (pytest output screenshot)
