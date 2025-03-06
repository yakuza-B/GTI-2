import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# --- TITLE ---
st.title("Terrorism Index Prediction App")

# --- FILE UPLOAD ---
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    # Read the uploaded file
    data = pd.read_csv(uploaded_file)

    # Show dataset preview
    st.write("### Dataset Preview")
    st.write(data.head())

    # --- VISUALIZATION ---
    st.write("### Data Distribution")
    numeric_columns = data.select_dtypes(['float64', 'int64']).columns

    if len(numeric_columns) > 0:
        selected_col = st.selectbox("Choose a numeric column", numeric_columns)
        fig, ax = plt.subplots()
        sns.histplot(data[selected_col], bins=20, kde=True, ax=ax)
        st.pyplot(fig)
    else:
        st.write("No numeric columns available for visualization.")

    # --- FEATURE SELECTION & TRAINING ---
    st.write("### Model Training")
    target_col = st.selectbox("Select the target column", numeric_columns)

    if target_col:
        X = data.drop(columns=[target_col]).select_dtypes(['float64', 'int64'])
        y = data[target_col]

        if not X.empty:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            model = LinearRegression()
            model.fit(X_train, y_train)

            st.write(f"Model Trained! R² Score: {model.score(X_test, y_test):.2f}")

            # --- PREDICTION ---
            st.write("### Make a Prediction")
            user_input = {col: st.number_input(f"Enter {col}") for col in X.columns}
            user_df = pd.DataFrame([user_input])

            if st.button("Predict"):
                prediction = model.predict(user_df)
                st.write(f"### Predicted {target_col}: {prediction[0]:.2f}")
