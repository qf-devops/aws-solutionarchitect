aws ec2 run-instances --image-id ami-0ded8326293d3201b --count 1 --instance-type t2.micro --key-name mumbai --security-group-ids sg-0fbebfd9572febce5 --subnet-id subnet-e58fafa9

aws ec2 describe-instances --filters "Name=instance-type,Values=t2.micro" --query "Reservations[].Instances[].InstanceId"

 aws ec2 terminate-instances --instance-ids i-0da5673fa8a38684e