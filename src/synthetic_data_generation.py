from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
from .templates.synthetic_data_pompts import (
    INNACURATE_BUT_RELEVANT,
    ACCURATE_BUT_IRRELEVANT,
    INNACURATE_AND_IRRELEVANT,
)

TEMPLATES = {
    "innacurate_but_relevant": INNACURATE_BUT_RELEVANT,
    "accurate_but_irrelevant": ACCURATE_BUT_IRRELEVANT,
    "innacurate_and_irrelevant": INNACURATE_AND_IRRELEVANT,
}


class SynteticSampleGenerator:
    def __init__(self, model, templates=None):
        # model init
        self.model = model
        self.claim = None
        # system template prompts:
        if templates is None:
            templates = TEMPLATES
        self.templates = templates

    def generate(self, claim):
        self.claim = claim
        # generate prompts
        innacurate_but_relevant = self.create_sample("innacurate_but_relevant")
        accurate_but_irrelevant = self.create_sample("accurate_but_irrelevant")
        innacurate_and_irrelevant = self.create_sample("innacurate_and_irrelevant")
        return (
            innacurate_but_relevant,
            accurate_but_irrelevant,
            innacurate_and_irrelevant,
        )

    def create_sample(self, sample_type):

        prompt_template = PromptTemplate(
            template=self.templates[sample_type],
            input_variables=["claim"],
        )
        message = HumanMessage(
            content=prompt_template.invoke({"claim": self.claim}).text
        )

        result = self.model.invoke(message)
        result = self.cleanup_response(result.content)
        return result

    def cleanup_response(self, response):
        cleaned_response = response.replace("<text>", "").replace("</text>", "").strip()
        return cleaned_response
