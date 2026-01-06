---
title: Bias–Variance Tradeoff
sidebar_position: 7
---

:::tip 🌟 Day 07 Highlight
**Bias–Variance Tradeoff**  
The core principle behind **why models underfit, overfit, or generalize well**.
:::

## 📚 Table of Contents
- [Overview](#overview)
- [What is Bias?](#what-is-bias)
- [What is Variance?](#what-is-variance)
- [The Bias–Variance Tradeoff](#the-biasvariance-tradeoff)
- [Underfitting vs Overfitting](#underfitting-vs-overfitting)
- [How to Manage the Tradeoff](#how-to-manage-the-tradeoff)
- [System Design Perspective](#system-design-perspective)
- [Key Takeaways](#key-takeaways)
- [Quick Summary](#quick-summary)
- [References](#references)

---

## Overview

One of the most important ideas in Machine Learning is the **Bias–Variance Tradeoff** — a framework that explains **why models fail to generalize**.

Every ML model makes errors due to:
- **Bias** → error from overly simple assumptions
- **Variance** → error from excessive sensitivity to training data

The goal is to find the **sweet spot** between the two.

---

## What is Bias?

**Bias** refers to errors introduced by **oversimplifying assumptions** in the learning algorithm.

### Characteristics of High Bias
- Model is too simple
- Misses important patterns
- Performs poorly on both training and test data
- Leads to **underfitting**

### Examples
- Linear regression on highly non-linear data
- Shallow decision trees

> Intuition: *“My model is too simple to capture reality.”*

---

## What is Variance?

**Variance** refers to errors caused by a model being **too sensitive to training data**.

### Characteristics of High Variance
- Model is overly complex
- Fits noise instead of signal
- Excellent training performance
- Poor generalization to new data
- Leads to **overfitting**

### Examples
- Very deep decision trees
- k-NN with very small k

> Intuition: *“My model memorized the data instead of learning.”*

---

## The Bias–Variance Tradeoff

As model complexity increases:
- **Bias decreases**
- **Variance increases**

As model complexity decreases:
- **Bias increases**
- **Variance decreases**

There is **no free lunch** — improving one often worsens the other.

---

## Underfitting vs Overfitting

| Scenario | Bias | Variance | Outcome |
|-------|------|----------|--------|
| Underfitting | High | Low | Poor training & test performance |
| Overfitting | Low | High | Poor test performance |
| Good Fit | Balanced | Balanced | Strong generalization |

---

## How to Manage the Tradeoff

### Reduce High Bias
- Use more complex models
- Add relevant features
- Reduce regularization
- Train longer

### Reduce High Variance
- Collect more data
- Simplify the model
- Increase regularization
- Use ensembling (bagging)

---

## System Design Perspective

In real-world ML systems:

- **High-bias models**  
  → Easier to deploy, faster, more interpretable

- **High-variance models**  
  → Higher accuracy but harder to scale and maintain

System design choices (latency, cost, interpretability) often determine **where you sit on the tradeoff curve**.

---

## Key Takeaways

- Bias and variance are two sources of model error
- Underfitting = high bias
- Overfitting = high variance
- Good models balance both
- This tradeoff drives most ML design decisions

---

## Quick Summary

:::info ⏱️ 5-Minute Recap
- **What you learned:**  
  Why ML models underfit, overfit, or generalize well

- **Why it matters:**  
  The bias–variance tradeoff guides model selection, tuning, and system design

- **What’s next:**  
  **Overfitting vs Underfitting (with visuals & metrics)**
:::

---

## References

- Stanford CS229 — *Bias–Variance Tradeoff*  
- Andrew Ng — *Machine Learning Lectures*  
- Géron, A. — *Hands-On Machine Learning*
