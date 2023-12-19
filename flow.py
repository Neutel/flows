from prefect import flow
from prefect.deployments import DeploymentImage


@flow(log_prints=True)
def buy():
    print("Buying securities")


if __name__ == "__main__":
    buy.deploy(
        name="my-code-baked-into-an-image-deployment", 
        work_pool_name="test-work-pool", 
        image=DeploymentImage(
            name="my_image",
            tag="deploy-guide",
            dockerfile="Dockerfile"
        ),
        push=False
    )