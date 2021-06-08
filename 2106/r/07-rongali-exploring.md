# Exploring Transfer Learning For End-to-End Spoken Language Understanding
Authors: **Subendhu Rongali, Beiye Liu, Liwei Cai, Konstantine Arkoudas, Chengwei Su, Wael Hamza**

Venue: *AAAI 2021*

Link: [arXiv](https://arxiv.org/abs/2012.08549)

Topics: end-to-end SLU, spoken language understanding, transformer, joint decoder

## Summary

Opens with the core justification of end-to-end SLU. They propose a model that is jointly trained on ASR, SLU, and NLU-level tasks. They call this Audio-Text All-Task (AT-AT). They demonstrate results on both an internal Alexa dataset and on FSC (Fluent Speech Commands) and SNIPS Audio. They highlight the following as core issues hindering E2E SLU deployment:

* Rely on giant neural components and require lots of E2E training data
* Don't make use of ASR and NLU level training data available
* **Feature expansion**: not robust to new domains, intents, and slots

To get around this, they apply transfer learning, jointly training audio- and text-level encoders to text-level decoders. Among the tasks in the mix are ASR, SLU, Cloze, and NLU.

![their figure 1, the model diagram](07-rongali-1.png)

Among the interesting innovations are: 

* They do an *ASR-level* cloze task instead of a *text-level* cloze task like BERT does.
* They demonstrate zero-shot E2E prediction
* They produce a zero-shot E2E benchmark on the Facebook TOP dataset.

### The model

They take LFBE features as audio input. They embed them using a CNN-based embedder followed by a transformer encoder. They embed and encode input text using BERT. They then train a single transformer decoder to transcribe both into output text. I *think* the output text is just an in-place slot-labeled text sequence. (I.e., "alexa, play despacito on spotify" -> "SONG_PLAY TITLE_START despacito TITLE_END SERVICE_START spotify SERVICE_END")


### Zero-shot

Their "zero-shot" formulation involves using only sample SLU data to bootstrap an audio->text encoder decoder to do audio->interpretation. I prefer this a lot to the previous preferred approach, which they reference in the section, of producing augmented E2E speech data using a synthesizer.


### Experiments

For internal, they focus on a music domain-only SLU dataset. There are limiting inductive biases to focusing on just one domain, I think, but regardless the results they're able to get are still interesting. They perform ablations with synthetic audio and in the zero-shot domain.


## Thoughts

They achieve SOTA on FSC (nearly 100%, also no longer SOTA but everyone is beating 99% these days). I appreciate the idea of zero-shot E2E benchmarking. We touch on this in our upcoming Interspeech 2021 paper. I think outputting in-place slot encoded text is the only alternative to the multistage approach in our upcoming Interspeech paper. I'd be interested in seeing a head-to-head comparison.


## Further Reading

1. TODO: add our Interspeech 2021 paper here once it's on arxiv