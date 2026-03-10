# Scoring Function

**Definition:**
- The **scoring function** determines how to transform the predictions of a language model into an estimate of the likelihood of a specific answer.

**Understanding Its Purpose:**
- The answer with the highest probability obtained from the scoring function is selected as the final answer.

## Different Scoring Functions Used

1. **Direct Method**
   - Uses conditional probability of candidate answers represented by tokens in the model’s vocabulary (Brown et al., 2020).
   - Limitation: Requires answer tokens to be at the end of input sequences, restricting template design.

2. **Perplexity (PPL)**
   - Computes the sentence perplexity of the entire input sequence \( S_j = \{C, s(x, y_j, I)\} \).
   - Evaluates the probability of the sentence, allowing more flexibility in token positions but needing additional computational time.

3. **Channel Model**
   - Estimates the likelihood of the input query given the label.
   - Particularly effective under imbalanced data regimes.

## Key Takeaways
- **Performance:**
  - All existing scoring functions compute a score from the conditional probabilities of language models.
  - They exhibit sensitivity to the demonstration surface and are impacted by the selection and ordering of demonstration examples.
  
- **Research Direction:**
  - Limited studies exist on calibrating bias or mitigating sensitivity with scoring strategies, indicating a need for further exploration and improvement in scoring functions.