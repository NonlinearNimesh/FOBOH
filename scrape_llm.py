import csv
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from huggingface_hub import login

api_token = "XXXXXXXXXXXXXXXXXXXXX"
login(api_token)

model_name = "meta-llama/Meta-Llama-3-8B"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=True)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

device = "cuda" if torch.cuda.is_available() else "cpu"
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, use_auth_token=True).to(device)
model.eval()

def query_llama(prompt, model, tokenizer, max_tokens=500):
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    output = model.generate(**inputs, max_new_tokens=max_tokens)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

def parse_llama_output(output_text):
    rows = []
    lines = output_text.split("\n")
    for line in lines:
        if line.strip():
            row = line.split("\t")
            if len(row) == 3:
                rows.append(row)
    return rows

def get_restaurant_data(num_iterations=13, output_csv="restaurant_data.csv"):
    all_rows = []
    prompt_template = """
    Give me the name of 50 restaurants that are in Sydney CBD 2000 area, including their menu and ingredients used to make the dishes, in a tabular format with columns: Restaurant, Menu, Ingredients.
    """
    for iteration in range(num_iterations):
        if iteration == 0:
            prompt = prompt_template
        else:
            prompt = "Give me 50 more restaurants from Sydney CBD 2000 with their menu and ingredients in a tabular format."
        result = query_llama(prompt, model, tokenizer)
        rows = parse_llama_output(result)
        all_rows.extend(rows)
    if all_rows:
        with open(output_csv, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Restaurant", "Menu", "Ingredients"])
            writer.writerows(all_rows)

get_restaurant_data()
