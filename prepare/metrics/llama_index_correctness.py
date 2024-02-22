from unitxt import add_to_catalog
from unitxt.metrics import (
    LlamaIndexCorrectnessMetric,
)
from unitxt.test_utils.metrics import test_metric

model_name = "gpt-3.5-turbo"
metric = LlamaIndexCorrectnessMetric(model_name=model_name)

predictions = ["The right answer"]
references = [["The right answer", "The wrong answer"]]
task_data = [
    {
        "question": "question number 1",
        "contexts": "['context number 1']",
        # "reference_answers": ["The right answer", "The wrong answer"],
    },
]

model_name_normalized = model_name.replace(".", "_").replace("-", "_")
score_name = f"correctness_llama_index_by_{model_name_normalized}_judge"

instance_targets = [  # nDCG is undefined at instance level
    {
        "score": 1.0,
        "score_name": score_name,
        score_name: 1.0,
        # "feedback": "The generated answer is fully correct and relevant to the user query, matching the reference answer exactly.",
    }
] * len(predictions)

global_target = {
    "score": 1.0,
    "score_name": score_name,
    score_name: 1.0,
}

outputs = test_metric(
    metric=metric,
    predictions=predictions,
    references=references,
    task_data=task_data,
    instance_targets=instance_targets,
    global_target=global_target,
)

add_to_catalog(metric, "metrics.rag.llama_index_correctness", overwrite=True)
