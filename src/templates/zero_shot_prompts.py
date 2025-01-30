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


ZS_ACCURACY_DECISION_CURRENT_RUBTRIC = (
    "You are an expert in evaluating the quality of a misinformation debunking. "
    "You will be given a claim, and a fact that attempts to debunk the claim. "
    "You should focus only on the accuracy of the fact.\n"
    "Is the fact accurate?\n"
    "\n"
    "<claim>\n"
    "\t{claim} \n"
    "</claim>\n"
    "<fact>\n"
    "\t{fact}\n"
    "</fact>"
    "\n"
    "Please respond with one of the following options: \n"
    "- completely inaccurate\n"
    "- mostly inaccurate\n"
    "- mostly accurate\n"
    "- completely accurate\n"
    "Format your answer enclosed in angle brackets, e.g., <completely accurate>."
)

ZS_RELEVANCE_DECISION_CURRENT_RUBTRIC = (
    "You are an expert in evaluating the quality of a misinformation debunking. "
    "You will be given a claim, and a fact that attempts to debunk the claim. "
    "You should focus only on the relevance of the fact to the claim. \n"
    "Is the fact relevant to the claim?\n"
    "\n"
    "<claim>\n"
    "\t{claim} \n"
    "</claim>\n"
    "<fact>\n"
    "\t{fact}\n"
    "</fact>"
    "\n"
    "Please respond with one of the following options: \n"
    "- completely irrelevant\n"
    "- mostly irrelevant\n"
    "- mostly relevant\n"
    "- completely relevant\n"
    "Format your answer enclosed in angle brackets, e.g., <completely relevant>."
)

ZS_GENERATIVE_DEBUNKING_RUBRIC = (
    "You are an expert in evaluating the quality of a misinformation debunking. "
    "You will be given a claim, and a fact that attempts to debunk the claim. "
    "\n"
    "<claim>\n"
    "\t{claim} \n"
    "</claim>\n"
    "<fact>\n"
    "\t{fact}\n"
    "</fact>"
    "\n"
    "Evaluate how effectively the rebuttal counters the myth by providing a factual "
    "alternative. Consider the following criteria:\n"
    '- excellent: Includes a relevant, "sticky" fact that is accurate and free from '
    'allacies. "Sticky" means it is simple, unexpected, credible, concrete, emotional, '
    "or tells a story.\n"
    '- good: Includes a relevant but "non-sticky" fact that is accurate and free '
    "from fallacies.\n"
    "- needs Improvement: Includes a fact that is inaccurate, irrelevant, or contains "
    "a fallacy.\n"
    "- inadequate: The explanation is nonsensical or lacks a relevant fact.\n"
    "Please respond with one classification enclosed in angle brackets, e.g., <excellent>."
)
