"""
Zero Shot Analysis

This module provides a class for performing zero-shot analysis on a claim and a fact 
using a language model.  The analysis includes evaluating the accuracy and relevance 
of the fact with respect to the claim.

"""

import logging
import logging.config
import yaml
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from .templates.zero_shot_prompts import ACCURACY_DECISION, RELEVANCE_DECISION, INPUT

TEMPLATES = {
    "accuracy": ACCURACY_DECISION,
    "relevance": RELEVANCE_DECISION,
    "input": INPUT,
}

# Load logging configuration from YAML file
with open("logging.yaml", "r") as f:
    config = yaml.safe_load(f)

# create logger
logging.config.dictConfig(config)
logger = logging.getLogger("app")


class ZeroShotAnalysis:
    def __init__(self, model, templates=None):
        # model init
        self.model = model
        self.claim = None
        self.fact = None
        # system template prompts:
        if templates is None:
            templates = TEMPLATES
        self.templates = templates

    def evaluate(self, evaluation):

        messages = []

        messages.append(SystemMessage(content=self.templates[evaluation]))

        prompt_template = PromptTemplate(
            template=self.templates["input"],
            input_variables=["claim", "fact"],
        )
        messages.append(
            HumanMessage(
                content=prompt_template.invoke(
                    {"claim": self.claim, "fact": self.fact}
                ).text
            )
        )

        result = self.model.invoke(messages)
        result = self.cleanup_resposnse(result.content)
        return result

    def analyze(self, claim, fact):
        self.claim = claim
        self.fact = fact
        # generate prompts
        accuracy_decision = self.evaluate("accuracy")
        relevance_decision = self.evaluate("relevance")

        return accuracy_decision, relevance_decision

    def cleanup_resposnse(self, response):
        response = response.lower()
        cleaned_response = response.replace("<term>", "").replace("</term>", "").strip()
        return cleaned_response
