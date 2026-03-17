resource "aws_instance" "webserver" {
  ami                    = var.amiID[var.region]
  instance_type          = "t2.micro"
  key_name               = "key_ec2"
  vpc_security_group_ids = [aws_security_group.terra-sg.id]
  availability_zone      = var.zone

  tags = {
    Name    = "terrainstance"
    Project = "terraform"
  }
  /* provisioner "file"{ //put file and setup webapp
    source = "web.sh"
    destination = "/tmp/web.sh"
  }
  connection {
    type = "ssh"
    user = var.user
    private_key = file("ec2_key")
    host = self.public_ip
  }
  provisioner "remote-exec" {
    inline = [ 
      "chmod +x /tmp/web.sh",
      "sudo /tmp/web.sh"
     ]
  } */
  
}
/* resource "aws_ec2_instance_state" "state_ec2" {
  instance_id =  aws_instance.webserver.id
  state = "running" //Check state instance
} */