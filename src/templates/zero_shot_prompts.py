"""
this file contains templates for the different types of prompts
"""

ACCURACY_DECISION = (
    "You are an expert in evaluating the quality of a misinformation debunking. "
    "You will be given a claim, and a fact that attempts to debunk the claim. "
    "You should focus only on the accuracy of the fact.\n"
    "Is the fact accurate?"
    "Please respond with: \n"
    "<term>\n"
    "\tYes\n"
    "</term>\n"
    "OR \n"
    "<term>\n"
    "\tNo\n"
    "</term>\n"
    "<claim>\n"
    "\t{claim} \n"
    "</claim>\n"
    "<fact>\n"
    "\t{fact}\n"
    "</fact>"
)

RELEVANCE_DECISION = (
    "You are an expert in evaluating the quality of a misinformation debunking. "
    "You will be given a claim, and a fact that attempts to debunk the claim. "
    "You should focus only on the relevance of the fact to the claim. \n"
    "Is the fact relevant to the claim?\n"
    "Please respond with: \n"
    "<term>\n"
    "\tYes\n"
    "</term>\n"
    "OR \n"
    "<term>\n"
    "\tNo\n"
    "</term>\n"
    "<claim>\n"
    "\t{claim} \n"
    "</claim>\n"
    "<fact>\n"
    "\t{fact}\n"
    "</fact>"
)
