# Actions Server Deploy on Kubernetes
The below outlines how to deploy this on kubernetes via helm using the [Rasa Helm Chart](https://github.com/RasaHQ/helm-charts/tree/main/charts/rasa-action-server)

The main thing you will need is a export/env var called `API_KEY` which is basically the Nasa API key for the APOD trigger.

This can be generated at [Nasa API](https://api.nasa.gov/).

You will also need to install [Helm](https://helm.sh/docs/helm/helm_install/) if you haven't already.

## Deploying
Once you have your API key then you need to export it on the CLI:

`export API_KEY=xxxx`

Add the Rasa helm repo:

`helm repo add rasa https://helm.rasa.com`

Then do a update for good measure:

`helm repo update`

Now we can install our action server into our kubernetes cluster via:

`helm install -f values.yaml rasa-action rasa/rasa-action-server`

If you already have it installed then you can run:

`helm upgrade --reuse-values -f values.yaml rasa-action rasa/rasa-action-server`