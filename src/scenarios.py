import yaml

def load_scenario(path):
    with open(path, "r") as file:
        return yaml.safe_load(file)


def build_prompt(scenario):
    persona = scenario["persona"]
    goal = scenario["goal"]
    preferences = scenario["preferences"]
    rules = scenario["rules"]

    prompt = f"""
You are {persona['name']}, a {persona['age']}-year-old patient.

Goal:
{goal}

Preferences:
- Preferred day: {preferences['preferred_day']}
- Preferred time: {preferences['preferred_time']}

Rules:
"""

    for rule in rules:
        prompt += f"- {rule}\n"

    return prompt