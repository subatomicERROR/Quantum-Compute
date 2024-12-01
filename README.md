# Quantum-Compute

Quantum-Compute is a robust, modular API service designed to handle quantum computation tasks by integrating various quantum machine learning capabilities. The project combines **Quantum-API**, **Quantum-ML**, and **Quantum-Compute** to facilitate hybrid quantum-classical computations and provide an API interface for easy integration into other applications.

## Features
- Hybrid quantum-classical model for computation.
- Integration with **Quantum-API** and **Quantum-ML** for seamless data processing.
- Provides a simple REST API using **FastAPI** for interacting with quantum models.
- Supports easy deployment and scalability.

## Technologies
- **Quantum-ML**: A hybrid quantum-classical machine learning model, using **PennyLane** for quantum computations and **PyTorch** for classical machine learning.
- **Quantum-API**: Exposes quantum model computations as a REST API using **FastAPI**.
- **Quantum-Compute**: The central API that coordinates quantum computing tasks between Quantum-ML and Quantum-API.

## Installation

### Prerequisites
- Python 3.7 or later
- `pip` (Python package installer)
- A running **Quantum-API** and **Quantum-ML** service

### Step-by-Step Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/subatomicERROR/Quantum-Compute.git
   cd Quantum-Compute
   ```

2. **Create a Virtual Environment**:
   If you haven't already, create a virtual environment to isolate your dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Linux/macOS
   .venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**:
   Install the required packages from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Submodules**:
   The project depends on two submodules: **Quantum-API** and **Quantum-ML**. Ensure they are initialized and updated:
   ```bash
   git submodule update --init --recursive
   ```

5. **Start the Quantum-API and Quantum-ML Services**:
   - Start **Quantum-API** on port 5000:
     ```bash
     cd submodules/Quantum-API
     uvicorn app:app --reload --host 0.0.0.0 --port 5000
     ```
   - Start **Quantum-ML** on port 7000:
     ```bash
     cd submodules/Quantum-ML
     uvicorn main:app --reload --host 0.0.0.0 --port 7000
     ```

6. **Start Quantum-Compute**:
   Start the **Quantum-Compute** API on port 8000:
   ```bash
   cd ..
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```

## Usage

Once the servers are up and running, you can access the following endpoints:

### Root Endpoint
- **GET /**  
  Returns a simple greeting message indicating the API is running.

### Status Endpoint
- **GET /quantum-ai/status**  
  Returns the status of the Quantum AI system.
  - **Response**: `{ "status": "Quantum AI is up and running!" }`

### Prediction Endpoint
- **POST /quantum-ai/predict**
  This endpoint accepts a quantum input and returns predictions from the hybrid quantum-classical model. The request body should be a JSON object with a `input_value` field:
  - **Request Body**:
    ```json
    {
      "input_value": 1.0
    }
    ```
  - **Response**:
    ```json
    {
      "quantum_result": 0.8329,
      "classical_result": 0.7463
    }
    ```

### Subscription Endpoint
- **POST /quantum-ai/subscribe**  
  Allows users to subscribe to the API (simulated for freemium model).
  - **Request Body**:
    ```json
    {
      "user_email": "user@example.com"
    }
    ```
  - **Response**:
    ```json
    {
      "status": "Subscription successful",
      "email": "user@example.com"
    }
    ```

## Testing

To confirm the functionality of each service:
1. Start the servers for **Quantum-API**, **Quantum-ML**, and **Quantum-Compute** as described above.
2. Use `curl`, Postman, or Swagger UI to interact with the API.

Example command to test the Quantum-Compute prediction:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/quantum-ai/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"input_value": 1.0}'
```

## Contributing

Contributions are welcome! To get started:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a new pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

For more information or to contribute, visit the repository at [https://github.com/subatomicERROR/Quantum-Compute](https://github.com/subatomicERROR/Quantum-Compute).

```

### Breakdown of Sections:
1. **Introduction**: Explains the purpose of the Quantum-Compute API.
2. **Technologies**: Lists the key components such as **Quantum-API**, **Quantum-ML**, and **Quantum-Compute**.
3. **Installation**: Detailed steps to clone the repo, set up the virtual environment, install dependencies, and run the services.
4. **Usage**: Describes the key API endpoints and how to use them.
5. **Testing**: Instructions for confirming everything is running correctly.
6. **Contributing**: Explains how others can contribute to the project.
7. **License**: Basic licensing info.

Let me know if you want any adjustments or additions!
