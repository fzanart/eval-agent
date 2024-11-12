from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from .templates.synthetic_data_pompts import (
    BAD_SAMPLE,
    TOPICALLY_RELATED_SAMPLE,
    REASONABLE_SAMPLE,
    INPUT,
)

TEMPLATES = {
    "really_bad": BAD_SAMPLE,
    "topically_related": TOPICALLY_RELATED_SAMPLE,
    "reasonable": REASONABLE_SAMPLE,
    "input": INPUT,
}


class SynteticSampleGenerator:
    def __init__(self, model, templates=None):
        # model init
        self.model = model
        self.claim = None
        self.fact = None
        # system template prompts:
        if templates is None:
            templates = TEMPLATES
        self.templates = templates

    def generate(self, claim, fact):
        self.claim = claim
        self.fact = fact
        # generate prompts
        really_bad = self.create_sample("really_bad")
        really_bad_but_topically_related = self.create_sample("topically_related")
        reasonable_but_not_as_good = self.create_sample("reasonable")
        return really_bad, really_bad_but_topically_related, reasonable_but_not_as_good

    def create_sample(self, sample_type):

        messages = []

        messages.append(SystemMessage(content=self.templates[sample_type]))

        prompt_template = PromptTemplate(
            template=self.templates["input"],
            input_variables=["claim", "fact"],
        )
        messages.append(
            HumanMessage(
                content=prompt_template.invoke(
                    {"claim": self.claim, "fact": self.fact}
                ).text
            )
        )

        result = self.model.invoke(messages)
        result = self.cleanup_resposnse(result.content)
        return result

    def cleanup_resposnse(self, response):
        cleaned_response = response.replace("<fact>", "").replace("</fact>", "").strip()
        return cleaned_response
