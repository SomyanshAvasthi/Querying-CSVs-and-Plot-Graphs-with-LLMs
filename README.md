## Querying CSVs and Plot Graphs with LLM
This project leverages the power of Large Language Models (LLMs) to streamline the process of querying CSV files and generating graphical visualizations of data. At its core, the project utilizes LLMs to interpret natural language queries, making data manipulation and analysis more intuitive for users. The technical foundation of this project includes several key components that enhance its functionality and user experience.

LLMs are integral to the project, utilizing tokens as the basic units of text. These tokens are converted into embeddings, which are numerical representations capturing the semantic meaning of words and phrases. The embeddings allow the model to understand and generate contextually relevant responses. Model learning, the training process for LLMs, involves extensive exposure to large datasets to recognize patterns and language structures. Additionally, the temperature parameter is crucial for controlling the randomness of the model’s responses; a lower temperature results in more deterministic outputs, while a higher temperature yields more varied responses.

For data manipulation, the project employs the pandas library, renowned for its robust data handling capabilities, particularly with CSV files. This library enables efficient data cleaning, transformation, and analysis. For visualization, the matplotlib library is used to generate static, animated, and interactive plots, providing users with clear and insightful graphical representations of their data.

The project also integrates Streamlit, a tool that facilitates the creation of interactive web applications. Streamlit serves as the user interface, allowing users to upload CSV files, input natural language queries, and instantly view the resulting visualizations. This real-time interaction is key to enhancing the user experience, making data analysis accessible and efficient.

Environment configuration is managed using python-dotenv, a library that securely handles environment variables, ensuring that API keys and other sensitive information are managed appropriately. This setup not only secures the application but also simplifies the configuration process for users.

In summary, this project utilizes advanced technical components such as LLMs, pandas, matplotlib, Streamlit, and python-dotenv to create a powerful tool for querying CSV files and visualizing data. The integration of these technologies allows users to interact with complex datasets using natural language, making data analysis more accessible, intuitive, and efficient.

![image](https://github.com/user-attachments/assets/ae50150a-ec64-44f7-ac67-6d6185ca8432)

Incorporating the power of natural language and advanced data tools, this project redefines how we interact with and derive insights from CSV data. By bridging the gap between complex data analysis and intuitive user experience, it empowers users to unlock meaningful insights effortlessly. This innovation marks a significant step towards democratizing data-driven decision-making and fostering a more accessible approach to analytics.
