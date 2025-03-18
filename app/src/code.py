import os
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from typing import Literal
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"


class EvalWorkflow:
    def __init__(self):
        self.llm = ChatOpenAI(
            temperature=0,
            openai_api_key=os.environ.get("OPENAI_API_KEY"),
            openai_organization=os.environ.get("OPENAI_ORGANIZATION_ID"),
            model_name="gpt-4o-2024-05-13",
        )
        self.data = pd.read_csv(
            "input/debunking_all.csv",
        )
        self.chains = {}

    def run_eval(
        self,
        prompt_type: Literal[
            "fact_accuracy", "fact_relevance", "fallacy_correctness", "fallacy_clarity"
        ],
        chain_type: Literal["fact_1", "fact_2", "fallacy"],
    ):
        # Create a Runnable Chain

        prompt_map = {
            "fact_accuracy": (TEMPLATES_DIR / "fact_accuracy.md").read_text(
                encoding="utf-8"
            ),
            "fact_relevance": (TEMPLATES_DIR / "fact_relevance.md").read_text(
                encoding="utf-8"
            ),
            "fallacy_clarity": (TEMPLATES_DIR / "fallacy_clarity.md").read_text(
                encoding="utf-8"
            ),
            "fallacy_correctness": (TEMPLATES_DIR / "fallacy_correctness.md").read_text(
                encoding="utf-8"
            ),
        }

        variable_map = {
            "fact_1": ("fact", "fact_1"),
            "fact_2": ("fact", "fact_2"),
            "fallacy": ("explanation", "fallacy"),
        }

        for i in range(len(self.data)):
            variable_name, column_name = variable_map[chain_type]
            partial_variables = {
                "myth": self.data.loc[i, "claim"],
                variable_name: self.data.loc[i, column_name],
            }

            if chain_type == "fallacy":
                partial_variables["fallacy"] = self.data.loc[i, "pred_fallacy"]
            if prompt_type == "fallacy_clarity":
                partial_variables["fact"] = self.data.loc[i, "fact_1"]

            # Create a prompt for each row with specific claim and fact
            prompt = PromptTemplate(
                template=prompt_map[prompt_type],
                partial_variables=partial_variables,
            )
            # Create a chain for each row
            chain_name = f"row_{i}"
            self.chains[chain_name] = prompt | self.llm

        # Create a parallel runner
        runner = RunnableParallel(**self.chains)

        # Batch Process the Data
        results = runner.invoke({})

        # Extract and clean evaluations
        evals = [self.clean_label(v.content, prompt_type) for k, v in results.items()]

        return evals

    def clean_label(
        self,
        text,
        label_type: Literal[
            "fact_accuracy", "fact_relevance", "fallacy_correctness", "fallacy_clarity"
        ],
    ):

        label_map = {
            "fact_accuracy": [
                "completely accurate",
                "mostly accurate",
                "mostly inaccurate",
                "completely inaccurate",
            ],
            "fact_relevance": [
                "completely relevant",
                "mostly relevant",
                "mostly irrelevant",
                "completely irrelevant",
            ],
            "fallacy_correctness": [
                "completely incorrect",
                "mostly incorrect",
                "mostly correct",
                "completely correct",
            ],
            "fallacy_clarity": [
                "completely unclear",
                "mostly unclear",
                "mostly clear",
                "completely clear",
            ],
        }

        valid_labels = label_map[label_type]

        for label in valid_labels:
            if label in text.lower():
                return label

        return text
