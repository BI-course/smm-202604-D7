# Lab Submission Instructions

## Student Details and Individual Member Contributions

**Name of the team on GitHub Classroom:** smm-202604-D7

**Member 1:**

| **Details**                                                                                                                           | **Comment** |
|:--------------------------------------------------------------------------------------------------------------------------------------|:------------|
| **Student ID**                                                                                                                        | 151109 |
| **Name**                                                                                                                              | Emmanuel Ogaro |
| **What part of the lab did you personally<br/>contribute to (provide a link to the<br/>branch(es)), and what did you learn from it?** | Branch: [feature/151109-regression](https://github.com/BI-course/smm-202604-D7/tree/feature/151109-regression).<br/><br/>I replaced the sample SME revenue route with Group D's farm income model. The endpoint is `/api/v1/models/farm-income-regressor/predictions`. It loads `model/farm_income_model.joblib` at startup, takes the farm features as JSON, and returns the predicted annual income in KES from the saved Ridge pipeline. If a required field is missing, it returns HTTP 400 and lists the missing fields. I also added a sample request and response to the README. I learned how to serve a fitted scikit-learn pipeline from a file in Flask, without retraining it, and how to check the request body against the columns the model expects. |

**Member 2:**

| **Details**                                                                                                                           | **Comment** |
|:--------------------------------------------------------------------------------------------------------------------------------------|:------------|
| **Student ID**                                                                                                                        | 166910 |
| **Name**                                                                                                                              | Sol Ikamar |
| **What part of the lab did you personally<br/>contribute to (provide a link to the<br/>branch(es)), and what did you learn from it?** | Branch: [feature/166910-classification](https://github.com/BI-course/smm-202604-D7/tree/feature/166910-classification).<br/><br/>I added the invoice payment risk classifier endpoint at `/api/v1/models/invoice-payment-risk-classifier/predictions`. It loads the saved imblearn pipeline (`model/invoice_payment_risk_classifier.joblib`) once when the API starts and returns the predicted category (On-Time, Late, or Severely Late) together with the class probabilities. A request that is missing required fields gets HTTP 400 and a list of those fields. I also wrote a README section with a sample curl command and response. I learned how to expose a pre-trained classification pipeline, including one that used ADASYN only during training, as a JSON API without fitting anything at runtime. |

**Member 3:**

| **Details**                                                                                                                           | **Comment** |
|:--------------------------------------------------------------------------------------------------------------------------------------|:------------|
| **Student ID**                                                                                                                        | 158393 |
| **Name**                                                                                                                              | Dilcon Kihoro |
| **What part of the lab did you personally<br/>contribute to (provide a link to the<br/>branch(es)), and what did you learn from it?** | Branch: [feature/158393-clustering](https://github.com/BI-course/smm-202604-D7/tree/feature/158393-clustering).<br/><br/>I added the farmer segmentation endpoint at `/api/v1/models/farmer-segmenter/predictions`. It loads `model/farmer_clustering_pipeline.joblib`, which holds the fitted imputer, scaler and K-Means model (k=2), and returns the cluster number plus the segment name (Smallholder Farmers or Established Commercial Farmers). Missing required fields return HTTP 400. I also added a sample request and response to the README. I learned how to serve a clustering pipeline so a new farmer can be assigned to an existing segment without re-running K-Means in the API. |

**Member 4:**

| **Details**                                                                                                                           | **Comment** |
|:--------------------------------------------------------------------------------------------------------------------------------------|:------------|
| **Student ID**                                                                                                                        | 168873 |
| **Name**                                                                                                                              | Shantelle Nkatha |
| **What part of the lab did you personally<br/>contribute to (provide a link to the<br/>branch(es)), and what did you learn from it?** | Branch: [feature/168873-recommender](https://github.com/BI-course/smm-202604-D7/tree/feature/168873-recommender).<br/><br/>I added the food delivery recommender endpoint at `/api/v1/models/food-delivery-recommender/predictions`. It loads the precomputed Apriori association rules from `model/food_delivery_recommendation_rules.joblib`, takes a cart of item IDs, and returns ranked product recommendations. If the cart is missing or empty, the endpoint returns a clear error; if no rule matches, it returns an empty list with a short message. I learned how to serve association rules from a saved lookup, instead of running Apriori again inside the API. |

**Member 5:**

| **Details**                                                                                                                           | **Comment** |
|:--------------------------------------------------------------------------------------------------------------------------------------|:------------|
| **Student ID**                                                                                                                        | 170186 |
| **Name**                                                                                                                              | Hassan Kulubya |
| **What part of the lab did you personally<br/>contribute to (provide a link to the<br/>branch(es)), and what did you learn from it?** | Branches: [feature/170186-deployment](https://github.com/BI-course/smm-202604-D7/tree/feature/170186-deployment) and [integration/all-four-models](https://github.com/BI-course/smm-202604-D7/tree/integration/all-four-models).<br/><br/>I merged the four model branches on `integration/all-four-models`, fixed the README conflict, and added the missing recommender documentation. On `feature/170186-deployment` I set up Docker Compose so the same unmodified `api.py` runs with Gunicorn behind an Nginx reverse proxy, and I deployed that API to Render at https://smm-202604-d7-api.onrender.com. I learned how to put a Flask API behind Nginx in Docker, how to pin the Python and package versions so the saved joblib models still load, and how to publish the same app as a public Render web service. |

## Chosen Level of Difficulty

**Specify the chosen level of difficulty** (baseline, intermediate, or advanced): Intermediate

## Video Demonstration

Submit the link to a short video (**not more than 10 minutes**) demonstrating your complete solution at whichever difficulty level you chose. Please ensure that the lecturer has rights to view the video.

At minimum, the video must show, in one continuous walkthrough:

1. `api.py` running **locally**, with a live request/response against each model endpoint you implemented.
2. If you attempted the Intermediate or Advanced tier: the same API running inside its **Gunicorn + Nginx Docker container**, reached through the reverse proxy, not the Flask development server.
3. If you attempted the Advanced tier: your **Hugging Face Space** and your **Streamlit Community Cloud app**, each opened live in a browser, with at least one prediction made on each tab, and your **Render**-hosted API answering a request from Postman or `curl`.

**Why this matters for grading:** free-tier public deployments are not guaranteed to still exist by the time this is graded. The video is treated as the authoritative record of what was actually working at submission time; a broken link at grading time is not penalized if the video clearly shows that deployment working.

Note that you are required to submit the link to the video and NOT the video itself. The video should NOT be uploaded to your repository—that would be a misuse of GitHub.

**Link to the video:** [ADD VIDEO LINK HERE]

## Public URLs

Fill in only the rows that apply to your chosen difficulty level (see Part C below). Leave a row blank if your tier does not require that deployment target.

| **Deployment target**                             | **URL** |
|:--------------------------------------------------|:--------|
| Render (the full `api.py`, all endpoints)         | https://smm-202604-d7-api.onrender.com<br/>POST paths: `/api/v1/models/farm-income-regressor/predictions`, `/api/v1/models/invoice-payment-risk-classifier/predictions`, `/api/v1/models/farmer-segmenter/predictions`, `/api/v1/models/food-delivery-recommender/predictions` |
| Hugging Face Space (Gradio, one tab per model)    |         |
| Streamlit Community Cloud app (one tab per model) |         |

---

## Scenario

Across earlier labs, **your group** was assigned its own dataset and trained your own models for four distinct tasks:

1. A **regression** task
2. A **classification** task
3. A **k-Means clustering** task
4. An **Apriori association-rule mining** task

Different groups worked with different datasets and, in some cases, different algorithms for each task -- there is no single shared reference repository or model list for the whole class. Wherever this document refers to "your regressor," "your classifier," "your clustering model," or "your recommender," it means **whichever model your own group already trained and saved for that task**, not a specific named algorithm.

You are now required to build a single Flask API (`api.py`) that serves **your own group's four models**, loaded from disk (never retrained inside `api.py`), and to demonstrate that API running correctly across a growing number of deployment surfaces depending on the difficulty tier you choose.

### Part A: Regression and Classification

- Locate the trained regression and classification model files your group produced and saved in your earlier labs on Regression and Classification.
- Update [api.py](api.py) to include end-points that load these two models from disk and serve predictions from them.

### Part B: Clustering and Association Rule Mining

- Locate the trained clustering model and the association rules your group produced and saved in your earlier labs on Clustering and Association Rule Mining.
- Update [api.py](api.py) to include end-points that:
  - Load the clustering model from disk and predict which cluster a new client belongs to
  - Load the association rules from disk and recommend products based on them

**Note 1:** **`api.py` is NOT production-grade as it is.** It is only meant for demonstration purposes. Scalability and security must be taken into consideration before deploying an API in a production environment.

**Note 2:** Some students often treat the API as an afterthought, focusing only on training ML models. In practice, **the API is the product** -- it is how others interact with your model. The "hidden" learning here is that the delivery mechanism (API design, usability, error handling, and even documentation) often matters more to stakeholders in the industry than the models themselves.

### Part C: Deployment Breadth (Read Before Choosing Your Tier)

All three tiers below ask you to serve **the same four models** (your regressor, your classifier, your clustering model, your recommender) from **one, unmodified `api.py`**. The model files and the Flask routes do not change between tiers -- only how many different places that one working API is shown to run correctly.

**Baseline (Required):**

- Update `api.py` to serve **at least three of your four** models, loaded from disk.
- Run and demonstrate `api.py` **locally** with Flask's development server, with a successful request against each implemented endpoint.

**Intermediate (Recommended):**

- Update `api.py` to serve **all four** of your models, loaded from disk.
- Dockerize your Flask API using **Gunicorn**, and place it behind an **Nginx** reverse proxy (see the reverse-proxy lab notes for the full Docker Compose setup).
- Deploy the same, unmodified `api.py` to **Render**, and demonstrate a real request against it from outside your own machine (cURL or Postman).

**Advanced (Optional):**

- Everything required for Intermediate, plus:
  - Create a web page (or pages) using Basic HTML, CSS, and Vanilla JavaScript that demonstrates the use of the API
  - Implement basic error handling (e.g., missing inputs)
  - Build **one Gradio app with a tab per model** (all four of your models) and publish it as a **Hugging Face Space**
  - Build **one Streamlit app with a tab per model**, covering the same four models, and publish it on **Streamlit Community Cloud**
  - All deployment targets -- local, Dockerized/Nginx, Render, Hugging Face, and Streamlit -- must serve models loaded **from the same trained artifacts**; retraining different models per platform does not satisfy this requirement

Why this is production-relevant beyond the model itself:

- **Portability:** the same container image and the same trained artifacts run unmodified on your laptop, inside Docker, and on a managed cloud host.
- **Consistency:** no "but it works on my machine" gap between what you demo locally and what a domain expert sees on a public URL.
- **Separation of concerns:** a REST API (Render), a no-code demo UI (Hugging Face/Streamlit), and your own frontend (the Advanced-tier HTML pages) are three different ways of exposing the *same* underlying models to three different kinds of user -- a developer integrating your API, a non-technical domain expert validating it, and an end customer.

---

## Marking Guide

Refer to the marking guide available here: [lab_submission_marking_guide.md](lab_submission_marking_guide.md)