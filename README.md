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

## Clustering

Group D's clustering model segments farmers of an agricultural cooperative into two groups with K-Means (k = 2): `Smallholder Farmers` (cluster 0) and `Established Commercial Farmers` (cluster 1). The saved artifact `model/farmer_clustering_pipeline.joblib` holds the fitted imputer, scaler and K-Means model, and is loaded once at startup in `api.py`. Nothing is retrained there.

**Endpoint:** `POST /api/v1/models/farmer-segmenter/predictions`

`farm_size_acres`, `annual_yield_tonnes`, `income_per_acre_kes` and `years_farming_experience` are required. `market_access_score` is optional (missing values are filled with the training median).

**Sample request**

```bash
curl -X POST http://127.0.0.1:5000/api/v1/models/farmer-segmenter/predictions \
  -H "Content-Type: application/json" \
  -d '{"farm_size_acres": 4.5, "annual_yield_tonnes": 9.8, "income_per_acre_kes": 42000, "years_farming_experience": 6, "market_access_score": 55}'
```

**Sample response (200)**

```json
{
  "assigned_cluster": 0,
  "model": "K-Means (k=2, median-imputed, standardized features)",
  "segment": "Smallholder Farmers"
}
```

**Sample response when required fields are missing (400)**

```json
{
  "error": "Missing required field(s).",
  "missing_fields": [
    "annual_yield_tonnes",
    "income_per_acre_kes",
    "years_farming_experience"
  ]
}
```

## Recommender

Group D's recommender uses Apriori association rules mined from food-delivery orders and saved as `model/food_delivery_recommendation_rules.joblib`. The artifact is a precomputed lookup (antecedent item-set to ranked candidate items) plus a SKU-to-name map. It is loaded once at startup in `api.py`. Apriori is never re-run there.

**Endpoint:** `POST /api/v1/models/food-delivery-recommender/predictions`

`cart` is required and must be a non-empty list of item IDs (for example `F10` for Chicken Biryani). `top_n` is optional and defaults to 3.

**Sample request**

```bash
curl -X POST http://127.0.0.1:5000/api/v1/models/food-delivery-recommender/predictions \
  -H "Content-Type: application/json" \
  -d '{"cart": ["F10", "F11"], "top_n": 3}'
```

**Sample response (200)**

```json
{
  "cart": ["F10", "F11"],
  "model": "Apriori association rules, cleaned + precomputed lookup",
  "recommendations": [
    {
      "confidence": 0.926,
      "lift": 5.21,
      "product_name": "Naan Bread",
      "sku": "F12"
    }
  ]
}
```

If no rule matches the cart, the response is still HTTP 200, with an empty list and a short message:

```json
{
  "cart": ["F15"],
  "message": "No matching rule found for this cart, so there are no recommendations.",
  "model": "Apriori association rules, cleaned + precomputed lookup",
  "recommendations": []
}
```

**Sample response when the cart is missing (400)**

```json
{
  "error": "Missing field: 'cart' is required, for example {\"cart\": [\"F10\", \"F11\"]}"
}
```

## Deployment

This covers the Intermediate-tier work: the same unmodified `api.py` served with Gunicorn behind an Nginx reverse proxy in Docker, and prepared for Render. `api.py` is not edited here. The comment at the top of that file still describes the lecturer's example models; the live routes and the files in `model/` are Group D's.

### Docker + Gunicorn + Nginx (local)

Docker Desktop must be running. A self-signed certificate must already be in `container-volumes/nginx/certs/` (`selfsigned.crt` and `selfsigned.key`). If that folder is empty, generate the certs by following [app_server_reverse_proxy_server_setup.md](app_server_reverse_proxy_server_setup.md).

From the repository root:

```shell
docker compose up --build
```

That uses [compose.yaml](compose.yaml): it builds the API image, starts Gunicorn inside the container (not the Flask development server), and puts Nginx in front on ports 80 and 443. Port 80 redirects to HTTPS. The API port (8000) is only reachable from the Nginx container, not from your machine.

The original two-file lab command still works if you also want the optional Ubuntu teaching container and two API replicas:

```shell
docker compose \
  -f Docker-Compose.yaml \
  -f docker-compose-dev.yaml \
  up --build \
  --scale flask-gunicorn-app=2
docker compose restart nginx
```

Call every endpoint **through Nginx** (the `-k` flag is needed because the certificate is self-signed). Use the sample JSON bodies from the model sections above.

```shell
# Regression
curl -k -X POST https://127.0.0.1/api/v1/models/farm-income-regressor/predictions \
  -H "Content-Type: application/json" \
  -d '{"years_farming_experience": 12, "soil_quality_score": 65, "market_distance_km": 8, "num_workers_employed": 3, "crop_type": "Coffee", "county": "Kericho", "irrigation_type": null, "cooperative_member": "No"}'

# Classification
curl -k -X POST https://127.0.0.1/api/v1/models/invoice-payment-risk-classifier/predictions \
  -H "Content-Type: application/json" \
  -d '{"client_industry": "Technology", "client_credit_rating": "Good", "client_company_size": "Medium", "payment_method": "Bank Transfer", "has_dispute_history": "No", "collateral_or_guarantee": "No", "payment_terms_days": 30, "invoice_amount_kes": 350000, "client_relationship_years": 4.5, "prior_late_payments_count": 0, "discount_offered_pct": 1.5, "days_outstanding_avg_historical": 25, "guarantee_value_kes": null, "economic_sector_growth_rate_pct": 2.5}'

# Clustering
curl -k -X POST https://127.0.0.1/api/v1/models/farmer-segmenter/predictions \
  -H "Content-Type: application/json" \
  -d '{"farm_size_acres": 4.5, "annual_yield_tonnes": 9.8, "income_per_acre_kes": 42000, "years_farming_experience": 6, "market_access_score": 55}'

# Recommender
curl -k -X POST https://127.0.0.1/api/v1/models/food-delivery-recommender/predictions \
  -H "Content-Type: application/json" \
  -d '{"cart": ["F10", "F11"], "top_n": 3}'
```

A successful response is HTTP 200 and includes a `Server: nginx` header (`curl -k -i` will show it). Stop the stack with `docker compose down`.

The API image installs `requirements/base.txt` and `requirements/prod.txt`, pinned by `requirements/constraints.txt` (`scikit-learn==1.9.0`, `imbalanced-learn==0.14.2`, `joblib==1.6.0`) so the saved models load correctly.

### Render

Deploy the same unmodified `api.py` and the same `model/*.joblib` files. Configuration already in the repo:

- [Procfile](Procfile): `web: gunicorn -w 4 -b 0.0.0.0:$PORT api:app`
- [requirements.txt](requirements.txt), plus `requirements/base.txt`, `requirements/prod.txt`, and `requirements/constraints.txt`
- [runtime.txt](runtime.txt) and [.python-version](.python-version): Python 3.12.10. Pin this. Render's default Python may be newer and would fail to load the joblib models.
- Optional [render.yaml](render.yaml) Blueprint with the same build and start commands

Steps to do in the Render dashboard after this branch is on GitHub (nothing is deployed from this repo yet):

1. Push this branch, or merge it into `main` and push `main`.
2. Open [https://dashboard.render.com](https://dashboard.render.com) and sign in, or create an account. The free tier may ask for a $1 card-verification charge.
3. Click **+ New → Web Service** and connect the `BI-course/smm-202604-D7` GitHub repository.
4. Select the branch that contains this work (`main` after the merge, or `feature/170186-deployment` if you deploy the branch directly).
5. Runtime: Python 3. Set **Build Command** to:

   ```text
   pip install -r requirements/base.txt -r requirements/prod.txt -c requirements/constraints.txt
   ```

6. Set **Start Command** to:

   ```text
   gunicorn -w 4 -b 0.0.0.0:$PORT api:app
   ```

7. Set the environment variable `PYTHON_VERSION` to `3.12.10` (or rely on `.python-version`).
8. Choose the Free plan and click **Deploy Web Service**.
9. When the deploy finishes, copy the `https://<service>.onrender.com` URL into [lab_submission_instructions.md](lab_submission_instructions.md). The site root returns 404; send `POST` requests to the four `/api/v1/models/.../predictions` paths, using the sample bodies above. Free services sleep after 15 minutes of inactivity, so the first request afterwards can take 30–60 seconds.

If you apply the Blueprint instead, Render reads `render.yaml` and uses the same commands and Python version.

To confirm the Render start command locally, without Docker:

```shell
source .venv/bin/activate
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5001 api:app
```

Then repeat the `curl` commands above against `http://127.0.0.1:5001` instead of `https://127.0.0.1`.
