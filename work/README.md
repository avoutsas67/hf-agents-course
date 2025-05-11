# Course work for Hugging Face Agent Course

## Agent whitepapers

* [AI Agents research](https://medium.com/@gianetan/ai-agents-research-papers-and-whitepaper-ca45e69c1a96)

### Google

* [Agents](https://www.kaggle.com/whitepaper-agents)
* [Agents companion](https://www.kaggle.com/whitepaper-agent-companion)

### Anthropic

* [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)

## Agent SDKs

### Amazon Bedrock

* [Amazon Bedrock agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)

### OpenAI Agent SDK

* [Use Azure OpenAI and APIM with the OpenAI Agents SDK](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/use-azure-openai-and-apim-with-the-openai-agents-sdk/4392537)

## Smollagents

### Walkthrough

[Smollagents walkthrough notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/smolagents_doc/en/pytorch/guided_tour.ipynb)

### Examples

[Text-to-SQL PyTorch](https://colab.research.google.com/github/huggingface/notebooks/blob/main/smolagents_doc/en/pytorch/text_to_sql.ipynb#scrollTo=3XBVoGZQyEVc)

## Unit 1

### Colab notebooks

[Dummy Agent Library](https://colab.research.google.com/#fileId=https%3A//huggingface.co/agents-course/notebooks/blob/main/dummy_agent_library.ipynb)

## Comparison of Agentic frameworks by Claude

I'll search for information about the most popular AI Agent Python SDKs currently available:

Let me search for more specific information about popular AI agent Python SDKs and their technical details:

Based on my research, here are the most popular AI Agent Python SDKs currently available, along with their key features and use cases:

### 1. LangChain

LangChain is one of the most established and widely-used frameworks for building AI agents.

**Key Features:**
- Comprehensive ecosystem with extensive documentation and community support
- Modular architecture with chains, memory systems, and tool integration
- Pre-built agent types (ReAct, OpenAI Functions, etc.)
- Integration with various LLMs, vector stores, and external tools
- LangSmith for debugging and monitoring

**Best For:** 
- Complex applications requiring various tools and data sources
- Production-ready applications needing robust infrastructure
- Projects requiring data retrieval from multiple sources

**Installation:**
```bash
pip install langchain
```

### 2. LangGraph

LangGraph extends LangChain with graph-based structures for building stateful, multi-agent applications.

**Key Features:**
- Graph-based architecture for flexible workflow management
- State management for complex agent interactions
- Precise control over workflow execution and branching
- Native support for cyclic and multi-step reasoning
- Easy visualization of agent workflows

**Best For:**
- Applications requiring complex, multi-step reasoning
- Systems with multiple agents that need coordination
- Projects needing fine-grained control over execution flow

**Installation:**
```bash
pip install langgraph
```

### 3. CrewAI

CrewAI focuses on simplifying the development of role-based multi-agent systems.

**Key Features:**
- Intuitive role-based agent definition
- Easy-to-understand task delegation and collaboration
- Built on LangChain with simplified abstractions
- Built-in agent memory and collaboration patterns
- Lower learning curve than other frameworks

**Best For:**
- Projects requiring simulated team collaboration
- Quick prototyping of multi-agent systems
- Applications where agents need distinct roles and responsibilities

**Installation:**
```bash
pip install crewai
```

### 4. Microsoft AutoGen

AutoGen, developed by Microsoft, provides a framework for multi-agent conversation-based workflows.

**Key Features:**
- Event-driven conversation-based architecture
- Secure code execution in Docker containers
- Visual interface through AutoGen Studio
- Support for multiple programming languages (Python, .NET)
- Strong focus on agent-to-agent communication

**Best For:**
- Dynamic problem-solving through agent collaboration
- Applications requiring secure code execution
- Projects needing flexible, conversation-based workflows

**Installation:**
```bash
pip install pyautogen
```

### 5. LlamaIndex

LlamaIndex (formerly GPT Index) specializes in data indexing and retrieval but has expanded to include agent capabilities.

**Key Features:**
- Robust data indexing and RAG capabilities
- Efficient data structures for document processing
- Event-driven workflow architecture
- Strong focus on data-centric applications
- Integration with various data sources and formats

**Best For:**
- Applications requiring advanced document retrieval
- Data-heavy tasks with large document collections
- Context-aware question answering systems

**Installation:**
```bash
pip install llama-index
```

### 6. OpenAI Assistants API & Swarm SDK

OpenAI's Assistants API and their experimental Swarm SDK provide a way to build and coordinate multiple AI agents.

**Key Features:**
- Direct integration with OpenAI's models
- Built-in file handling and retrieval
- Simple, lightweight design
- Managed infrastructure (for Assistants API)
- Tool use and function calling capabilities

**Best For:**
- Lightweight prototyping
- Projects exclusively using OpenAI models
- Applications where simplicity is prioritized over customization

**Installation:**
```bash
pip install openai
```

### 7. SmolaGents

Developed by Hugging Face, SmolaGents takes a minimalist approach to agent development.

**Key Features:**
- Code-centric approach to agent development
- Small, lightweight design with minimal dependencies
- Support for various models beyond OpenAI
- Simple integration with Hugging Face ecosystem
- Focus on code generation and execution

**Best For:**
- Projects requiring compact and simple agent implementations
- Applications where the agent primarily writes and executes code
- Developers who prefer a minimalist approach

**Installation:**
```bash
pip install smolagents
```

### 8. Microsoft Semantic Kernel

Semantic Kernel is Microsoft's framework for integrating AI capabilities into applications.

**Key Features:**
- Cross-language support (Python, C#, Java)
- Enterprise-focused with security and compliance features
- Strong integration with Azure services
- Structured planning capabilities
- Combination of AI and traditional code

**Best For:**
- Enterprise applications requiring security and compliance
- Projects integrating AI with existing .NET/Java systems
- Applications requiring formal planning capabilities

**Installation:**
```bash
pip install semantic-kernel
```
### How to Choose?

When selecting an AI agent SDK, consider these factors:

1. **Project Complexity**: For complex workflows with multiple steps, LangGraph or AutoGen may be best. For simpler agents, CrewAI or SmolaGents might be more appropriate.

2. **Data Requirements**: If your application is data-heavy, LlamaIndex excels at retrieval and indexing.

3. **Development Speed**: CrewAI is often cited as having the quickest setup time for multi-agent systems.

4. **Model Flexibility**: If you need to work with models beyond OpenAI, frameworks like LangChain and SmolaGents offer broader compatibility.

5. **Enterprise Needs**: For enterprise applications, Semantic Kernel provides stronger security and integration with enterprise systems.

Each framework continues to evolve rapidly, with new features and capabilities being added regularly. The best choice depends on your specific use case, technical requirements, and development preferences.