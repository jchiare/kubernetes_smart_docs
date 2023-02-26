# Kubernetes Smart Docs Readme

Welcome to the Kubernetes Smart Doc! This document provides instructions on how to use and deploy the Kubernetes Smart Doc

## Introduction

The Kubernetes Smart Doc is a tool that enables you to ask questions, and receive (hopefully) helpful replies back about the Kubernetes Content document.

Workflow is:

1. Ask a question, for example
   > When should I use a Stateful State over a Deployment?
2. Kubernetes Smart Doc will prompt an AI to reply to the question, using articles from the Kubernetes Official Content document as the source

## Prerequisites

Before deploying the Kubernetes Smart Doc, you should have the following prerequisites:

- Python installed locally, version `3.10.8` was used during development
- OpenAI API key set under the env var `OPENAI_API_KEY`

## Usage

Install dependencies

1. `pip install -r requirements.txt`

Run the flask app in development mode

2. `flask --app kubernetes_smart_docs/app run`

## Todo

- [ ] A LOT!
- [ ] Unit/Integration test on flask server
- [ ] Caching for API requests
- [ ] Save word embedding in DB instead of csv
- [ ] Use a modern frontend instead of vanilla JS
- [ ] Add formatting / linting

### License

The Kubernetes Smart Doc is licensed under the MIT license. See the LICENSE file for details.
