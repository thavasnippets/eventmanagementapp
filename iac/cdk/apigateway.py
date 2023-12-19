from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_s3 as s3,
    core
)


class LambdaApiGatewayStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a Lambda layer
        layer = _lambda.LayerVersion(
            self, "MyLambdaLayer",
            code=_lambda.Code.from_asset("path/to/your/layer/code"),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_8],
            description="My Lambda Layer"
        )

        # Create a Lambda function
        lambda_function = _lambda.Function(
            self, "MyLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("path/to/your/lambda/code"),
            layers=[layer],
            environment={
                "LAYER_ENV_VAR": "value"  # Add any environment variables you need
            }
        )

        # Create an API Gateway
        api = apigateway.RestApi(
            self, "MyApiGateway",
            default_cors_preflight_options={
                "allow_origins": apigateway.Cors.ALL_ORIGINS,
                "allow_methods": apigateway.Cors.ALL_METHODS
            }
        )

        # Create a Lambda integration for the API Gateway
        integration = apigateway.LambdaIntegration(lambda_function, proxy=True)

        # Add a proxy resource and associate the Lambda integration
        api.root.add_resource("{proxy+}").add_method("ANY", integration)


app = core.App()
LambdaApiGatewayStack(app, "LambdaApiGatewayStack")
app.synth()
