# Amazon FBA UI


# Deploying the UI to GCP Cloud Run

## Prerequisites

- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
- [Docker](https://docs.docker.com/get-docker/)
- Streamlit
- [Google Cloud Project](https://cloud.google.com/resource-manager/docs/creating-managing-projects)

## Steps

1. Build the Docker image

```bash
docker build --no-cache -t fba_ui .
```

2. Test the Image

```bash
docker run -p 8080:8080 fba_ui
```

3. Push the image to Google Container Registry

```bash
gcloud builds submit --tag gcr.io/amazonfba-408406/fba_ui --timeout=2h
```