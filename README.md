**GenAI with LangChain**

A practical, hands-on repository documenting everything learned and implemented while learning Generative AI using LangChain which includes runnable examples covering prompts, models, structured output, chains, RAG, tools, tool-calling, and agents.

**Repository Structure**

GenAI-with-LangChain/
│
│── langchain_models/
│   ├── 1_LLMS/
│   │   └── llms_demo.py
│   ├── 2_ChatModels/
│   │   ├── 1_openai.py
│   │   ├── 2_anthropic.py
│   │   ├── 3_google.py
│   │   ├── 4_hf_api.py
│   │   └── 5_hf_local.py
│   └── 3_EmbeddedModels/
│       ├── 1_openai_query.py
│       ├── 2_openaidocs.py
│       ├── 3_hf_local.py
│       └── 4_similarity.py
│
│── langchain_prompts/
│   ├── 1_prompt_ui.py
│   ├── 2_prompt_generator.py
│   ├── 3_prompt_template.py
│   ├── 4_template.json
│   ├── 5_chatbot.py
│   ├── 6_chat_prompt_template.py
│   ├── 7_messages.py
│   ├── 8_chat_history.txt
│   └── 9_messages_placeholder.py
│
│── langchain_structured_output/
│   ├── 1_typeddict_demo.py
│   ├── 2_with_structured_output_typeddict.py
│   ├── 3_pydantic_demo.py
│   ├── 4_with_structured_output_pydantic.py
│   ├── 5_json_schema.json
│   └── 6_with_structured_output_json.py
│
│── langchain_output_parsers/
│   ├── 1_strOutputParser.py
│   ├── 2_strOutputParser1.py
│   ├── 3_jsonOutputParser.py
│   ├── 4_structuredoutputparser.py
│   └── 5_pydanticoutputparser.py
│
│── langchain_chains/
│   ├── 1_simple_chain.py
│   ├── 2_sequential_chain.py
│   ├── 3_parallel_chain.py
│   └── 4_conditional_chain.py
│
│── langchain_runnables/
│   ├── 1_runnable_sequence.py
│   ├── 2_runnable_parallel.py
│   ├── 3_runnable_passthrough.py
│   ├── 4_runnable_lambda.py
│   └── 5_runnable_branch.py
│
│── langchain_document_loaders/
│   ├── 1_football.txt
│   ├── 2_text_loader.py
│   ├── 3_Gen AI.pdf
│   ├── 4_pdf_loader.py
│   ├── 5_directory_loader.py
│   ├── 6_webbase_loader.py
│   ├── 7_Social_Network_Ads.csv
│   └── 8_csv_loader.py
│
│── langchain_text_splitters/
│   ├── 1_length_based.py
│   ├── 2_text_structure_based.py
│   ├── 3_document_structured_based_python_code_splitting.py
│   ├── 4_document_structured_based_markdown_splitting.py
│   └── 5_semantic_meaning_based.py
│
│── langchain_vector_store/
│   └── langchain_chroma.py
│
│── langchain_retrievers/
│   ├── 1_wikipedia_retriever.py
│   ├── 2_vector_store_retriever.py
│   ├── 3_maximal_marginal_relevance.py
│   ├── 4_multiquery_retriever.py
│   └── 5_contextual_compression_retriever.py
│
│── langchain_rags/
│   └── main.py
│
│── langchain_tools/
│   ├── 1_built-in-tool_DuckDuckGo Search.py
│   ├── 2_built-in-tool_Shell Tool.py
│   ├── 3_custom_tools_method1.py
│   ├── 4_custom_tools_method2.py
│   ├── 5_custom_tools_method3.py
│   └── 6_Toolkit.py
│
│── langchain_tools_calling/
│   └── main.py
│
└── langchain_agents/
    └── agents.py

**Purpose**

To serve as a structured learning resource and reference guide for building real GenAI applications with LangChain — from fundamentals to advanced agents & tools.

