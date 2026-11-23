"""
api.py

A RESTish API, built with Flask, that serves FOUR machine learning artifacts
produced in earlier labs:

    1. Regression       -- SME monthly revenue prediction
    2. Classification   -- SME credit risk category
    3. Clustering       -- Mall customer segment assignment
    4. Association Rule -- Product recommendation from a cart
       Mining (ARM)

The point of this file is to show you that a fitted scikit-learn /
imbalanced-learn Pipeline is a SINGLE object that already knows how to impute
missing values, encode categorical columns, scale numeric columns, and (for
the classifier) apply SMOTE only during training -- never during inference.
Because all of that preprocessing lives inside the Pipeline itself, this file
never manually label-encodes anything, never manually engineers date features,
and never manually reorders columns before calling .predict(). It builds a
DataFrame straight from the incoming JSON and hands it to the pipeline as-is.
This is the main lesson of the lab: "the pipeline IS the deployment artifact."

Run this file directly to start a local development server:

    python api.py
"""

import os

import joblib
import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# -----------------------------------------------------------------------
# CORS (Cross-Origin Resource Sharing)
# -----------------------------------------------------------------------
# By default, a browser blocks JavaScript on one origin (e.g., a page served
# from http://127.0.0.1:5500) from calling an API on a different origin
# (e.g., http://127.0.0.1:5000). `flask_cors` relaxes that restriction for the
# specific origins we trust during local development.
#
# A few alternative configurations are shown below (commented out) so you can
# see how the restriction can be loosened or tightened depending on your
# deployment target. Only ONE of these should be active at a time.

# Option A (the most permissive. This is fine for a quick classroom demo or
# local development, *NEVER* for production):
# CORS(app)

# Option B (allow only a specific frontend origin):
# CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5500"}})

# Option C (the one actually in use here -- allow localhost/127.0.0.1 on the
# ports our lab's frontend files are typically served from):
CORS(app, resources={r"/api/*": {"origins": [
    "http://localhost:5000", "http://127.0.0.1:5000",
    "http://localhost:5500", "http://127.0.0.1:5500",
    "https://localhost:443", "https://127.0.0.1:443",
    "http://localhost:63342",  # VS Code Live Server extension
    "null",  # allows opening a frontend .html file directly (file://) with no web server
]}})

# -----------------------------------------------------------------------
# The best practice is to load the four persisted artifacts ONCE, at startup,
# not per-request.
# Loading inside a route function would re-read the file from disk on every
# single API call, which is slow and pointless -- the fitted model never
# changes while the server is running.
# -----------------------------------------------------------------------
MODEL_DIR = "./model"

regression_pipeline = joblib.load(
    os.path.join(MODEL_DIR, "farm_income_model.joblib")
)

classification_pipeline = joblib.load(
    os.path.join(MODEL_DIR, "invoice_payment_risk_classifier.joblib")
)

clustering_artifact = joblib.load(
    os.path.join(MODEL_DIR, "farmer_clustering_pipeline.joblib")
)
clustering_imputer = clustering_artifact["imputer"]
clustering_scaler = clustering_artifact["scaler"]
clustering_kmeans = clustering_artifact["kmeans"]
clustering_features = clustering_artifact["numeric_features"]

arm_artifact = joblib.load(
    os.path.join(MODEL_DIR, "apriori_recommendation_rules.joblib")
)
recommendation_lookup = arm_artifact["recommendation_lookup"]
sku_lookup = arm_artifact["sku_lookup"]

print("All the four artifacts have been loaded. The API is ready.")


# 1. REGRESSION -- predict annual farm income (KES)
@app.route("/api/v1/models/farm-income-regressor/predictions", methods=["POST"])
def predict_farm_income():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify(error="Expected a JSON object."), 400

    fields = list(regression_pipeline.feature_names_in_)
    missing_fields = [field for field in fields if field not in payload]
    if missing_fields:
        return jsonify(error="Missing required fields.", missing_fields=missing_fields), 400

    import numpy as np

    # Convert explicit JSON nulls to NaN for the fitted preprocessing pipeline.
    input_row = pd.DataFrame(
        [[np.nan if payload[field] is None else payload[field] for field in fields]],
        columns=fields,
    )
    try:
        predicted_log_income = regression_pipeline.predict(input_row)[0]
    except (TypeError, ValueError):
        return jsonify(error="Invalid values for the farm income model."), 400

    return jsonify(
        predicted_annual_farm_income_kes=round(float(np.expm1(predicted_log_income)), 2),
        model="Ridge Regressor",
    )


# 2. CLASSIFICATION -- predict B2B invoice payment risk (On-Time / Late / Severely Late)

# Sample request (cURL):
#   curl -X POST http://127.0.0.1:5000/api/v1/models/invoice-payment-risk-classifier/predictions \
#        -H "Content-Type: application/json" \
#        -d '{"client_industry": "Technology", "client_credit_rating": "Good",
#             "client_company_size": "Medium", "payment_method": "Bank Transfer",
#             "has_dispute_history": "No", "collateral_or_guarantee": "No",
#             "payment_terms_days": 30, "invoice_amount_kes": 350000,
#             "client_relationship_years": 4.5, "prior_late_payments_count": 0,
#             "discount_offered_pct": 1.5, "days_outstanding_avg_historical": 25,
#             "guarantee_value_kes": null, "economic_sector_growth_rate_pct": 2.5}'
#
# Note: guarantee_value_kes is optional. It is structurally missing when the
# invoice has no collateral/guarantee, and the pipeline's imputer + missingness
# indicator handles that. Every other field is required.
INVOICE_REQUIRED_FIELDS = [
    "client_industry", "client_credit_rating", "client_company_size",
    "payment_method", "has_dispute_history", "collateral_or_guarantee",
    "payment_terms_days", "invoice_amount_kes", "client_relationship_years",
    "prior_late_payments_count", "discount_offered_pct",
    "days_outstanding_avg_historical", "economic_sector_growth_rate_pct",
]


@app.route("/api/v1/models/invoice-payment-risk-classifier/predictions", methods=["POST"])
def predict_invoice_payment_risk():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"error": "Request body must be a JSON object."}), 400

    missing = [f for f in INVOICE_REQUIRED_FIELDS if payload.get(f) is None]
    if missing:
        return jsonify({
            "error": "Missing required field(s).",
            "missing_fields": missing,
        }), 400

    # guarantee_value_kes is optional; default to None (the pipeline imputes it).
    payload.setdefault("guarantee_value_kes", None)

    try:
        input_row = pd.DataFrame([payload])
        predicted_class = classification_pipeline.predict(input_row)[0]
        predicted_probabilities = classification_pipeline.predict_proba(input_row)[0]
        class_labels = classification_pipeline.named_steps["model"].classes_
    except Exception as error:
        return jsonify({
            "error": "Could not make a prediction. Check the field values and types.",
            "details": str(error),
        }), 400

    return jsonify({
        "predicted_payment_risk_category": str(predicted_class),
        "class_probabilities": {
            str(label): round(float(prob), 4)
            for label, prob in zip(class_labels, predicted_probabilities)
        },
        "model": "Logistic Regression (tuned, ADASYN-resampled at training only)",
    })


# 3. CLUSTERING -- assign a farmer to an existing segment

# Sample request (cURL):
#   curl -X POST http://127.0.0.1:5000/api/v1/models/farmer-segmenter/predictions \
#        -H "Content-Type: application/json" \
#        -d '{"farm_size_acres": 4.5, "annual_yield_tonnes": 9.8,
#             "income_per_acre_kes": 42000, "years_farming_experience": 6,
#             "market_access_score": 55}'
#
# Note: the saved artifact holds three fitted objects -- the imputer, the scaler
# and the K-Means model. A new farmer must go through the imputer and the scaler
# (fitted on the training data) before K-Means can assign a cluster.
# market_access_score is optional: it had missing values in the training data,
# so the fitted imputer fills it with the training median when it is absent.
FARMER_REQUIRED_FIELDS = [
    "farm_size_acres",
    "annual_yield_tonnes",
    "income_per_acre_kes",
    "years_farming_experience",
]
FARMER_CLUSTER_NAMES = {0: "Smallholder Farmers", 1: "Established Commercial Farmers"}


@app.route("/api/v1/models/farmer-segmenter/predictions", methods=["POST"])
def predict_farmer_segment():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"error": "Request body must be a JSON object."}), 400

    missing = [f for f in FARMER_REQUIRED_FIELDS if payload.get(f) is None]
    if missing:
        return jsonify({
            "error": "Missing required field(s).",
            "missing_fields": missing,
        }), 400

    # market_access_score is optional; default to None (the imputer fills it).
    payload.setdefault("market_access_score", None)

    try:
        input_row = pd.DataFrame([payload])[clustering_features].astype(float)
        imputed_input = clustering_imputer.transform(input_row)
        scaled_input = clustering_scaler.transform(imputed_input)
        assigned_cluster = int(clustering_kmeans.predict(scaled_input)[0])
    except Exception as error:
        return jsonify({
            "error": "Could not assign a cluster. Check the field values and types.",
            "details": str(error),
        }), 400

    return jsonify({
        "assigned_cluster": assigned_cluster,
        "segment": FARMER_CLUSTER_NAMES.get(assigned_cluster, "Unknown"),
        "model": "K-Means (k=2, median-imputed, standardized features)",
    })


# 4. ASSOCIATION RULE MINING -- recommend products for a shopping cart

# Sample request (cURL):
#   curl -X POST http://127.0.0.1:5000/api/v1/models/ecommerce-recommender/predictions \
#        -H "Content-Type: application/json" \
#        -d '{"cart": ["H06", "H07"]}'
#
#   curl -X POST http://127.0.0.1:5000/api/v1/models/ecommerce-recommender/predictions \
#        -H "Content-Type: application/json" \
#        -d '{"cart": ["P04", "P01"]}'
#
# Note: there is no scikit-learn ".predict()" here -- the mined association
# rules were precomputed into a lookup dictionary
# (antecedent SKU-set -> ranked candidate consequents)
# during the notebook's persistence stage. This
# endpoint performs the exact same lookup+rank step a production recommender
# microservice would perform on every incoming request; it does not mine
# for the rules again.
@app.route("/api/v1/models/ecommerce-recommender/predictions", methods=["POST"])
def recommend_products():
    payload = request.get_json()
    cart = set(payload.get("cart", []))
    top_n = int(payload.get("top_n", 3))

    candidates = {}
    for antecedent, consequent_list in recommendation_lookup.items():
        if antecedent.issubset(cart):
            for sku, confidence, lift in consequent_list:
                if sku not in cart:
                    if sku not in candidates or confidence > candidates[sku][0]:
                        candidates[sku] = (confidence, lift)

    ranked = sorted(candidates.items(), key=lambda item: item[1][0], reverse=True)[:top_n]
    recommendations = [
        {
            "sku": str(sku),
            "product_name": sku_lookup.loc[sku, "product_name"],
            "confidence": round(float(confidence), 3),
            "lift": round(float(lift), 2),
        }
        for sku, (confidence, lift) in ranked
    ]

    return jsonify({
        "cart": sorted(cart),
        "recommendations": recommendations,
        "model": "Apriori association rules, cleaned + precomputed lookup",
    })


# -----------------------------------------------------------------------
# Entry point
# -----------------------------------------------------------------------
if __name__ == "__main__":
    # Development server. debug=True gives auto-reload and an interactive
    # debugger on errors -- convenient in class, but NEVER use debug=True in
    # a deployed/public environment (it can expose a remote code execution
    # console to anyone who can reach the server).
    app.run(debug=True)

    # Production-style alternative (no debugger, no auto-reload):
    # app.run(debug=False, host="0.0.0.0", port=5000)

    # HTTPS/TLS alternative for local development (requires a self-signed
    # certificate; see app_server_reverse_proxy_server_setup.md):
    # app.run(debug=False, ssl_context=("cert.pem", "key.pem"))
