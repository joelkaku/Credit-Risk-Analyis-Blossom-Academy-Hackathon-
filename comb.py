import streamlit as st
import hashlib

# Function to hash the password (though not used in this case)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Title for the application
st.title("Welcome to SPJ Savings and Loans")

# Session state to track login
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Check if the user is logged in
if not st.session_state['logged_in']:
    # Login Form
    default_username = "Admin"
    username = st.text_input("Username", value=default_username)

    password = st.text_input("Password", type="password")
    show_password = st.checkbox("Show password")

    if show_password:
        st.text_input("Password", value=password)

    # Login button
    if st.button("LOGIN"):
        # Hash the entered password (optional, since we bypass validation)
        hashed_password = hash_password(password)

        # Bypass password check and log in directly
        st.session_state['logged_in'] = True
        st.success("Login successful! Redirecting to the model page...")
else:
    # If logged in, display the predictive model page
    st.title("SPJ Savings and Loans Default Predictive Model")

    # Instructions
    st.write("Please fill in the details below")

    # Client Information
    st.header("Client Information")

    # Name of Client
    client_name = st.text_input("Name of Client")

    # Create 3 columns for Age, Annual Income, and Home Ownership Status
    col1, col2, col3 = st.columns(3)

    with col1:
        # Age input
        age = st.number_input("Age (18 and above)", min_value=18)

    with col2:
        # Annual income input
        annual_income = st.number_input("Annual Income (Dollars)", min_value=0.0, step=1000.0)

    with col3:
        # Home ownership dropdown
        home_ownership = st.selectbox("Home Ownership Status", ("Own", "Mortgage", "Rent"))

    # Create another row with 3 columns for Employment Duration, Loan Purpose, and Loan Amount
    col4, col5, col6 = st.columns(3)

    with col4:
        # Employment Duration
        employment_duration = st.number_input("Employment Duration (Years)", min_value=0)

    with col5:
        # Purpose of the loan dropdown
        loan_purpose = st.selectbox("Purpose of the Loan", ("Education", "Home Improvement"))

    with col6:
        # Loan applied
        loan_applied = st.number_input("Loan Applied (Dollars)", min_value=0.0, step=500.0)

    # Control Section
    st.header("Control Section")

    # Rate percentage
    rate = st.number_input("Rate (%)", min_value=0.0, step=0.1)

    # Loan approval status dropdown
    loan_approval_status = st.selectbox("LOAN APPROVAL Status", ("Approved", "Not Approved"))

    # Calculate loan amount as a percentage of income
    if annual_income > 0:
        percent_income = (loan_applied / annual_income) * 100
    else:
        percent_income = 0
    st.write(f"Percent Income: {percent_income:.2f}%")

    # Applicant's credit history input
    credit_history = st.text_area("Applicant's Credit HISTORY")

    # Button for prediction
    if st.button("Predict"):
        # Placeholder for prediction logic
        st.success("Prediction completed.")