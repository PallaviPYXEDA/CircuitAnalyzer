import os
import base64
import requests

import streamlit as st
from openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from pinecone import Pinecone


# keys
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["PINECONE_API_KEY"] = st.secrets["PINECONE_API_KEY"]
os.environ["INDEX_HOST"] = st.secrets["INDEX_HOST"]

# constants
NAMESPACE_KEY = "Arya"
TEXT_MODEL = "text-embedding-ada-002"
QA_MODEL = "gpt-4o-mini"
COMMON_TEMPLATE = """
"Assume you are an expert assisstant in the domain of electronics."
"Use the following pieces of context and the question to provide more information and details about different electronic chip types."
"Please do not use data outside the context to generate any questions."
"If you don not know the context, just say that you don't have enough context."
"don't try to make up an answer."
"\n\n"
{context}
"\n\n"
{question}
"\n"
"Helpful answer:   "
"""


# pinecone setup
pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
index = pc.Index(host=os.environ["INDEX_HOST"])

# create client
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def get_openai_embeddings(text: str) -> list[float]:
    response = client.embeddings.create(input=f"{text}", model=TEXT_MODEL)

    return response.data[0].embedding


# function query similar chunks
def query_response(query_embedding, k = 2, namespace_ = NAMESPACE_KEY):
    query_response = index.query(
        namespace=namespace_,
        vector=query_embedding,
        top_k=k,
        include_values=False,
        include_metadata=True,
    )

    return query_response


def content_extractor(similar_data):
    top_values = similar_data["matches"]
    # get the text out
    text_content = [sub_content["metadata"]["text"] for sub_content in top_values]
    return " ".join(text_content)


def get_model():
    model = ChatOpenAI(model=QA_MODEL, api_key=os.environ["OPENAI_API_KEY"])
    return model


def question_answering(query_question: str, context_text: str,  template: str = COMMON_TEMPLATE):
    prompt = ChatPromptTemplate.from_template(template)
    model = get_model()
    output_parser = StrOutputParser()

    # create the chain
    chain = prompt | model | output_parser

    # get the answer
    answer = chain.invoke({"context": context_text, "question": query_question})

    return answer


def generate_answer(question: str) -> str:
    # get the query embeddings
    quer_embed_data = get_openai_embeddings(question)

    # query the similar chunks
    similar_chunks = query_response(quer_embed_data)

    # extract the similar text data
    similar_content = content_extractor(similar_chunks)

    # get the answer
    answer = question_answering(question, similar_content)

    return answer


def get_similar_context(question: str):
    # get the query embeddings
    quer_embed_data = get_openai_embeddings(question)

    # query the similar chunks
    similar_chunks = query_response(quer_embed_data)

    # extract the similar text data
    similar_content = content_extractor(similar_chunks)

    return similar_content


def streaming_question_answering(query_question: str, context_text: str,  template: str = COMMON_TEMPLATE):
    prompt = ChatPromptTemplate.from_template(template)
    model = get_model()
    output_parser = StrOutputParser()

    # create the chain
    chain = prompt | model | output_parser

    # get the answer
    return chain.stream({"context": context_text, "question": query_question})


# functions related to vision API
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


def call_vision_api(image_path:str):
    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ["OPENAI_API_KEY"]}"
    }

    prompt = "You are an expert assisstant trained to identify different electronic chip types. You are given an image of a chip. First carefully go over the images and classify the image into one out of four categories which are mentioned next. Analog ICs (Op-Amps, Voltage Regulators, ADCs),ASIC and SOC, Digital ICs (Microprocessors, Memory Chips, DSPs) and Mixed-Signal ICs (Modems, Codecs, Mixed-Signal Processors). Please respond with only the classified name. If you can't classify the image into given 4 classes, please say you don't have the context. Use the text on the chip, physical characteristics, and any available labeling to determine the most appropriate category."

    payload = {
    "model": QA_MODEL,
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": prompt
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 300
    }

    # get the response
    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        json_response = response.json()
        chip_type = json_response["choices"][0]["message"]["content"]
        return chip_type
    
    except Exception as error:
        message = "Vision api fails. Error:{}".format(str(error))
        print(message)
        return None
