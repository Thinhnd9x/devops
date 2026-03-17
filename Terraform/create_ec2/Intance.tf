resource "aws_instance" "webserver" {
  ami                    = data.aws_ami.amiID.id
  instance_type          = "t2.micro"
  key_name               = "key_ec2"
  vpc_security_group_ids = [aws_security_group.terra-sg.id]
  availability_zone      = "ap-southeast-1a"

  tags = {
    Name    = "terrainstance"
    Project = "terraform"
  }
}
/* resource "aws_ec2_instance_state" "state_ec2" {
  instance_id =  aws_instance.webserver.id
  state = "running" //Check state instance
} */