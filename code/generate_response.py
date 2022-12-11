import cohere
co = cohere.Client('MZEXVdqnzLxLGnxmzNjCLS129C4aF6iEEFejYCGy')

# prompt = "Explain me in a paragraph the concept of: computer algorithm"

def generate_responses(topic):

    area = "reinforcement learning"
    prompt = f"explain to me the concept of {topic} in the context of {area}"
    
    response = co.generate(
    model='command-xlarge-20221108',
    prompt=prompt,
    max_tokens=512,
    temperature=0.7,
    k=0,
    p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop_sequences=[],
    return_likelihoods='NONE')

    ans = response.generations[0].text
    return ans


