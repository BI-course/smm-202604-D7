# Serving Machine Learning Models through RESTish APIs using Flask in Python

| Key             | Value                                                                                                                                                                                                                                                                                     |
|:----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Course Code** | BBT 4206                                                                                                                                                                                                                                                                                  |
| **Course Name** | BBT 4206: Business Intelligence II (Week 4-6 of 13)                                                                                                                                                                                                                                       |
| **Semester**    | September to December 2026                                                                                                                                                                                                                                                                |
| **Lecturer**    | Allan Omondi                                                                                                                                                                                                                                                                              |
| **Contact**     | aomondi@strathmore.edu                                                                                                                                                                                                                                                                    |
| **Note**        | The lecture contains both theory and practice.<br/>This notebook forms part of the practice.<br/>It is intended for educational purposes only.<br/>Recommended citation: [BibTex](https://raw.githubusercontent.com/course-files/ServingMLModels/refs/heads/main/RecommendedCitation.bib) |

## Technology Stack

<p align="left">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg" width="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linux/linux-original.svg" width="40" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/nginx/nginx-original.svg" width="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flask/flask-original.svg" width="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postman/postman-original.svg" width="40"/>
<img src="assets/images/gunicorn-logo-png-transparent.png" width="60"/>
<img src="assets/images/Hf-logo-with-title.svg" width="120"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/streamlit/streamlit-original.svg" width="40" />
<img src="assets/images/Render-logo-Black.png" width="100"/>
</p>

## Repository Structure

```text
.
├── LICENSE
├── Procfile
├── README.md
├── RecommendedCitation.bib
├── admin_instructions
│   ├── 0_instructions_for_project_setup.md
│   ├── 1_instructions_for_python_installation.md
│   └── 2_instructions_for_project_teardown.md
├── api.py
├── app_server_reverse_proxy_server_setup.md
├── assets
│   └── images
│       ├── Hf-logo-with-title.svg
│       ├── Render-logo-Black.png
│       ├── Streamlit-logo-primary-colormark-darktext.png
│       ├── gunicorn-logo-png-transparent.png
│       └── ssh_student_at_localhost_p_2222.jpeg
├── cleanup_instructions.md
├── docker-compose-dev.yaml
├── docker-compose-prod.yaml
├── docker-compose.yaml
├── dockerfiles
│   ├── Dockerfile.flask-gunicorn-app
│   ├── Dockerfile.nginx
│   └── ubuntu
│       ├── Dockerfile.ubuntu
│       └── entrypoint.sh
├── env.example
├── frontend
│   ├── Proxies.png
│   ├── RequestFlow.jpg
│   ├── api_consumer.py
│   ├── api_consumer_from_dev_flask.py
│   ├── ecommerce_recommender.html
│   ├── index.html
│   ├── mall_customer_segmenter.html
│   ├── sme_credit_risk_classifier.html
│   └── sme_revenue_regressor.html
├── huggingface-spaces-using-gradio
│   ├── app.py
│   └── requirements.txt
├── lab_submission_instructions.md
├── model
│   ├── apriori_recommendation_rules.joblib
│   ├── kmeans_mall_customer_segmentation.joblib
│   ├── lasso_regressor_for_sme_revenue.joblib
│   └── svc_classifier_for_sme_credit_risk.joblib
├── publicly_serving_the_model_for_validation_by_domain_experts.md
├── requirements
│   ├── base.txt
│   ├── colab.txt
│   ├── constraints.txt
│   ├── dev.inferred.txt
│   ├── dev.lock.txt
│   ├── dev.txt
│   └── prod.txt
├── rules
├── runtime.txt
└── streamlit-sharing-using-streamlit
    ├── app.py
    └── requirements.txt

12 directories, 50 files
```

## Setup Instructions

- [Setup Instructions](./admin_instructions/0_instructions_for_project_setup.md)

## Lab Manual

Refer to the files below, in the order specified, for more details:

1. [api_consumer.py](frontend/api_consumer.py) ← How to use `requests` in Python
2. [api.py](api.py) ← How to create a RESTish API using Flask in Python
3. [api_consumer_from_dev_flask.py](frontend/api_consumer_from_dev_flask.py) ← How to consume the RESTish API from a Flask development server
4. [index.html](frontend/index.html) ← Example of a frontend (HTML, CSS, and JS) that consumes from the API endpoint
5. [Reverse Proxy Server and Application Server Setup](app_server_reverse_proxy_server_setup.md) ← How to use Nginx as a reverse proxy server to serve the Flask application through Gunicorn
6. [Publicly Serving the Model for Validation by Domain Experts](publicly_serving_the_model_for_validation_by_domain_experts.md) ← How to serve the model through Hugging Face, Streamlit, and Render

## Regression

Send a `POST` to `/api/v1/models/farm-income-regressor/predictions` with a JSON
object containing every input column used by the fitted farm-income pipeline.
The API loads `model/farm_income_model.joblib` at startup and returns the
predicted annual income in KES.

In Postman, send the following JSON body to
`http://127.0.0.1:5000/api/v1/models/farm-income-regressor/predictions`.

```json
{
  "years_farming_experience": 12,
  "soil_quality_score": 65,
  "market_distance_km": 8,
  "num_workers_employed": 3,
  "crop_type": "Coffee",
  "county": "Kericho",
  "irrigation_type": null,
  "cooperative_member": "No"
}
```

The response is HTTP 200.

```json
{"model": "Ridge Regressor", "predicted_annual_farm_income_kes": 226728.09}
```

If you omit `crop_type`, the response is HTTP 400.

```json
{"error": "Missing required fields.", "missing_fields": ["crop_type"]}
```

Export the fitted pipeline with the scikit-learn version pinned in
`requirements/constraints.txt`.

## Lab Submission Instructions

- [Lab Submission Instructions](lab_submission_instructions.md)

## Cleanup Instructions (to be done after submitting the lab)

- [Cleanup Instructions](/admin_instructions/2_instructions_for_project_teardown.md)

## Classification

Group D's classification model predicts the payment risk category of a B2B invoice (`On-Time`, `Late` or `Severely Late`). The model is the full `imblearn` pipeline (preprocessing, ADASYN resampling at training time only, and a tuned Logistic Regression) saved as `model/invoice_payment_risk_classifier.joblib`. It is loaded once at startup in `api.py` and is never retrained there.

**Endpoint:** `POST /api/v1/models/invoice-payment-risk-classifier/predictions`

All fields are required except `guarantee_value_kes`, which may be `null` or omitted (it is structurally missing when an invoice has no collateral or guarantee).

**Sample request**

```bash
curl -X POST http://127.0.0.1:5000/api/v1/models/invoice-payment-risk-classifier/predictions \
  -H "Content-Type: application/json" \
  -d '{"client_industry": "Technology", "client_credit_rating": "Good", "client_company_size": "Medium", "payment_method": "Bank Transfer", "has_dispute_history": "No", "collateral_or_guarantee": "No", "payment_terms_days": 30, "invoice_amount_kes": 350000, "client_relationship_years": 4.5, "prior_late_payments_count": 0, "discount_offered_pct": 1.5, "days_outstanding_avg_historical": 25, "guarantee_value_kes": null, "economic_sector_growth_rate_pct": 2.5}'
```

**Sample response (200)**

```json
{
  "class_probabilities": {
    "Late": 0.0383,
    "On-Time": 0.9617,
    "Severely Late": 0.0
  },
  "model": "Logistic Regression (tuned, ADASYN-resampled at training only)",
  "predicted_payment_risk_category": "On-Time"
}
```

**Sample response when required fields are missing (400)**

```json
{
  "error": "Missing required field(s).",
  "missing_fields": [
    "client_credit_rating",
    "client_company_size",
    "payment_method"
  ]
}
```
