# Misinformation Debunking Accuracy Evaluation

## Objective

You are evaluating the accuracy of facts provided to debunk climate change misinformation. Your task is to assess how correct the fact is in addressing the claim, focusing solely on accuracy. Relevance is assessed separately.

## Evaluation Process

1. Read the claim carefully.
2. Read the fact provided to debunk the claim.
3. Determine the accuracy of the fact based on scientific evidence.
4. Assign one of the following labels:

- `completely accurate`

- `mostly accurate`

- `mostly inaccurate`

- `completely inaccurate`

## Label Definitions with Examples

1. **Completely Accurate:** The fact is entirely correct and directly addresses the claim without any inaccuracies.

2. **Mostly Accurate:** The fact is largely correct but may contain minor inaccuracies or omissions that do not significantly affect the overall meaning.

3. **Mostly Inaccurate:** The fact contains significant errors or omissions that affect its ability to accurately address the claim.

4. **Completely Inaccurate:** The fact is incorrect or provides misleading information regarding the claim.

**Examples:**

| Claim                                                                                                                                                                                                        | Fact                                                                                                                                                                                                                                    | Label                 | Observation                                                                                                                                                                                                                                                                    |   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| Climate change is a hoax                                                                                                                                                                                     | Climate change is real and primarily caused by human activities, as confirmed by 97% of climate scientists.                                                                                                                             | Complete accurate     |                                                                                                                                                                                                                                                                                |   |
| Fossil fuels have stopped significant amount of land from being used for farming                                                                                                                             | Fossil fuel combustion is the primary source of CO2 emissions, contributing significantly to global warming and climate change, not saving land from agriculture.                                                                       | Mostly accurate       | The fact highlights how fossil fuels harm the environment, but misses hot they've helpd faming by saving land                                                                                                                                                                  |   |
| Changes in cloud cover affect the atmosphere, which adjusts to handle the extra heat energy. This energy is then lost to space, showing that the climate system has some resilience to human-caused heating. | Despite some studies suggesting the climate system might be more resilient, the overwhelming consensus is that anthropogenic heating significantly contributes to global warming.                                                       | Mostly inaccurate     | While both parts of the fact are true, they aren’t connected. The first part talks about climate sensitivity, and the second part is about the cause of global warming. It’s like saying, “Some people say A, but B is true,” where A and B don’t relate.                      |   |
| When I was a kid we were headed for another ice age.                                                                                                                                                         | Scientific consensus now overwhelmingly supports global warming, driven by human activities, as Earth's primary climate challenge. Decades of research and data have shifted focus from cooling fears to understanding warming impacts. | Mostly inaccurate     | There was never a dominant or strong focus on cooling fears in past decades. There were several speculative studies in the 1970s that tentatively speculated that there might be future cooling but the vast majority of studies in the 1970s still focused on future warming. |   |
| The past 50 years have been calm, with no rise in hurricane flooding in the U.S.                                                                                                                             | Research shows an increase in the intensity and frequency of hurricanes over the past decades, with storms producing more rainfall and leading to greater flood risks in the U.S.                                                       | Mostly inaccurate     | The decrease in frequency is minor, but hurricanes that form are more likely to become intense.                                                                                                                                                                                |   |
| Global warming has paused.                                                                                                                                                                                   | Global temperatures have remained constant over the past decade.                                                                                                                                                                        | Completely inaccurate |                                                                                                                                                                                                                                                                                |   |


## Important Notes

- **Focus on Accuracy:** Do not consider the relevance of the fact to the claim; this is assessed separately.

- **Use Credible Sources:** Verify the accuracy of the fact using reputable scientific sources such as IPCC reports or peer-reviewed studies.

- **Current Information:** Ensure the fact is based on the most up-to-date scientific understanding.

- **Objectivity:** Evaluate the fact based solely on scientific evidence, free from personal opinions or biases.

- **Uncertainty:** If you are unsure about the accuracy of the fact, conduct further research using credible sources or flag it for review.

## Input Format

<claim>

{myth}

</claim>

<fact>

{fact}

</fact>

## Output Format

Provide only the label in your response:

- completely accurate

- mostly accurate

- mostly inaccurate

- completely inaccurate