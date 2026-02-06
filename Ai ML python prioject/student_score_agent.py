import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Dataset
data = {
    "hours_studied": [1, 2, 3, 4, 5, 6, 7, 8],
    "score": [35, 40, 50, 55, 65, 70, 80, 85]
}

df = pd.DataFrame(data)

# 2. Prepare data
X = df[["hours_studied"]]
y = df["score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Train model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Evaluate
r2 = model.score(X_test, y_test)
print(f"📈 Model R² Score: {r2:.2f}")

# 5. Agent function
def predict_score(hours):
    predicted_score = model.predict([[hours]])[0]

    decision = "PASS" if predicted_score >= 60 else "FAIL"

    explanation = (
        "Student studied enough hours"
        if predicted_score >= 60
        else "Student needs more study time"
    )

    return predicted_score, decision, explanation


# 6. User interaction
hours = float(input("Enter hours studied: "))
score, decision, reason = predict_score(hours)

print(f"\n📊 Predicted Score: {score:.2f}")
print(f"🤖 Agent Decision: {decision}")
print(f"🧠 Reason: {reason}")

