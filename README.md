# Introduction

The goal is to write deep learning code from scratch (i.e. no external libraries) for deep learning.

The task is always image classification on MNIST data.

There will be $2 \times N $ cases,
where $N$ is some to-be-determined number of programming languages
and $2$ endoces the number of paradigms (object-oriented and functional).

ChatGPT will be used to generate the code.
To estimate the time, the author will tag git commits with "start" and "end" tags
every time the author starts and ends working on the code.

There may also be an attempt to compare the "readability" of the different cases.

The cases will be written in the following languages:
- Python
- Mojo
- C++
- Haskell
- Julia
- ... (hence the $N$)

The object-oriented approach will always target the following classes:
- `Dataset`: for data downloading, creation, and loading
- `Model`: for mathematically defining the neural network model
- `Trainer`: for training the model
- `Evaluator`: for evaluating the model

The functional approach will always target the following functions:
- `create_dataset`: for creating the dataset
- `define_model`: for mathematically defining the neural network model
- `train_model`: for training the model
  - `forward_pass`: for the forward pass
  - `backward_pass`: for the backward pass
- `evaluate_model`: for evaluating the model

# Learning goals

- Implement back propagation code from scratch - that is: no using external backpropagation libraries like TensorFlow or PyTorch for now.
- Understand the implementation differences between object-oriented and functional programming paradigms.
- Understand how well chatbot LLMs can work as "junior coding partners" for someone with a good understanding of the underlying deep learning principles and deep familiary with at least one langugage (i.e. python).
- Tightly integrate an LLM into the code development and integration pipeline.

# Scorecard

| language | accuracy | runtime  | dev time | readability |
|----------|----------|----------|----------|-------------|
| python   | ?        | ?        | ?        | ?           |
| mojo     | ?        | ?        | ?        | ?           |
| c++      | ?        | ?        | ?        | ?           |
| haskell  | ?        | ?        | ?        | ?           |
| julia    | ?        | ?        | ?        | ?           |
| ...      | ...      | ?        | ?        | ?           |