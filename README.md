What is Basel II?

Basel Committee on Banking Supervision developed Basel II, an international banking regulation framework designed to improve how banks manage financial risk.
The framework helps banks ensure they have enough capital to cover risks such as:
-Credit risk
-Operational risk
-Market risk
-Basel II mainly focuses on:
-Proper risk measurement
-Model transparency
-Documentation
-Continuous monitoring
-Explainability of decisions
For credit risk modeling, Basel II requires banks to use reliable and understandable methods when deciding whether customers are risky or eligible for loans.
Why Interpretability Matters

**In financial institutions, models cannot only provide predictions — they must also provide explanations.

Banks must be able to explain:

-Why a loan application was rejected
-Why a customer is considered risky
-Which features influenced the prediction

Examples of influential features may include:

Transaction frequency
Account activity
Purchase behavior
Customer engagement
Payment patterns

Because of these requirements:

Pure black-box models are risky in regulated environments
Documentation is mandatory
Decisions must be auditable and explainable to regulators

This is why interpretable machine learning models are highly valued in banking systems.
Why a Proxy Variable Was Needed

The dataset used in this project did not contain a direct default column indicating whether customers failed to repay loans.

Therefore, a proxy target variable had to be created.

To estimate customer risk behavior, the project used:

Customer transaction behavior
Transaction engagement patterns
RFM Analysis
What is RFM Analysis?

RFM stands for:

Recency → How recently the customer made a transaction
Frequency → How often the customer transacts
Monetary → How much money the customer spends or transfers

Customers with poor engagement patterns may indicate higher financial risk.

Using these behavioral indicators, customers were grouped into likely low-risk and high-risk categories to create a proxy default label.
Business Risks of Using a Proxy Variable

Although proxy variables help when true default data is unavailable, they introduce important business and regulatory risks.

Key risks include:

1. Proxy Does Not Equal Real Default

The generated target is only an estimate and may not perfectly represent actual loan default behavior.

2. Possible Bias

Behavioral assumptions may unintentionally favor or disadvantage certain customer groups.

3. Customer Misclassification

Some good customers may be classified as risky, while risky customers may appear safe.

4. Unfair Loan Decisions

Incorrect classifications can lead to unfair loan approvals or rejections.

5. Regulatory Concerns

Financial regulators expect fairness, transparency, and accountability in credit decisions. Weak proxy definitions may create compliance risks.

Because of these concerns, proxy-based credit models require careful monitoring, validation, and documentation.
| Logistic Regression          | Gradient Boosting       |
| ---------------------------- | ----------------------- |
| Interpretable                | Higher accuracy         |
| Easy to explain              | Hard to explain         |
| Basel-friendly               | Complex                 |
| Stable                       | Powerful                |
| Lower predictive performance | Better predictive power |
Comparison Discussion
Logistic Regression

Logistic Regression is widely used in banking because it is simple, transparent, and easy to interpret.

Advantages:

Easy to explain to regulators
Coefficients show feature impact clearly
Stable and well-understood
Strong governance compatibility

Disadvantages:

May not capture complex nonlinear relationships
Usually lower predictive performance compared to advanced ensemble methods
Gradient Boosting

Gradient Boosting is a powerful ensemble learning technique that often achieves higher prediction accuracy.

Advantages:

Strong predictive power
Captures complex feature interactions
Performs well on structured financial data

Disadvantages:

Harder to interpret
More difficult to explain to regulators
Requires additional explainability tools such as SHAP values
Final Conclusion

In regulated financial environments, model performance alone is not sufficient.

Banks must ensure that models are transparent, explainable, stable, and properly documented to comply with Basel II requirements.

Therefore:

In regulated finance, interpretability and governance are often as important as predictive performance.