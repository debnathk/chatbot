import streamlit as st
import random
import json
import torch
from model import NeuralNet
from utils import tokenize, stem, bag_of_words

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load intents
with open('tutorial/info.json', 'r') as f:
    intents = json.load(f)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)

# Model evaluation
model.eval()

# Design the chat
bot_name = "Kusal"

def get_bot_response():
    sentence = st.text_input("Type your message here...")

    if st.button('Send'):
        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X)

        output = model(X)
        _, predicted = torch.max(output, dim=1)
        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]

        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent['tag']:
                    st.markdown(f'**{bot_name}:** {random.choice(intent["responses"])}')
        else:
            st.markdown(f'**{bot_name}:** I don\'t understand...')

st.title('KusalBot')
get_bot_response()