
# Specmatic Sample: Python-Flask BFF

* [Specmatic Website](https://specmatic.io)
* [Specmatic Documentation](https://specmatic.io/documentation.html)

This example project illustrates the practice of contract-driven development and contract testing within a Flask (Python) application that relies on an external domain service. In this context, Specmatic is utilized to stub calls to domain API services according to its OpenAPI specification.

Here is the Domain [OpenAPI spec](https://github.com/specmatic/specmatic-order-contracts/blob/main/io/specmatic/examples/store/openapi/api_order_v3.yaml)

Here is the BFF [OpenAPI spec](https://github.com/specmatic/specmatic-order-contracts/blob/main/io/specmatic/examples/store/openapi/product_search_bff_v4.yaml)

## Definitions

* BFF: Backend for Frontend
* Domain API: API managing the domain model
* Specmatic Stub/Mock Server: Generate a server that simulates a real service using its OpenAPI or AsyncAPI specification

## Background

A standard web application setup may resemble the following structure. By leveraging Specmatic, we can engage in contract-driven development and perform comprehensive testing on all the components listed below. In this illustrative project, we demonstrate the process for a Flask BFF, which relies on the Domain API Service, showcasing OpenAPI support within **Specmatic**.

![HTML client talks to client API which talks to backend API](assets/specmatic-order-bff-architecture.gif)

## Tech

1. Flask
2. Specmatic
3. PyTest
4. Coverage

## Setup

1. Install [Python 3.12](https://www.python.org/)
2. Install JRE 17 or later.

## Setup Virtual Environment

1. ### Create a virtual environment named ".venv" by executing the following command in the terminal from the project's root directory

   ```shell
    python -m venv .venv
    ```

2. ### Activate virtual environment by executing

* **on MacOS and Linux**

   ```shell
   source .venv/bin/activate
   ```

* **on Windows CMD**

  ```cmd
  .venv\Scripts\activate.bat
  ```

* **on Windows Powershell (you may need to adjust the ExecutionPolicy)**

  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```

## Install Dependencies

To install all necessary dependencies for this project, navigate to the project's root directory in your terminal and execute

```shell
pip install -r requirements.txt
```

## Execute Tests and Validate Contracts with Specmatic

Executing this command will initiate Specmatic and execute the tests on the Flask application.

```shell
pytest test -v -s
```
