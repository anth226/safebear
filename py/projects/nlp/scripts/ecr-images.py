"""
Huggingface x Tensorflow
AWS SageMaker ECR Images

https://docs.aws.amazon.com/sagemaker/latest/dg/ecr-eu-west-3.html#huggingface-eu-west-3.title
https://sagemaker.readthedocs.io/en/stable/api/utility/image_uris.html
"""
import sagemaker.serverless
from sagemaker import image_uris

HUGGINGFACE_VERSION = "4.17.0"
TENSORFLOW_VERSION = "2.6.3"

training_image = image_uris.retrieve(
    framework="huggingface",
    region="eu-west-3",
    image_scope="training",
    base_framework_version=f"tensorflow{TENSORFLOW_VERSION}",
    version=HUGGINGFACE_VERSION,
)

print(training_image)

inference_image = image_uris.retrieve(
    framework="huggingface",
    region="eu-west-3",
    image_scope="inference",
    base_framework_version=f"tensorflow{TENSORFLOW_VERSION}",
    version=HUGGINGFACE_VERSION,
    serverless_inference_config=sagemaker.serverless.ServerlessInferenceConfig(),
)

print(inference_image)
