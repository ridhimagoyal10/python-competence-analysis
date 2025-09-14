# python-competence-analysis
A project for Python Screening Task 3 : Evaluating Open Source Models for Student Competence Analysis.
# Python Competence Analysis: Open Source Model Evaluation

## Task Submission for FOSSEE Python Screening Task 3

This repository contains my submission for the Python Competence Analysis task, which involves evaluating an open-source AI model for assessing student understanding of Python programming.

***

## Research Plan

My approach is to evaluate open-source large language models (LLMs) that are specifically trained on code. I will use the *CodeLlama 7B Instruct-GGUF* model by META for my evaluation, chosen for its strong performance in code-related tasks and its ability to run on local machines without expensive hardware. My goal is to determine if this model can effectively analyze student-written Python code and generate prompts that assess a student's conceptual understanding rather than just identifying syntax errors.

To test the model's suitability, I will create a structured test case. I will provide the model with a Python code snippet that contains a subtle logical error, typical of a student's misconception. The model will then be prompted to generate a conceptual question about the code. I will manually evaluate the generated question to see if it encourages deeper thinking and helps the student identify their own mistake without giving away the solution. This process will validate the model's ability to act as a helpful and insightful educational assistant.

***

## Reasoning

### What makes a model suitable for high-level competence analysis?

A model is suitable for high-level competence analysis if it can go beyond surface-level syntax checks and understand the underlying logic and reasoning behind the code. It should be able to identify gaps in a student's conceptual understanding and generate context-specific, insightful prompts. A good model for this task avoids providing direct solutions and instead guides the student toward a deeper understanding, acting as a true learning facilitator.For example, if a student has used a complex if-else if-else chain, a good model can identify that a dictionary or polymorphism would have been more efficient. This allows the model to analyze the student's problem-solving mindset.

### How would you test whether a model generates meaningful prompts?

I would test a model's prompt generation by providing it with several code snippets, each containing a different type of error (e.g., a logical error, a misconception about a data structure, or an inefficient algorithm). I would then manually review the questions the model generates. A prompt is considered meaningful if it is open-ended, directly addresses the specific error or misconception in the code, and encourages the student to reflect on the core programming concept they are struggling with. I would specifically look for questions that use "why" or "how" to prompt critical thinking.
 I would test this in the following way:

Test Case 1: Code with a common misconception. I would write code with a common mistake (like the incorrect use of is vs. ==). I would then ask the model to analyze the code and generate a question. A good model wouldn't just suggest a bug fix; it would ask a question like, "What is the difference between the is and == operators, and what could be their impact in this code?"

Test Case 2: Code with multiple valid solutions. I would provide a problem whose code can be written in multiple ways. I would then ask the model to provide prompts for refactoring the code. For instance, "How can you make this code more concise using a list comprehension?" or "How can you improve the performance of this code?"

### What trade-offs might exist between accuracy, interpretability, and cost?

Significant trade-offs exist between these three factors. *Accuracy* often comes at a high *cost; larger, more accurate models require significant computational resources for training and inference. This makes them expensive to use, especially in a free educational context ,(like GPT-4) are often not open-source and cost money to use. Conversely, smaller models are less costly but may be less accurate and prone to "hallucinations" (generating plausible but incorrect information).Open-source models (like Code Llama 7B) are free, but their accuracy might be lower than the larger, proprietary models. In terms of **interpretability*, complex, highly accurate models can be difficult to understand (like deep neural networks, they are "black boxes"), making it hard to see why they generated a specific response. 
Smaller open-source models like CodeLlama, however, are more transparent and can be fine-tuned, balancing cost, accuracy, and providing a clearer path to understanding how they work.

### Why did you choose the model you evaluated, and what are its strengths or limitations?

I chose *CodeLlama 7B Instruct-GGUF* because it is a powerful, open-source, and instruction-tuned model designed specifically for code.It's a state-of-the-art open-source LLM specifically trained for code-related tasks. Its open-source nature makes it accessible and a perfect match for the task requirements. It's GGUF format allows it to run efficiently on a standard computer, which makes it an excellent, cost-free option for educational use. Its key *strength* is its proficiency in understanding and generating code-related text, which is perfect for this task. 
However, its main *limitations* include its smaller size compared to commercial models, which might lead to less accurate or nuanced analysis for complex programming concepts. The model might be better at "correcting" code than at generating questions about conceptual understanding. This would likely require further fine-tuning.It may also occasionally generate responses that are not perfectly aligned with the instructional goal.

***

## Setup Instructions

This project uses the CodeLlama 7B Instruct-GGUF model. To run the evaluation script, you will need to:

1.  *Install the necessary library:*
    bash
    pip install ctransformers
2.   *Download the model file:*
    Download the model file (https://huggingface.co/TheBloke/CodeLlama-7B-Instruct-GGUF) from a trusted source (https://huggingface.co/-TheBloke's Hugging Face repository).
3.  *Place the model file:*
    Create a new folder named models inside this project's directory and place the downloaded [Codellama-7B Instruct GGUF](c:/Users/hp/Downloads/codellama-7b-instruct.Q4_K_M.gguf) file inside it.
4.  *Run the script:*
    Execute the evaluation.py script to see the model's output.

    
