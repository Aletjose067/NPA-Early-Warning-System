from flask import Flask, render_template, request
import joblib
import pandas as pd

from email_alert import send_email

app = Flask(__name__)

# Load trained model
model = joblib.load("models/npa_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Customer Details
    customer_name = request.form["customer_name"]
    customer_id = request.form["customer_id"]
    email = request.form["email"]
    mobile = request.form["mobile"]

    # Loan Details
    age = float(request.form["age"])
    sanct_lim = float(request.form["sanct_lim"])
    overdue_amt = float(request.form["overdue_amt"])
    balance_os = float(request.form["balance_os"])
    total_transactions = int(request.form["total_transactions"])
    total_transaction_amount = float(
        request.form["total_transaction_amount"]
    )
    avg_transaction_amount = float(
        request.form["avg_transaction_amount"]
    )

    # Create DataFrame for Prediction
    data = pd.DataFrame(
        [[
            age,
            sanct_lim,
            overdue_amt,
            balance_os,
            total_transactions,
            total_transaction_amount,
            avg_transaction_amount
        ]],
        columns=[
            "AGE",
            "SANCT_LIM",
            "OVERDUE_AMT",
            "BALANCE_OS",
            "TOTAL_TRANSACTIONS",
            "TOTAL_TRANSACTION_AMOUNT",
            "AVG_TRANSACTION_AMOUNT"
        ]
    )

    # Predict Probability
    probability = model.predict_proba(data)[0][1]

    email_status = "No Email Sent"

    # Risk Classification
    if probability >= 0.70:

        risk_level = "HIGH RISK"
        animation_class = "high-risk"

        email_sent = send_email(
            email,
            customer_name,
            probability * 100
        )

        if email_sent:
            email_status = "Email Alert Sent Successfully"
        else:
            email_status = "Email Sending Failed"

    elif probability >= 0.40:

        risk_level = "MEDIUM RISK"
        animation_class = "medium-risk"

    else:

        risk_level = "LOW RISK"
        animation_class = "low-risk"

    return render_template(
        "result.html",
        customer_name=customer_name,
        customer_id=customer_id,
        email=email,
        mobile=mobile,
        age=age,
        sanct_lim=sanct_lim,
        overdue_amt=overdue_amt,
        balance_os=balance_os,
        total_transactions=total_transactions,
        total_transaction_amount=total_transaction_amount,
        avg_transaction_amount=avg_transaction_amount,
        probability=round(probability * 100, 2),
        risk_level=risk_level,
        animation_class=animation_class,
        email_status=email_status
    )


if __name__ == "__main__":
    app.run(debug=True)