---
# **Overview of Language Model Methodologies**

This document provides an overview of various language model methodologies, highlighting their reasoning steps, tool use, and real-world applicability. The methodologies covered include ReAct, Language Agent Tree Search (LATS), REST Meets ReAct (ReST), Automatic Tool Chain (ATC), and Toolformer.

## **Table of Contents**

- [**ReAct (Reasoning and Acting)**](#react-reasoning-and-acting)
  - [**Reasoning Steps**](#reasoning-steps)
  - [**Tool Use**](#tool-use)
  - [**Real-World Applicability**](#real-world-applicability)
- [**Language Agent Tree Search (LATS)**](#language-agent-tree-search-lats)
  - [**Reasoning Steps**](#reasoning-steps-1)
  - [**Tool Use**](#tool-use-1)
  - [**Real-World Applicability**](#real-world-applicability-1)
- [**REST Meets ReAct (ReST)**](#rest-meets-react-rest)
  - [**Reasoning Steps**](#reasoning-steps-2)
  - [**Tool Use**](#tool-use-2)
  - [**Real-World Applicability**](#real-world-applicability-2)
- [**Automatic Tool Chain (ATC)**](#automatic-tool-chain-atc)
  - [**Tool Use**](#tool-use-3)
  - [**Real-World Applicability**](#real-world-applicability-3)
- [**Toolformer**](#toolformer)
  - [**Reasoning Steps**](#reasoning-steps-3)
  - [**Tool Use**](#tool-use-4)
  - [**Real-World Applicability**](#real-world-applicability-4)
- [**Contrasting Methodologies**](#contrasting-methodologies)
- [**Real-World Applicability Assessment**](#real-world-applicability-assessment)
- [**Citations**](#citations)

---

## **ReAct (Reasoning and Acting)**

ReAct agents interleave reasoning and action steps, initially reasoning about the task before executing a function. This approach uses a "Few Shot" prompt technique, where human annotators provide examples of their thoughts and actions in language.

### **Reasoning Steps**  
ReAct employs free-form reasoning steps interspersed with actions [1]. These steps include:  
- Decomposing a question  
- Extracting information  
- Commonsense reasoning  
- Guiding search  
- Synthesizing a final answer  

The reasoning process is dynamic, allowing for the creation and adjustment of action plans.

### **Tool Use**  
ReAct leverages external tools, such as the Wikipedia API, to gather information [1], updating its knowledge and informing its reasoning.

### **Real-World Applicability**  
ReAct is useful when direct action is not possible and reasoning is required first. For example, a complex query like:  
`Find a floral skirt under $40 in size S. Is it in stock, and can I apply a discount code ‘SAVE10’?`  
This query needs to be broken down and reasoned before employing any function.

---

## **Language Agent Tree Search (LATS)**

LATS uses a tree-based search algorithm with a language model as an agent. It expands on ReAct by exploring a combinatorial space of reasoning and acting steps and uses Monte Carlo Tree Search (MCTS) for exploration and decision-making [2].

### **Reasoning Steps**  
LATS integrates language model reasoning, acting, and planning. It uses a value function and self-reflections to guide the search for the most promising trajectory, which can involve organizing information, planning future actions, or injecting internal knowledge.

### **Tool Use**  
LATS uses external tools and APIs to interact with the environment, incorporating observations from tool use and self-generated reflections.

### **Real-World Applicability**  
LATS shows strong results in programming, question answering, web navigation, and math. It offers more deliberate decision-making compared to the reflexive approach in ReAct and is adaptable to different scenarios by modifying state design and tree dimensions.

---

## **REST Meets ReAct (ReST)**

ReST builds on the ReAct framework by incorporating self-critique. It features a multi-step design that includes decision-making, tool use, summarization, and answer generation [3].

### **Reasoning Steps**  
ReST reasons through multiple steps and employs self-critique to improve performance. It performs relevance and grounding self-checks.

### **Tool Use**  
ReST uses web search to generate long-form, attributable answers.

### **Real-World Applicability**  
ReST's self-improvement and self-distillation refine the agent over multiple iterations. It does not require human-labeled data, making it suitable for complex question answering.

---

## **Automatic Tool Chain (ATC)**

ATC enables LLMs to use a chain of tools through programming. It learns input-output schema and data flow dependency from tool protocols and generates an executable program that sequentially calls tools, parses responses, and derives a final answer [4].

### **Tool Use**  
ATC uses a black-box probing method to actively learn and document new tool usages by creating and testing tool-use instances.

### **Real-World Applicability**  
ATC is designed for complex tasks requiring multiple tool interactions. It is useful in scenarios requiring automation of real-world tasks and has shown success in datasets with long, documented protocols.

---

## **Toolformer**

Toolformer is a language model that learns to use external tools through a self-supervised process. It determines when and how to call external tools using a filtering mechanism [5].

### **Reasoning Steps**  
Toolformer uses self-supervised learning to identify which API calls reduce loss and are useful.

### **Tool Use**  
Toolformer can access external APIs such as:  
- Calculator  
- Q&A system  
- Search engine  
- Translation system  
- Calendar  

It inserts special tokens to indicate API calls and where responses should be included.

### **Real-World Applicability**  
Toolformer has zero-shot capabilities and broad applicability due to the ability to use different tools dynamically.

---

## **Contrasting Methodologies**

| Feature         | ReAct | LATS | ReST | ATC | Toolformer |
|---------------|------|------|------|-----|------------|
| **Reasoning & Acting** | Interleaved | Tree-based search | Self-critique | Stepwise execution | Self-supervised |
| **Learning** | Few-shot prompt engineering | Search-based refinement | AI self-improvement | Protocol documentation | API call learning |
| **Planning** | Step-by-step | Tree search algorithm | Iterative refinement | Pre-planned execution | Embedded in training data |
| **Tool Interaction** | External APIs | External APIs with search | Web search | Python code for tool chaining | API calls within training data |

---

## **Real-World Applicability Assessment**

| Model        | Application Areas |
|-------------|------------------|
| **ReAct**   | Customer service, data analysis |
| **LATS**    | Coding, web navigation, structured decision-making |
| **ReST**    | Long-form Q&A, iterative training, AI self-critique |
| **ATC**     | Scientific research, business process automation |
| **Toolformer** | Versatile, suitable for multiple real-world applications |

---

## **Citations**

1. REACT : SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS
2. Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models
3. REST MEETS REACT: SELF-IMPROVEMENT FOR MULTI-STEP REASONING LLM AGENT
4. Chain of Tools: Large Language Model is an Automatic Multi-tool Learner
5. Toolformer: Language Models Can Teach Themselves to Use Tools
| **LATS**    | Coding, web navigation, structured decision-making |
| **ReST**    | Long-form Q&A, iterative training, AI self-critique |
| **ATC**     | Scientific research, business process automation |
| **Toolformer** | Versatile, suitable for multiple real-world applications |


### Challenges & Improvements

1. Agent might not always return a promising result.
2. It can be further improved by actually using a DB of ECommerce website.
3. There can be more use of ATC (Automatic Tool Chain) to incorporate more robust code.


# FashionAgent
