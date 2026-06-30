# Flask CI/CD Pipeline Project

This project establishes automated CI/CD automation processes utilizing Jenkins Pipelines and GitHub Actions.

## Prerequisites
- Python 3.10+
- Jenkins Server with Python ecosystem plugins installed
- GitHub Account

## Jenkins Pipeline Setup
1. Define a new **Pipeline project** inside your Jenkins server dashboard.
2. Configure a Build Trigger for **GitHub hook trigger for GITScm polling** to catch main branch changes automatically.
3. Set the Pipeline definition to **Pipeline script from SCM**, pick Git, and point to your project URL.

## GitHub Actions Configuration
The system uses automated environment rules contingent on branches:
- **Staging Branch Push**: Triggers test, package validation, and execution deployments directly to the staging layer.
- **Tagged Release (`v*`)**: Initiates final deployments to production systems.

### Configuration Secrets
Ensure you register the following configurations in **Settings -> Secrets and variables -> Actions** inside GitHub:
- `STAGING_API_TOKEN`: Integration authorization token for staging environments.
- `PROD_DEPLOY_KEY`: SSH or API infrastructure parameters targeting production networks.
