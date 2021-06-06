# Limitations of Autoregressive Models and Their Alternatives
Authors: **Chu-Cheng Lin, Aaron Jaech, Xin Li, Matthew R. Gormley, Jason Eisner**
Venue: *NAACL 2021*
Link: [arXiv](https://arxiv.org/abs/2010.11939v2)
Topics: theoretical CS, NLP, language models, autoregressive, proofs

## Summary

The authors present a problem with autoregressive LMs: their use of polynomial-time computation to pick/assess the probability of the next symbol means that they have provable limitations on the kinds of distributions. In the abstract they immediately present the implications: you can't just generally solve NLP with ever-larger, ever-data-hungrier autoregressive LMs.

In more precise terms, the problem is as follows: computing unnormalized string probabilities individually is easy, but computing or estimating the autoregressive factors that compose the stringwise probability individually is NP-hard. To do this they introduce two classes of models, ECCP and ELNCP.

Defining an RNN or general recursive language model as a Turing machine that produces Turing machines from some set of parameter vectors. This set of parameter vectors is "efficiently computable with compact parameters" (ECCP) if their size, time-to-construct-machine, and probability scoring time for any input vector x all grows as O(poly(n)). They ask not if those parameter vectors are **learnable**, just if some such set of parameters exists. 

Furthermore, they introduce ELNCP models, which are "efficiently locally normalizable with compact parameters." In other words, have compact parameters and can efficiently assess the sequence of conditional probabilities for the sequence of prefixing sequences that make up a sentence. They demonstrate how autoregressive LMs are ELNCP.

They then show that there exist weighted languages that are ECCP but not ELNCP. This means that some language problems for which the computation of p over a whole sentence is easy, but computing the sequence of conditional probabilities is NP-hard. This is effectively a **capacity problem** for autoregressive LMs.

They then present classes of models that do not have these problems, trading in efficiency or compactness to achieve capacity. These include Energy-based and Latent variable models. However, there are tradeoffs. In particular, I want to read Further Reading paper [1.](https://jmlr.org/papers/v22/20-326.html) to learn more about ways that globally normalized EBMs can be infused with locally normalized inductive biases to overcome the worse performance of the empirical results the authors got on RNN and Transformer EBMs as opposed to MLE models.

## Thoughts

The Knapsack problem XKCD comic inclusion as [Figure 1](https://xkcd.com/287/) was both funny and useful as an example for understanding the key issue at stake in this paper.

There is a lot of dense front-loading of definitions in section 2. I ended up skipping it, reading the rest of the paper, and then going back.

Overall, this paper is definitely beyond my current Mathy-Theoretical-CS-level, or at least, my current able-to-quickly-read-mathy-theoretical-CS-papers-level (pls forgive me I studied EE in undergrad). I'm not in a position to confidently judge the quality or correctness of some of the arguments in here without putting a lot of time in. I will probably revisit this with more depth in the future, especially if some of the problems they raise become more relevant to my own work.

My familiarity with language processing models is heavily biased towards neural architectures employing autoregressive decoders. I want to familiarize myself with EBMs and LVMs thanks to the points raised here.

## Further Reading

1. Residual Energy-Based Models for Text, A. Bakhtin, Y. Deng, S. Gross, M. Ott, M.A. Ranzato, A. Szlam, [JMLR](https://jmlr.org/papers/v22/20-326.html)