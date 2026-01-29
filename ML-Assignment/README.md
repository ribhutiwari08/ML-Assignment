# ML Engineer Practical Assessment

## Dataset
Breast Cancer Dataset from scikit-learn.

## Task 1: Production ML Pipeline
- Data loading & validation
- Feature engineering (4 engineered features)
- RandomForest model selection
- Cross-validation
- Evaluation metrics
- Model persistence
- Reproducibility with random seeds
- Modular production-style code

## Task 2: Model Debugging & Stability
### Issues Observed
- High variance across runs
- Prediction instability

### Root Causes
- Randomness in model training
- No cross-validation
- Single train-test split dependency

### Fixes Implemented
- Fixed random_state everywhere
- Added cross-validation

### Before vs After
| Version | Accuracy |
|------|------|
| Before | ~0.90 |
| After | ~0.96 |

## Task 3: Performance Improvement
- Feature engineering
- Hyperparameter tuning
- Improved accuracy by more than 10%

## Task 4: ML System Design (Fraud Detection)
### Components
- Data ingestion via API
- Feature store
- Model training pipeline
- Real-time inference
- Monitoring & drift detection
- Scheduled retraining

