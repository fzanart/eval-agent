"""
this file contains templates for the different types of prompts
"""

ACCURACY_DECISION = (
    "Analyze the following fact in relation to the claim presented, focusing on how "
    "effectively it counters or debunks the claim."
    "Is the fact accurate?\n"
    "Please respond with: \n"
    "<term>\n"
    "\tYes\n"
    "</term>\n"
    "OR \n"
    "<term>\n"
    "\tNo\n"
    "</term>\n"
)

RELEVANCE_DECISION = (
    "Analyze the following fact in relation to the claim presented, focusing on how "
    "effectively it counters or debunks the claim."
    "Is the fact relevant to the claim?\n"
    "Please respond with: \n"
    "<term>\n"
    "\tYes\n"
    "</term>\n"
    "OR \n"
    "<term>\n"
    "\tNo\n"
    "</term>\n"
)

INPUT = "<claim>\n\t{claim} \n</claim>\n<fact>\n\t{fact}\n</fact>"
