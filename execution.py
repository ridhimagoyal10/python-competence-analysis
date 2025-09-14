import os
from ctransformers import AutoModelForCausalLM

# Define model path and file
model_path = os.path.join(os.getcwd(), 'models')
model_file = 'codellama-7b-instruct.Q4_K_M.gguf'

# Configuration as a dictionary
model_config = {
    'max_new_tokens': 256,
    'temperature': 0.1,
    'context_length': 2048  # Add context length if needed
}

try:
    # Load the model with proper configuration
    model = AutoModelForCausalLM.from_pretrained(
        model_path_or_repo_id=model_path,
        model_file=model_file,
        model_type="llama",
        **model_config  # Unpack config as keyword arguments
    )
except ValueError as e:
    print(f"Error: Model file '{model_file}' not found in the 'models' folder. Details: {e}")
    exit()
except AttributeError as e:
    print(f"AttributeError: {e}")
    print("Trying alternative configuration method...")
    try:
        # Alternative method: Load model without config first
        model = AutoModelForCausalLM.from_pretrained(
            model_path_or_repo_id=model_path,
            model_file=model_file,
            model_type="llama"
        )
        # Set configuration after loading
        model.config = model_config
    except Exception as e2:
        print(f"Alternative method also failed: {e2}")
        exit()

# Student code with logical error
student_code_snippet = """
def find_largest_number(numbers):
    largest = 0
    for number in numbers:
        if number > largest:
            largest = number
    return largest
"""

# Create the prompt
prompt = f"""
### Instruction:
You are a Python programming tutor. Your goal is to help a student understand their code by asking a thoughtful, conceptual question. Do not give away the solution.
Here is the student's code:
{student_code_snippet}
### Question:
Based on this code, what single, conceptual question would you ask the student to help them discover why their function might not work correctly if the list of numbers contains only negative values (e.g., [-1, -5, -3])?
"""

# Generate the question
try:
    # Use the model to generate a response
    generated_question = model(prompt)
    print("Generated Question:")
    print(generated_question)
    
    # Test the corrected function
    def find_largest_number_corrected(numbers):
        if not numbers:
            return None
        largest = numbers[0]  # Initialize with first element
        for number in numbers:
            if number > largest:
                largest = number
        return largest

    # Test cases
    test_cases = [
        [1, 5, 3, 9, 2],      # Normal case
        [-1, -5, -3, -7],     # All negative numbers
        [],                   # Empty list
        [0, -1, 2],           # Mixed positive/negative
        [5]                   # Single element
    ]
    
    print("\nTesting Corrected Function:")
    for test in test_cases:
        result = find_largest_number_corrected(test)
        print(f"Input: {test} => Largest: {result}")
        
except Exception as e:
    print(f"An unexpected error occurred during model generation: {e}")
