
# Swagger API Chatbot

A Python & FastAPI based chatbot that reads Swagger (OpenAPI) JSON specs and interacts with users  
to perform API operations by understanding natural language requests.

---

## Features

- Parses Swagger JSON files to extract endpoints and required parameters  
- Uses NLP to match user intents to API endpoints  
- Interactive multi-step form filling for API requests  
- Frontend integration planned with React for UI and buttons  
- Easily extendable for different Swagger-defined APIs  

---

## Project Structure

- `swagger_specs/` - Swagger JSON specification files  
- `extract_endpoints.py` - Extracts API endpoints & parameters from Swagger JSON  
- `match_intent.py` - Matches user text input to API endpoints using similarity  
- `chatbot_backend/` - FastAPI backend code (to be developed)  
- `frontend/` - React frontend (planned)

---

## Getting Started

### Prerequisites

- Python 3.8+  
- FastAPI  
- (Optional) NLP libraries like `sentence-transformers` or OpenAI API key for advanced intent matching

### Installation
``` bash
1. Clone the repo  
> git clone https://github.com/yourusername/swagger-api-chatbot.git  
> cd swagger-api-chatbot

2. Create and activate virtual environment  
> python -m venv myvenv  
> source myvenv/bin/activate  # Linux/macOS  
> myvenv\Scripts\activate     # Windows

3. Install dependencies  
> pip install -r requirements.txt

4. Run extraction and matching scripts  
> python extract_endpoints.py  
> python match_intent.py

---

## How to Use

- Put your Swagger JSON files inside `swagger_specs/`  
- Run `extract_endpoints.py` to see available endpoints  
- Run `match_intent.py` to interactively match user requests to endpoints  

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---


## Contact

Your Ava Iranpour - a.iranpour8808.nia@gmail.com 
Project Link: https://github.com/yourusername/swagger-api-chatbot

