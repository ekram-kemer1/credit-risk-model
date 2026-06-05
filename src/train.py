import mlflow

mlflow.start_run()

mlflow.log_param("model", "logistic_regression")
mlflow.log_metric("accuracy", 0.85)

mlflow.end_run()