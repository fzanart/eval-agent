"""
this file contains templates for the different types of prompts
"""

SETUP = (
    "You are an expert in evaluating the quality of a misinformation debunking. "
    "You will be given a claim, and a fact that attempts to debunk the claim.  "
    "Specifically, you will assess whether the fact is accurate, and whether the fact is relevant "
    "to the claim. You will do this by generating short, "
    "targeted questions designed to verify the accuracy of the fact."
    "- Determine the fact's accuracy."
    "- Determine the fact's relevance to the claim."
    "Please keep asking questions as long as you are uncertain about the validity and "
    "relevance of the information provided.\n"
    "Format your questions as an unordered list, adding dashes (-) in front of each one. "
    "Begin with the first questions."
)

INPUT = "<claim>\n" "\t{claim} \n" "</claim>\n" "<fact>\n" "\t{fact}\n" "</fact>"

ANSWERS = (
    "<instruction> "
    "Analyze the following fact and answer the question below by following these "
    "guidelines: \n"
    " - Use simple, straightforward language.\n"
    " - Present your response in clear, plain text without special formatting.\n"
    " - Ensure your response is factually accurate and based on sound reasoning.\n"
    " - Be concise and focused, avoiding unnecessary details.\n"
    "</instruction>\n"
    "<fact>\n"
    "\t{fact}\n"
    "</fact>\n"
    "<question>\n"
    "\t{question}\n"
    "</question>\n"
)

FOLLOWUP = (
    "Do you have any follow-up questions? \n"
    "Please respond with: \n"
    "<term>\n"
    "\tYes\n"
    "</term>\n"
    "OR \n"
    "<term>\n"
    "\tNo\n"
    "</term>\n"
)

FOLLOWUP_QUESTIONS = (
    "What are the follow-up questions? \n"
    "Format each question as an unordered list item, using a dash (-) at the beginning "
    "of each line."
)

ACCURACY_DECISION = (
    "Based on the answers to your questions, is the fact accurate? \n"
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
    "Based on the answers to your questions, is the fact relevant to the claim? \n"
    "Please respond with: \n"
    "<term>\n"
    "\tYes\n"
    "</term>\n"
    "OR \n"
    "<term>\n"
    "\tNo\n"
    "</term>\n"
)

GENERATIVE_DEBUNKING_RUBRIC = (
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

ACCURACY_DECISION_CURRENT_RUBTRIC = (
    "Based on the answers to your questions, is the fact accurate? \n"
    "Please respond with one of the following options: \n"
    "- completely inaccurate\n"
    "- mostly inaccurate\n"
    "- mostly accurate\n"
    "- completely accurate\n"
    "Format your answer enclosed in angle brackets, e.g., <completely accurate>."
)

RELEVANCE_DECISION_CURRENT_RUBTRIC = (
    "Based on the answers to your questions, is the fact relevant to the claim? \n"
    "Please respond with one of the following options: \n"
    "- completely irrelevant\n"
    "- mostly irrelevant\n"
    "- mostly relevant\n"
    "- completely relevant\n"
    "Format your answer enclosed in angle brackets, e.g., <completely relevant>."
)
