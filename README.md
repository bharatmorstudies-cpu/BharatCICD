\# Flask CI/CD Web Application



A Python Flask application featuring fully integrated CI/CD pipelines through Jenkins and GitHub Actions.



\## Prerequisites

\- Python 3.8+

\- Jenkins Server

\- GitHub Account



\## Installation \& Local Execution

1\. Install dependencies:

&#x20;  ```bash

&#x20;  pip install -r requirements.txt

&#x20;  ```

2\. Run local tests:

&#x20;  ```bash

&#x20;  pytest

&#x20;  ```

3\. Boot the application:

&#x20;  ```bash

&#x20;  python app.py

&#x20;  ```



\## CI/CD Workflow Detail

\- \*\*Jenkins Pipeline\*\*: Triggers automatically on changes. It builds the virtual environment, fires `pytest`, and handles staging deployment simulation.

\- \*\*GitHub Actions\*\*: 

&#x20; - Pushing to `staging` initiates a deployment workflow to staging.

&#x20; - Publishing a release tag triggers a deployment workflow to production.



