from ollama_client import generate_code, parse_response


prompt = "Write a python program that reads all lines from a file and prints them to the screen."
raw_response = generate_code(prompt)
title, code = parse_response(raw_response)

print("\n*** Title ***\n")
print(title)
print("\n*** Code ***\n")
print(code)