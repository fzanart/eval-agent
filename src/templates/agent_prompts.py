"""
this file contains templates for the different types of prompts
"""

SETUP = (
    "Your goal is to assess the effectiveness of the following fact in accurately "
    "debunking climate misinformation and providing relevant, reliable information.\n"
    "To evaluate this, you will ask specific, focused questions aimed at verifying "
    "both the factual accuracy of the claim and its relevance to countering common "
    "misconceptions. \n"
    "Your questions should help clarify the evidence behind the fact, identify any "
    "potential gaps or logical inconsistencies, and determine whether it directly "
    "addresses the misleading information.\n"
    "Each question should aim to:\n"
    "- Validate the factual accuracy of the information.\n"
    "- Assess its relevance and effectiveness in countering the specific climate "
    "misinformation.\n"
    "- Examine whether the fact addresses potential fallacies or misunderstandings in "
    "the original misinformation.\n"
    "Please keep asking questions as long as you are uncertain about the validity and "
    "relevance of the information provided.\n"
    "Format your questions as an unordered list, adding dashes (-) in front of each "
    "one, and begin with the first questions."
)

INPUT = (
    "<misisnformation>\n"
    "\t{claim} \n"
    "</misisnformation>\n"
    "<fact>\n"
    "\t{fact}\n"
    "</fact>"
)

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
    "Based on the answers to your questions, what is your conclusion regarding the "
    "**accuracy** of the fact?, Do you think it is accurate? \n"
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
    "Based on the answers to your questions, what is your conclusion regarding the "
    "**relevance** of the fact to debunking the claim? Do you think it is relevant? \n"
    "Please respond with: \n"
    "<term>\n"
    "\tYes\n"
    "</term>\n"
    "OR \n"
    "<term>\n"
    "\tNo\n"
    "</term>\n"
)
