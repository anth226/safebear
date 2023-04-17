import pulumi
import pulumi_aws as aws

aws_config = pulumi.Config("aws")
region = aws_config.require("region")

SERVICE = "inference"
NAME_TEMPLATE = f"{pulumi.get_project()}-{SERVICE}-{pulumi.get_stack()}"

# Create a bucket for the trained models
models_bucket = aws.s3.BucketV2(
    resource_name="models",
    bucket=f"{pulumi.get_project()}-models-{pulumi.get_stack()}-{region}",
)
aws.s3.BucketAclV2(
    resource_name="models",
    bucket=models_bucket.id,
    acl="private",
    opts=pulumi.ResourceOptions(parent=models_bucket),
)

trained_model_object = aws.s3.BucketObject(
    resource_name="my-bert-model",
    bucket=models_bucket.id,
    key="my-bert-model/model.tar.gz",
    source=pulumi.StringAsset("foo"),
    storage_class="STANDARD",
    opts=pulumi.ResourceOptions(parent=models_bucket),
)

# Create an IAM role for SageMaker to use
execution_role = aws.iam.Role(
    resource_name=SERVICE,
    name=NAME_TEMPLATE,
    assume_role_policy=aws.iam.get_policy_document(
        statements=[
            aws.iam.GetPolicyDocumentStatementArgs(
                actions=["sts:AssumeRole"],
                principals=[
                    aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                        identifiers=["sagemaker.amazonaws.com"],
                        type="Service",
                    )
                ],
            )
        ]
    ).json,
    inline_policies=[
        aws.iam.RoleInlinePolicyArgs(
            name="sagemaker",
            policy=aws.iam.get_policy_document(
                statements=[
                    aws.iam.GetPolicyDocumentStatementArgs(
                        actions=["s3:GetObject"],
                        resources=[
                            pulumi.Output.concat(
                                models_bucket.arn, "/", trained_model_object.key
                            )  # type: ignore
                        ],
                    ),
                ]
            ).json,
        )
    ],
)

model = aws.sagemaker.Model(
    resource_name=SERVICE,
    name=NAME_TEMPLATE,
    execution_role_arn=execution_role.arn,
    primary_container=aws.sagemaker.ModelPrimaryContainerArgs(
        image=aws.sagemaker.get_prebuilt_ecr_image(
            repository_name="huggingface-tensorflow-inference",
            image_tag="2.6.3-transformers4.17.0-cpu-py38-ubuntu20.04",
        ).registry_path,
        model_data_url=pulumi.Output.concat(
            "s3://", trained_model_object.bucket, "/", trained_model_object.key
        ),
    ),
    opts=pulumi.ResourceOptions(parent=trained_model_object),
)

endpoint_config = aws.sagemaker.EndpointConfiguration(
    resource_name=SERVICE,
    name=NAME_TEMPLATE,
    production_variants=[
        aws.sagemaker.EndpointConfigurationProductionVariantArgs(
            variant_name=pulumi.get_stack(),
            model_name=model.name,
            serverless_config=aws.sagemaker.EndpointConfigurationProductionVariantServerlessConfigArgs(
                memory_size_in_mb=1024,
                max_concurrency=1,
            ),
        )
    ],
    opts=pulumi.ResourceOptions(parent=model),
)

# aws.sagemaker.Endpoint(
#     resource_name=SERVICE,
#     name=NAME_TEMPLATE,
#     endpoint_config_name=endpoint_config.name,
#     opts=pulumi.ResourceOptions(parent=endpoint_config),
# )
