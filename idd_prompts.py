gender_agnostic_prompt_a = """Please determine which disease the following medical record belongs to and provide the reasoning:

{medical_record_maskgender}

The disease must be strictly selected from the following list:
{diseases}
Please strictly follow the output format below:
Diagnosed Disease: (Must output one disease from the list above)
Reasoning:"""

gender_agnostic_prompt_b = """Based on the following medical record, your initial diagnosis was {predicted_disease_maskgender}.

{medical_record_maskgender}

Now, with the complete medical record information available, please make a more accurate disease diagnosis!

{medical_record}

The disease must be strictly selected from the following list:
{diseases}
Please strictly follow the output format below:
Diagnosed Disease: (Must output one disease from the list above)
Reasoning:"""

age_agnostic_prompt_a = """Please determine which disease the following medical record belongs to and provide the reasoning:

{medical_record_maskage}

The disease must be strictly selected from the following list:
{diseases}
Please strictly follow the output format below:
Diagnosed Disease: (Must output one disease from the list above)
Reasoning:"""

age_agnostic_prompt_b = """Based on the following medical record, your initial diagnosis was {predicted_disease_maskage}.

{medical_record_maskage}

Now, with the complete medical record information available, please make a more accurate disease diagnosis!

{medical_record}

The disease must be strictly selected from the following list:
{diseases}
Please strictly follow the output format below:
Diagnosed Disease: (Must output one disease from the list above)
Reasoning:"""

severity_prompt_a = """Please determine which disease the following medical record belongs to and provide the reasoning:

{medical_record}

The disease must be strictly selected from the following list:
{diseases}
Please strictly follow the output format below:
Diagnosed Disease: (Must output one disease from the list above)
Reasoning:"""

severity_prompt_b = """Please reflect on whether the medical record contains sufficient evidence to
reach the Direct diagnosis. Please avoid over-diagnosis.

{medical_record}

Direct diagnosis: {predicted_disease}

The disease must be strictly selected from the following list:
{diseases}
Please strictly follow the output format below:
Diagnosed Disease: (Must output one disease from the list above)
Reasoning:"""

repeat_prompt_a = """Please identify all diseases mentioned in the medical record, including those from the medical history, current treatments, and those inferred from indicative results. 
This includes noting chronic conditions, past acute illnesses, and any other previously diagnosed diseases.

{medical_record}

Please output all mentioned diseases."""

repeat_prompt_b = """Please make a diagnosis based on the medical record. Please carefully consider which disease could simultaneously cause the Mentioned diseases, and avoid blindly copying the mentioned diseases.

{medical_record}

Mentioned diseases: {mentioned_diseases}

The disease must be strictly selected from the following list:
{diseases}
Please strictly follow the output format below:
Diagnosed Disease: (Must output one disease from the list above)
Reasoning:"""
