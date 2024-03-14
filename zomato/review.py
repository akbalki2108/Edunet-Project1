import openai
import pandas as pd


def generate_summary_with_index(index):
    openai.api_key = 'OpenAI_API_Key'

    # Step 3: Preprocess your text data
    def split_text(text):
        max_chunk_size = 1500
        chunks = []
        current_chunk = ""
        for sentence in text.split("."):
            if len(current_chunk) + len(sentence) < max_chunk_size:
                current_chunk += sentence + "."
            else:
                chunks.append(current_chunk.strip())
                current_chunk = sentence + "."
        if current_chunk:
            chunks.append(current_chunk.strip())
        return chunks

    # Step 4: Generate summaries using OpenAI’s GPT-3 API
    def generate_summary(name, text):
        input_chunks = split_text(text)
        print(len(input_chunks))
        output_chunks = []
        for chunk in input_chunks:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Please summarize the following text in 50 words & as it is a restaurant review make it look like a review of {name}:\n{chunk}\n\nSummary:"}
                ]
            )
            summary = response['choices'][0]['message']['content'].strip()
            output_chunks.append(summary)

        return " ".join(output_chunks)

    # Process only the desired row and save the result to a new CSV file
    row = df.iloc[index]
    try:
        result = generate_summary(row['name'], row['summaries'])
        result_df = pd.DataFrame({'name': [row['name']], 'summary': [result]})
        ans = result_df['summary'].tolist()[0]
        return ans
    except Exception as e:
        return "REVIEWS ARE NOT AVAILABLE"

global df
input_csv_path = "zomato_cleaned.csv"
df = pd.read_csv(input_csv_path)