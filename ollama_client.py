import ollama

#System Prompt
system_prompt = (
    "You are a Python coding assistant. You get an prompt from an user. "
    "Based on this, generate a valid Python code snippet and a short, meaningful title "
    "Respond ONLY in the following format: \n"
    "[Title]: <your title>\n[Python code]:\n<your code>"
    "Do not include explanations or extra test. Only return the title and code."
)

def generate_code(prompt: str) -> str:
    """Send a prompt to the LLM and get the generated code and title."""
    response = ollama.chat(
        model = "codellama",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return response["message"]["content"]

def parse_response(response: str) -> tuple[str, str]:
    """
    Parses the model response to extract the title and Python Code

    Expected Repsonse Format:
    [Title]: Your Title
    [Python Code]:
    <python code here>
    (optional extra explanation)
    """
    lines = response.strip().split('\n')

    title = ""
    code_lines = []
    in_code_block = False

    for line in lines:
        if "[Title]:" in line:
            title = line.replace("[Title]:","").strip()
        elif "[Python code]:" in line:
            in_code_block = True
            continue
        elif in_code_block:
            #If there is any extra explenation stop it
            if line.strip().startswith("This program") or "Explanation" in line:
                break
            code_lines.append(line)
    code = '\n'.join(code_lines)
    if not code_lines:
        for line in lines:
            if line.strip().startswith(("def","import","for","while","print","class","with")):
                code_lines.append(line)
    code = '\n'.join(code_lines).strip()

    if not code:
        code ="# No valid Python code found in the repsonse"
    return title, code