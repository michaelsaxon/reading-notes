# Don’t Stop Pretraining: Adapt Language Models to Domains and Tasks
Authors: **Suchin Gururangan, Ana Marasović, Swabha Swayamdipta, Kyle Lo, Iz Beltagy, Doug Downey, Noah A. Smith**

Venue: *ACL 2020*

Link: [ACL Anthology](https://www.aclweb.org/anthology/2020.acl-main.740/)

Topics: 

## Summary

The key question is this: do language model pretraining strategies do what we think they're doing? Do they actually work? And are they truly generalized, or does domain-specific pretraining help? Their focus is on RoBERTa. They consider four domains (biomed, CS pubs, news, and reviews) and 2 classification tasks in each domain.

Key insights in intro: "domain-adaptive" pretraining is critical for targets that are not in-domain for RoBERTa. They constrast this with "task-adaptive" pretraining on task-relevant corpora. They find that task-adaptive training (i.e., ULMFiT), which has been abandoned in more recent work, still drives big gains on RoBERTa. Finally, they find manual curation of unlabeled data in the task distribution helps improve the benefits of TAPT.

### DAPT

**They quantify similarity between domains** using vocabulary overlap (in pct) between them. Clear motivation of the obvious distributional differences between the domains. I.e., News is close to the pre-training distribution, and to reviews, CS closer to biomed than anything else, etc.

Interestingly, they find not only that DAPT improves performance across the domains (やっぱり) but also that **further pre-training using text from a different domain makes the final performance worse than RoBERTa alone.**

They motivate overlap between domains well by highlighting documents from two domains (i.e., a movie review and a news article about movies) where *n*-grams and/or words overlap. This illustrates well that maybe closer domains are better for pretraining than farther apart domains. Indeed, they also demonstrate this empirically by showing that **the reduction in performance under incorrect domain DAPT is less for further apart domains than closer ones**.

### TAPT

TAPT focuses on *specifically pretraining on the training corpus for your task* to get a contextual model of language in the core area of interest. One issue with this is the available data is much smaller. They pretrain for 100 epochs of TAPT and wring as much value out of the available data via "augmenting" by masking different words with a high masking probability.

They find that TAPT also improves over vanilla RoBERTa, and that DAPT+TAPT tends to outperform the cobination of the two, with one exception.


## Thoughts

This is very interesting work, and directly relevant to several of my interests such as NLI. I can definitely see myself citing this one in the future.