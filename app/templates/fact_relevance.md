# Misinformation Debunking Relevance Evaluation

## Objective

You are evaluating how well facts address climate change misinformation claims. Assess whether the fact directly engages with the claim's core argument - accuracy is handled separately.

## Evaluation Process

1. Analyze the claim's primary assertion
2. Examine which aspects of the claim (if any) the fact addresses
3. Determine relevance using these criteria:
   - Directness: Does it counter the specific claim mechanism?
   - Completeness: Does it address all key claim elements?
   - Logical Connection: Is there clear cause/effect relationship?

## Label Definitions

1. **Completely Relevant:**  
   - Directly counters ALL main claim elements  
   - Addresses same mechanisms/arguments  
   - Example: Claim "CO2 doesn't cause warming" vs Fact showing CO2's IR absorption  

2. **Mostly Relevant:**  
   - Addresses primary claim but misses 1-2 nuances  
   - Counters main mechanism but misses secondary aspects  
   - Example: Claim "warming stopped after 1998" vs Fact showing long-term trend while ignoring specific 1998 events  

3. **Mostly Irrelevant:**  
   - Only addresses tangential/ancillary claim elements  
   - Uses related but non-responsive arguments  
   - Example: Claim "solar cycles cause warming" vs Fact about CO2 levels rising  

4. **Completely Irrelevant:**  
   - Addresses different subject matter entirely  
   - No logical connection to claim mechanisms  
   - Example: Claim "polar bears are thriving" vs Fact about heatwave frequency  

## Examples Table

| Claim                                                                 | Fact                                                                 | Label               | Reasoning                                                                 |
|-----------------------------------------------------------------------|----------------------------------------------------------------------|---------------------|---------------------------------------------------------------------------|
| "Climate action is driven by financial interests rather than science" | "The scientific consensus on climate change is based on peer-reviewed research from independent institutions worldwide."          | **Mostly Relevant** | Addresses scientific basis but doesn't counter financial motive claims    |
| "The climate agenda is a political fraud for control"                 | "Multiple independent investigations found no fraud in climate science, with consensus supported by decades of public data."       | **Completely Relevant** | Directly counters both fraud allegations and control narrative            |
| "Scientists exaggerate data to get funding"                           | "97% of climate scientists agree on human-caused warming based on publicly available datasets from multiple sources."              | **Mostly Relevant** | Supports consensus but doesn't address funding motivation mechanisms      |
| "Global warming claims benefit renewable energy companies"            | "Temperature projections match observed data across public/private research groups, regardless of industry affiliations."          | **Completely Relevant** | Counters exaggeration claim and addresses industry influence angle        |
| "Climate consensus is manufactured by academic elites"                | "Over 200 scientific organizations worldwide endorse climate consensus, including developing nations' research institutions."     | **Mostly Relevant** | Addresses breadth of consensus but not elite control allegations          |
| "Natural cycles explain all warming"                                  | "Multiple studies show observed warming patterns match greenhouse gas models but don't align with natural cycle projections."      | **Completely Relevant** | Directly engages with natural causes argument through mechanism analysis  |
| "Climate models constantly fail"                                      | "IPCC AR6 shows climate models accurately predicted 1990-2020 warming within 5% margin when accounting for real emissions."         | **Completely Relevant** | Specific performance counterargument to modeling reliability claim        |

## Critical Evaluation Guidelines

1. **Argument Mapping:** Identify the claim's core argument structure before assessing relevance
2. **Mechanism Matching:** Verify if the fact addresses the same causal pathways as the claim
3. **Scope Alignment:** Check if geographical/temporal scales match (global vs local, decades vs millennia)
4. **Counterfactual Test:** Could this fact logically weaken the claim if proven true?
5. **Red Herring Detection:** Watch for facts that seem related but address different causal layers

## Input/Output Format

<claim>
    {myth}
</claim>

<fact>
    {fact}
</fact>

Respond ONLY with one label:

- completely relevant
- mostly relevant
- mostly irrelevant
- completely irrelevant
