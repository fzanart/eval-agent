import os
import re
import operator
import logging
from typing import TypedDict, Annotated, Sequence
from langgraph.graph import StateGraph, END
from langchain_core.messages import AIMessage, BaseMessage, SystemMessage


logging.basicConfig(level=logging.INFO)


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]


class Agent:
    def __init__(self, model):
        pass
