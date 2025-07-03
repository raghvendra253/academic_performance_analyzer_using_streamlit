import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="CPI/SPI Dashboard", layout="wide")
st.title("📊 CPI/SPI Dashboard - IIT Kanpur")

uploaded_file = "Anonymized_CPI_SPI_Data.xlsx"

try:
    # Load file and sheet
    xls = pd.ExcelFile(uploaded_file)
    df = pd.read_excel(xls, sheet_name=0)

    # Clean columns and data
    df.columns = df.columns.str.lower().str.strip()
    df['roll no'] = df['roll no'].astype(str).str.strip()
    df['name'] = df['name'].astype(str).str.strip()
    df['dept'] = df['dept'].astype(str).str.strip()

    # Semesters to plot
    sem_cols = ['sem1', 'sem2', 'sem3', 'sem4']
    semesters = ['Sem 1', 'Sem 2', 'Sem 3', 'Sem 4']

    # Create searchable key: "Name (Roll No)"
    df['search_key'] = df['name'] + " (" + df['roll no'] + ")"

    # --- MAIN STUDENT SELECTION ---
    st.markdown("### 🔍 Search for a Student")
    search_input = st.text_input("Type name or roll no").strip().lower()
    filtered_options = df[df['search_key'].str.lower().str.contains(search_input)]['search_key'].tolist() if search_input else []

    selected_student_str = None
    if filtered_options:
        selected_student_str = st.selectbox("🎯 Select student", filtered_options)
    elif search_input:
        st.warning("No matching names or roll numbers.")

    student = None
    if selected_student_str:
        roll_no = selected_student_str.split("(")[-1].strip(")")
        student = df[df['roll no'] == roll_no].iloc[0]

    # --- COMPARISON STUDENT SELECTION ---
    compare = st.sidebar.checkbox("🔁 Compare with another student")
    compare_student = None

    if compare:
        compare_input = st.sidebar.text_input("🔍 Type name or roll no").strip().lower()
        compare_options = df[df['search_key'].str.lower().str.contains(compare_input)]['search_key'].tolist() if compare_input else []

        selected_compare_str = None
        if compare_options:
            selected_compare_str = st.sidebar.selectbox("🎯 Select second student", compare_options)
        elif compare_input:
            st.sidebar.warning("No matching names or roll numbers.")

        if selected_compare_str:
            compare_roll_no = selected_compare_str.split("(")[-1].strip(")")
            compare_student = df[df['roll no'] == compare_roll_no].iloc[0]

    # --- MAIN DASHBOARD DISPLAY ---
    if student is not None:
        name = student['name']
        branch = student['dept']
        cpi_values = student[sem_cols].values.astype(float)
        final_cpi = student['sem4']

        # Ranks
        df['sem4'] = pd.to_numeric(df['sem4'], errors='coerce')
        df_branch = df[df['dept'] == branch]
        dept_rank = (df_branch['sem4'] > final_cpi).sum() + 1
        inst_rank = (df['sem4'] > final_cpi).sum() + 1

        # Averages and Topper
        branch_avg = df_branch[sem_cols].mean()
        overall_avg = df[sem_cols].mean()
        dept_topper_row = df_branch.loc[df_branch['sem4'].idxmax()]
        dept_topper = dept_topper_row[sem_cols]
        dept_topper_name = dept_topper_row['name']

        # Info Display
        st.subheader(f"👤 {name} ({student['roll no']}) - {branch}")
        st.write(f"**CPI (Sem 4):** {final_cpi}")
        st.write(f"🏅 Department Rank: {dept_rank}")
        st.write(f"🎓 Institute Rank: {inst_rank}")
        st.markdown("### 📚 CPI for Each Semester")
        for i, sem in enumerate(sem_cols):
            st.write(f"- **{sem.capitalize()}**: {cpi_values[i]}")
        # --- CPI Plot ---
        st.markdown("### 📈 CPI Trend (Sem 1 to Sem 4)")
        fig, ax = plt.subplots(figsize=(10, 5))

        # Main student
        ax.plot(semesters, cpi_values, marker='o', label=f"{name}", linewidth=2)

        # Comparison student
        if compare_student is not None:
            compare_cpi = compare_student[sem_cols].values.astype(float)
            compare_name = compare_student['name']
            ax.plot(semesters, compare_cpi, marker='o', linestyle='-', linewidth=2, label=f"{compare_name}")

        # Averages and topper
        ax.plot(semesters, branch_avg.values, marker='o',linestyle='--', label="Branch Avg")
        ax.plot(semesters, overall_avg.values, marker='o',linestyle='--', label="Overall Avg")
        ax.plot(semesters, dept_topper.values,marker='o', linestyle='--', label=f"Dept Topper ({dept_topper_name})")

        ax.set_ylim(0, 10)
        ax.set_ylabel("CPI")
        ax.set_xlabel("Semester")
        ax.set_title("CPI Trend")
        ax.grid(True)
        ax.legend()

        st.pyplot(fig)
    else:
        st.info("Please select a student to view CPI data.")

except Exception as e:
    st.error(f"Error: {e}")
