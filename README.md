As i have faced issue with seprating dataset i have removed all the "" from the both the dataset it is adviced to remoce them from your side to succesfully run the program

# Name: Jalaj Sharma
# UCID : js2475
#github link: https://github.com/jalajsharma93/cloudcomputingproject2
#docker link : https://hub.docker.com/u/jalajsharma93

# cloudcomputingproject2

We have several steps to follow which includes sub commands also
	a)Set up EMR with 3 slave and 1 Master --- Required by professor
	b)uploads all the file to EMR 
	c)Install python, pyspark, docker with all dependencies required to run pyspark
	d)Create dokerFile, start docker, build, run and push to dockehub


## Setting up EMR cluster
	please check document with extention.pdf or word dockehub
	#copy file to cluster
	Scp -i A.key * hadopp@<address from ec2 instance connect> :/home/hadoop/
	Scp -i <key.pem with path> <directory or file with path> hadopp@<address from ec2 instance connect> :/home/Hadoop/
	
	#Connect to EMR cluster
	ssh -i A.key hadoop@<address from ec2 instance>
	
## Installing python
	sudo pip install --upgrade pip
	sudo apt install python3-pip
	#installing pyspark, docker and dependencies 
	sudo pip install --upgrade pip
	sudo pip install wheel
	sudo pip install pyspark --no-cache-dir
	sudo pip install findspark
	sudo pip install numpy
	sudo yum install -y docker

## sudo service docker start
sudo docker build . -f Dockerfile -t jalajsharma93/cloudcomputingpa2
sudo docker run -t jalajsharma93/cloudcomputingpa2

##for Pushing file to docker
	sudo docker login -u <user_name>
	<type password it will ask for it>
	sudo docker push



	
	

	
