import os
import re
import difflib
import logging
import logging.config
from collections import defaultdict
import yaml
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from langchain_core.runnables import RunnableParallel
from .templates import (
    SETUP,
    INPUT,
    ANSWERS,
    FOLLOWUP,
    FOLLOWUP_QUESTIONS,
    ACCURACY_DECISION,
    RELEVANCE_DECISION,
)


# Load logging configuration from YAML file
with open("logging.yaml", "r") as f:
    config = yaml.safe_load(f)


# create logger
logging.config.dictConfig(config)
logger = logging.getLogger("app")

TEMPLATES = {
    "setup": SETUP,
    "input": INPUT,
    "answers": ANSWERS,
    "followup": FOLLOWUP,
    "followup_questions": FOLLOWUP_QUESTIONS,
    "accuracy_decision": ACCURACY_DECISION,
    "relevance_decision": RELEVANCE_DECISION,
}


class Agent:
    def __init__(self, model, templates=None):
        # graph init
        self.state = defaultdict(list)
        # model init
        self.model = model
        self.claim = None
        self.fact = None
        # system template prompts:
        if templates is None:
            templates = TEMPLATES
        self.templates = templates

    def setup_node(self):

        prompt_template = PromptTemplate(
            template=self.templates["input"],
            input_variables=["claim", "fact"],
        )

        prompt = prompt_template.invoke({"claim": self.claim, "fact": self.fact})

        self.state["messages"].append(SystemMessage(content=self.templates["setup"]))
        self.state["messages"].append(HumanMessage(content=prompt.text))

        messages = self.state["messages"]

        result = self.model.invoke(messages)

        return result.content

    def answers_node(self, questions):

        questions = questions.split("\n")

        chains_dict = {}
        for i, question in enumerate(questions):
            prompt = PromptTemplate(
                template=self.templates["answers"],
                input_variables=["claim"],
                partial_variables={"question": question},
            )

            chain_name = f"answer{i+1}"
            chains_dict[chain_name] = prompt | self.model
            runner = RunnableParallel(**chains_dict)
            results = runner.invoke({"fact": self.fact})

        for question, answer in zip(questions, results.values()):
            self.state["messages"].append(AIMessage(content=question))
            self.state["messages"].append(HumanMessage(content=answer.content))

    def followup_node(self):

        messages = self.state["messages"] + [
            HumanMessage(content=self.templates["followup"])
        ]
        result = self.model.invoke(messages).content

        yes_ratio = difflib.SequenceMatcher(None, result.lower(), "yes").ratio()
        no_ratio = difflib.SequenceMatcher(None, result.lower(), "no").ratio()
        logger.info(
            "\tResult: %s, yes ratio: %f, no ratio: %f", result, yes_ratio, no_ratio
        )
        if yes_ratio > no_ratio:
            self.state["messages"].append(AIMessage(content=result))
            return "yes"
        return "no"

    def followup_questions_node(self):

        self.state["messages"].append(
            HumanMessage(content=self.templates["followup_questions"])
        )
        messages = self.state["messages"]
        result = self.model.invoke(messages).content

        return result

    def decision_node(self):

        messages = self.state["messages"] + [
            HumanMessage(content=self.templates["accuracy_decision"])
        ]
        accuracy_result = self.model.invoke(messages).content

        messages = self.state["messages"] + [
            HumanMessage(content=self.templates["relevance_decision"])
        ]
        relevance_result = self.model.invoke(messages).content

        return {"accuracy": accuracy_result, "relevance": relevance_result}

    def analyze(self, fact, claim, max_turns=5):

        self.claim = claim
        self.fact = fact
        logger.info("1. Claim: %s", claim)
        logger.info("2. Fact: %s", fact)

        questions = self.setup_node()
        logger.info("3. Answering questions...")
        self.answers_node(questions)

        answer = self.followup_node()
        logger.info("4. More questions? %s", answer)

        turn = 0
        while answer == "yes" and turn < max_turns:
            logger.info("5. Turn %d", turn)
            questions = self.followup_questions_node()
            self.answers_node(questions)
            answer = self.followup_node()
            turn += 1

        result = self.decision_node()

        return result
