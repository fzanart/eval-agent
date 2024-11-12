"""
this file contains templates for the different types of prompts
"""

INPUT = "<claim>\n\t{claim} \n</claim>\n<fact>\n\t{fact}\n</fact>"

BAD_SAMPLE = (
    "You are a synthetic data generator. You will be given a claim along with a fact "
    "that is relevant and accurate to debunk this claim.\n"
    "Your task is to generate a deliberately irrelevant and inaccurate fact that fails "
    "to address the claim.\n"
    "This fact should be clearly distinguishable as inappropriate for fact-checking "
    "purposes.\n"
    "Limit your answer two sentences or less than 30 words, enclosed by <fact> and "
    "</fact> delimiters."
)


TOPICALLY_RELATED_SAMPLE = (
    "You are a synthetic data generator. You will be given a claim along with a fact "
    "that is relevant and accurate to debunk this claim.\n"
    "Your task is to generate a deliberately irrelevant and inaccurate fact that fails "
    "to address the claim, yet is related to the topic of the claim.\n"
    "Limit your answer two sentences or less than 30 words, enclosed by <fact> and "
    "</fact> delimiters."
)


REASONABLE_SAMPLE = (
    "You are a synthetic data generator. You will be given a claim along with a fact "
    "that is relevant and accurate to debunk this claim.\n"
    "Your task is to generate a fact that reasonably addresses the claim, though not "
    "as effectively as the original fact.\n"
    "Limit your answer two sentences or less than 30 words, enclosed by <fact> and "
    "</fact> delimiters."
)
