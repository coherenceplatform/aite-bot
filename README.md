# Running on Coherence

- Set up the app on [Coherence](https://app.withcoherence.com) by installing the github app and configuring your fork of this repo, and linking your cloud account on GCP or AWS, following the Coherence onboarding wizard
- Set the `OPENAI_API_KEY` variable in your app to the value from your `OpenAI` account
- Visit the URL on your initial Coherence environment!

# Running the App on Cloud Shell
First need to set up git SSH key on Cloud Shell (https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

- Clone the repo e.g. `git clone git@github.com:coherenceplatform/aite-bot.git`
- `cd aite-bot`
- `docker build -t aite .`
- `docker run --rm -it --entrypoint bash -v $(pwd):/app aite`
- `docker run --rm -it --entrypoint bash -v $(pwd):/app -p 8080:8080 aite -c "python app.py"`
- Use the web preview in the top right