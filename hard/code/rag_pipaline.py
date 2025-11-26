# rag_pipeline.py (BUG ADDED: Passes trap metadata to LLM step)
import asyncio
import json
from agents import RetrieverAgent, ValidatorAgent
from utils import generate_llm_response # Now accepts trap_meta


class RAGPipeline:
    def __init__(self, dbs, mcp_config_path="mcp_config.json"):
        self.dbs = dbs
        # Load trap metadata for the new bug
        self.trap_meta = self.dbs["trap"]["meta"] # NEW BUG LINE
        with open(mcp_config_path, 'r') as f:
            self.mcp_config = json.load(f)
        
        self.retriever = RetrieverAgent(dbs)
        self.validator = ValidatorAgent(dbs)

    async def run_async(self, query):
        # 1. Retrieval (Will correctly pull good data)
        retrieved_data = await self.retriever.retrieve(query) 

        # 2. Validation
        is_valid = await self.validator.validate(query) 

        if not is_valid or not retrieved_data:
             return {"answer": "Validation failed or no data retrieved.", "evidence": [], "confidence": 0.0}

        # 3. LLM Generation
        # BUG: Pass the misleading trap metadata, which the LLM function will prioritize.
        llm_output = generate_llm_response(query, retrieved_data, trap_meta=self.trap_meta) 
        
        return llm_output

    def run(self, query):
        return asyncio.get_event_loop().run_until_complete(self.run_async(query))