from aws_cdk import core
from aws_cdk import aws_ec2 as ec2

class MyEc2InstanceStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Look up the default VPC
        vpc = ec2.Vpc.from_lookup(self, "VPC", is_default=True)

        # Define the EC2 instance using an Amazon Linux 2 AMI
        ec2.Instance(self, "MyInstance",
                     instance_type=ec2.InstanceType("t3.micro"),
           machine_image=ec2.MachineImage.latest_amazon_linux(),
                     vpc=vpc)
app = core.App()
MyEc2InstanceStack(app, "MyEc2InstanceStack")
app.synth()