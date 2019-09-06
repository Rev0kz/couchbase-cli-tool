import click
import subprocess

host=" "
username=" "  
password=" "  
bucketname=" "  
buckektype=" "
bucketsize=" "


@click.command()
@click.argument('host')   
@click.argument('username')
@click.argument('password')
@click.argument('bucketname')
@click.argument('bucketype')
@click.argument('bucketsize')


def CreateBucket(host, username, password, bucketname, bucketype, bucketsize):
    """
    This command connects to a couchbase cluster and creates a couchbase bucket. Specify the host in the following format: http://<ipaddress>:8080
    
    You need to supply the following arguments accordingly: username password bucketname bucketype bucketsize

    for example: python couchtoolp.py admin token userdata couchbase 1024

    """  

    subprocess.call("couchbase-cli bucket-create -c host -u username -p password --bucket bucketname --bucket-type bucketype --bucket-ramsize bucketsize", shell=True) 


if __name__  == "__main__":  
     CreateBucket()

