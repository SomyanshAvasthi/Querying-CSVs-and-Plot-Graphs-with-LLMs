# Somyansh_avasthi
import os
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from dotenv import load_dotenv as ld_dtenv
from langchain_groq import ChatGroq as ChGroq
from pandasai import SmartDataframe as SmrDtFrm

ld_dtenv()


def queries_with_model(dta_frm, qry):
    ld_dtenv()

    groq_api_key = os.environ["GROQ_API_KEY"]

    llm = ChGroq(
        groq_api_key=groq_api_key, model_name="llama3-70b-8192", temperature=0.25
    )
    pandas_ai = SmrDtFrm(dta_frm, config={"llm": llm})
    final_output = pandas_ai.chat(qry)
    return final_output


st.set_page_config(layout="wide")
st.title("Querying CSV Files and Plotting Graphs using LLM :")

user_csvs = st.sidebar.file_uploader(
    "Please upload the .csv file/ files here :-",
    type=["csv"],
    accept_multiple_files=True,
)


if user_csvs:

    user_file = st.selectbox(
        "Kindly select a .csv file. You can toggle the selection menu and choose the desired file :-",
        [file_selected.name for file_selected in user_csvs],
    )
    user_file_indx = [file_selected.name for file_selected in user_csvs].index(
        user_file
    )

    st.info("Your .csv file/ files has been uploaded successfully.")

    st.info("Small sample of the selected file.")
    csv_file_data = pd.read_csv(user_csvs[user_file_indx])
    st.dataframe(csv_file_data.head(5), use_container_width=True)

    st.info("Enter your desired query or prompt below.")
    user_input_prmt = st.text_area("**User query :-**")

    if user_input_prmt:
        if st.button("**RUN THE QUERY**"):
            st.info("Query :- " + user_input_prmt)
            final_output = queries_with_model(csv_file_data, user_input_prmt)
            st.success(final_output)


st.write("## Graphs/ Plots Visualization :")
st.write(
    "For visualization select the type of graph/ plot you want to visualize from the **Left Section** :-"
)

graph_types = st.sidebar.selectbox(
    "**Select the graph/ plot you want to visualize :-**",
    ["BAR CHART", "LINE GRAPH", "SCATTER PLOT", "HISTOGRAM"],
)

if graph_types and "csv_file_data" in locals():
    y_axis_attribute = st.sidebar.text_input("**Enter the X - Axis Attribute :-**")
    x_axis_attribute = st.sidebar.text_input("**Enter the Y - Axis Attribute :-**")

    if x_axis_attribute and y_axis_attribute:
        if (
            x_axis_attribute in csv_file_data.columns
            and y_axis_attribute in csv_file_data.columns
        ):
            if graph_types == "LINE GRAPH":
                st.write("### LINE GRAPH")
                graph_fig, axis_info = plt.subplots()
                axis_info.plot(
                    csv_file_data[x_axis_attribute], csv_file_data[y_axis_attribute]
                )
                axis_info.set_xlabel(x_axis_attribute)
                axis_info.set_ylabel(y_axis_attribute)
                st.pyplot(graph_fig)

            elif graph_types == "SCATTER PLOT":
                st.write("### SCATTER PLOT")
                graph_fig, axis_info = plt.subplots()
                axis_info.scatter(
                    csv_file_data[x_axis_attribute], csv_file_data[y_axis_attribute]
                )
                axis_info.set_xlabel(x_axis_attribute)
                axis_info.set_ylabel(y_axis_attribute)
                st.pyplot(graph_fig)

            elif graph_types == "BAR CHART":
                st.write("### BAR CHART")
                graph_fig, axis_info = plt.subplots()
                axis_info.bar(
                    csv_file_data[x_axis_attribute], csv_file_data[y_axis_attribute]
                )
                axis_info.set_xlabel(x_axis_attribute)
                axis_info.set_ylabel(y_axis_attribute)
                st.pyplot(graph_fig)

            elif graph_types == "HISTOGRAM":
                st.write("### HISTOGRAM")
                graph_fig, axis_info = plt.subplots()
                axis_info.hist(csv_file_data[x_axis_attribute], bins=25, alpha=0.75)
                axis_info.set_xlabel(x_axis_attribute)
                axis_info.set_ylabel("Freq of the Attribute")
                st.pyplot(graph_fig)
        else:
            st.write("Please enter a valid attribute name.")
            st.write(
                "**Please check the spellings of the entered attribute carefully.**"
            )
    else:
        st.write(
            "You have left column/ columns missing. Please enter a valid attribute for the same for visualization purposes."
        )
