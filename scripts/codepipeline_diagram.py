from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.storage import S3
from diagrams.aws.security import IAM
from diagrams.aws.network import VPC

with Diagram("AWS CodePipeline Infrastructure", show=False):
    with Cluster("VPC"):
        ec2 = EC2("EC2 Instance")

    codecommit = Codecommit("CodeCommit\nRepository")
    
    with Cluster("CodePipeline"):
        pipeline = Codepipeline("Pipeline")
        
        with Cluster("Stages"):
            source = Codecommit("Source")
            deploy = Codedeploy("Deploy")
            test = Codebuild("Acceptance\nTest")
        
        pipeline >> source >> deploy >> test

    s3 = S3("Artifact Store")
    
    iam_role = IAM("IAM Roles")

    codecommit >> pipeline
    pipeline >> s3
    pipeline >> ec2
    iam_role - pipeline
    iam_role - ec2
