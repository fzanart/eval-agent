"""
this file contains templates for the different types of prompts
"""

INNACURATE_BUT_RELEVANT = (
    "You are a synthetic data generator. "
    "You will be given a claim that is broadly related to climate change. "
    "Your task is to generate a short statement that is inaccurate, "
    "yet is related to the topic of the claim. Limit your answer two sentences or "
    "less than 30 words, enclosed by <text> and </text> delimiters.\n"
    "<claim>\n\t{claim} \n</claim>\n"
)

ACCURATE_BUT_IRRELEVANT = (
    "You are a synthetic data generator. "
    "You will be given a claim that is broadly related to climate change. "
    "Your task is to generate an accurate fact about climate change, that is irrelevant "
    "to the topic of the claim. Limit your answer two sentences or less than 30 words, "
    "enclosed by <text> and </text> delimiters.\n"
    "<claim>\n\t{claim} \n</claim>\n"
)

INNACURATE_AND_IRRELEVANT = (
    "You are a synthetic data generator. "
    "You will be given a claim that is broadly related to climate change. "
    "Your task is to generate a short statement that is inaccurate, and that is irrelevant "
    "to the topic of the claim. Limit your answer two sentences or less than 30 words, "
    "enclosed by <text> and </text> delimiters.\n"
    "<claim>\n\t{claim} \n</claim>\n"
)
