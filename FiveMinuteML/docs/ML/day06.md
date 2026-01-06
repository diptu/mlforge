---
title: Parametric vs Non-Parametric Models
sidebar_position: 6
---

:::tip 🌟 Day 06 Highlight
**Parametric vs Non-Parametric Models**  
Understand how assumptions about data shape **model flexibility, scalability, and performance**.
:::

## 📚 Table of Contents
- [Overview](#overview)
- [What are Parametric Models?](#what-are-parametric-models)
- [What are Non-Parametric Models?](#what-are-non-parametric-models)
- [Key Differences](#key-differences)
- [Bias–Variance Perspective](#biasvariance-perspective)
- [System Design Considerations](#system-design-considerations)
- [Key Takeaways](#key-takeaways)
- [Quick Summary](#quick-summary)
- [References](#references)

---

## Overview

Another powerful way to categorize Machine Learning models is based on **how many assumptions they make about data**.

- **Parametric Models** → Fixed number of parameters  
- **Non-Parametric Models** → Flexible number of parameters  

This distinction directly impacts **generalization, data requirements, interpretability, and scalability**.

---

## What are Parametric Models?

Parametric models assume a **specific functional form** for the data and summarize learning using a **fixed set of parameters**, regardless of dataset size.

### Key Characteristics
- Fixed number of parameters
- Strong assumptions about data distribution
- Faster training and inference
- Easier to interpret
- Performs well with limited data

### Common Examples
- Linear Regression
- Logistic Regression
- Naive Bayes
- Linear SVM

### Intuition
> “I assume the data follows a known pattern — I just need to learn the parameters.”

---

## What are Non-Parametric Models?

Non-parametric models make **fewer assumptions** and allow model complexity to **grow with data**.

### Key Characteristics
- Flexible number of parameters
- Minimal assumptions about data
- Captures complex patterns
- Requires more data
- Higher computational cost

### Common Examples
- k-Nearest Neighbors (k-NN)
- Decision Trees
- Random Forests
- Kernel SVMs

### Intuition
> “I’ll adapt my structure based on what the data looks like.”

---

## Key Differences

| Aspect | Parametric Models | Non-Parametric Models |
|-----|------------------|----------------------|
| Parameters | Fixed | Grows with data |
| Assumptions | Strong | Weak |
| Flexibility | Low | High |
| Data Need | Low–Medium | High |
| Interpretability | High | Lower |
| Compute Cost | Low | High |

---

## Bias–Variance Perspective

- **Parametric Models**
  - Higher bias
  - Lower variance
  - Risk of underfitting

- **Non-Parametric Models**
  - Lower bias
  - Higher variance
  - Risk of overfitting

This makes the choice **context-dependent**, not “one is better than the other.”

---

## System Design Considerations

Choose **Parametric Models** when:
- Data is limited
- Interpretability is important
- Low-latency inference is required
- Simpler deployment is preferred

Choose **Non-Parametric Models** when:
- Data is abundant
- Relationships are complex
- Accuracy is prioritized over interpretability
- Compute resources are available

---

## Key Takeaways

- Parametric models trade flexibility for simplicity and speed
- Non-parametric models trade efficiency for expressive power
- The decision affects **cost, latency, accuracy, and maintainability**
- Real-world ML systems often start parametric, then evolve

---

## Quick Summary

:::info ⏱️ 5-Minute Recap
- **What you learned:**  
  How parametric and non-parametric models differ in assumptions and flexibility

- **Why it matters:**  
  This choice impacts bias–variance tradeoff, scalability, and production readiness

- **What’s next:**  
  **Bias–Variance Tradeoff** — the core principle behind model selection
:::

---

## References

- Stanford CS229 — *Model Complexity & Generalization*  
- Géron, A. — *Hands-On Machine Learning*  
- IBM — *Parametric vs Non-Parametric Models*
