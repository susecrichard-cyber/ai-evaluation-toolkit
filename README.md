# AI Evaluation Toolkit

Tools and examples for evaluating AI-generated content: prompt evaluation, response ranking, rubric-based review, and hallucination detection.

Built by Richard Frimpong.

## What is in here

- `evaluate.py` — a small, example rubric scorer. Give it a prompt, a response, and a rubric, and it scores the response on each rubric item.
- `examples/sample_responses.json` — sample prompt/response pairs to try it with.

These are example / learning scripts, not a production service.

## Try it

```bash
python3 evaluate.py examples/sample_responses.json
```

## Rubric used in the example

1. Accuracy — is the answer factually correct?
2. Relevance — does it answer the question asked?
3. Clarity — is it clear and easy to follow?
4. Completeness — does it cover what was asked, without adding unrelated claims?
```

