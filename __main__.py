import os
import pulumi
import pulumi_aws as aws
import pulumi_eks as eks

cluster = eks.Cluster(
    "example",
    vpc_id="doesntmatter",
    skip_default_node_group=True,
    provider_credential_opts=eks.KubeconfigOptionsArgs(
        profile_name=os.environ.get("AWS_PROFILE"),
    ),
)

aws.eks.NodeGroup(
    "example",
    cluster_name="example",
    instance_types=["t3.micro"],
    node_role_arn=cluster.instance_roles[0].arn,
    subnet_ids=["doesntmatter"],
    scaling_config=aws.eks.NodeGroupScalingConfigArgs(
        desired_size=1,
        max_size=1,
        min_size=1,
    ),
    opts=pulumi.ResourceOptions(
        # Comment out the following line to make preview work.
        parent=cluster,
    ),
)
