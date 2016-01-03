
# open a local ssh tunnel to remote ssh connection
ssh -i YuchenAWSEC2.pem.txt -N -L 3307:ec2-54-178-201-20.ap-northeast-1.compute.amazonaws.com:3306 ubuntu@ec2-54-178-201-20.ap-northeast-1.compute.amazonaws.com

# ssh to remote aws ec2
ssh -i YuchenAWSEC2.pem.txt ubuntu@ec2-54-178-201-20.ap-northeast-1.compute.amazonaws.com

# check ssh tunnel is open
lsof -i tcp:3307

#kill not close ssh tunnel 
kill -9 <PID>