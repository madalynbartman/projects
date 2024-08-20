read -p "Enter the user id of the account you want to remove: " name

USER=$(whoami)
ip_a=X.X.X.X
ip_co=X.X.X.X
ip_ct=X.X.X.X
ip_m=X.X.X.X
# Get users
# curl -k -u elastic:PASSWORD --cacert /home/USER/ansible/elasticsearch-ca.pem -XGET https://IPADDR:9200/_security/user/

# Disable elastic user on each cluster
echo "Removing elastic user on each cluster.."
echo "############################"
echo "#          Audit           #"
echo "############################"
curl -k -u elastic:password1 --cacert /home/$USER/ansible/elasticsearch-ca.pem -XPUT https://$ip_a:9200/_security/user/$name/_disable?pretty | jq
echo "############################"
echo "#          Cyber 1         #"
echo "############################"
curl -k -u elastic:password2 --cacert /home/$USER/ansible/elasticsearch-ca.pem -XPUT https://$ip_co:9200/_security/user/$name/_disable?pretty | jq
echo "############################"
echo "#          Cyber 2         #"
echo "############################"
curl -k -u elastic:password3 --cacert /home/$USER/ansible/elasticsearch-ca.pem -XPUT https://$ip_ct:9200/_security/user/$name/_disable?pretty | jq
echo "############################"
echo "#          Monitoring      #"
echo "############################"
curl -k -u elastic:password4 --cacert /home/$USER/ansible/elasticsearch-ca.pem -XPUT https://$ip_m:9200/_security/user/$name/_disable?pretty | jq
echo "Done!"

# Disabling home directory on bastion
echo "Disabling home directory on bastion.."
set -x
i=IP2
cmd="mv /home/$name/ /home/hide-$name/";
pem="/home/maintuser/bin/ncave-internal.pem";
user="maintuser";
timeout 20 ssh -o "StrictHostKeyChecking no" -i $pem $user@$i sudo -- $cmd;
set +x
echo "Done!"
