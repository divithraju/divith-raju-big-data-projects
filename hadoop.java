cd /home/divithraju/Downloads/hadoop-3.3.6
sbin/start-all.sh
hdfs dfs -ls /
hdfs dfs -mv /tcs /tata
hdfs dfs -put /home/divithraju/Downloads/data  /sales
hdfs dfs -rm -r /sales
hdfs dfs -mkdir /ty
hdfs dfs -ls -R /
hdfs dfs -get /tcs /home/divithraju/pictures
hdfs dfs -mkdir -p /ty
hdfs dfs -rmdir /ty
hdfs dfs -cat /sales
hdfs dfs -head /sales
hdfs dfs -tail /sales
hdfs dfs -du /sales
hdfs dfs -du -h /sales
hdfs fsck /divithraju/hadoop
hdfs dfs -chmod 777 /sales
hdfs dfs -chmod 755 /sales
hdfs dfs -chmod 644 /sales
hdfs dfs -chmod 700 /sales
hdfs dfs -chmod 600 /sales
hdfs dfs -chmod 555 /sales
hdfs dfs -count /sales
hdfs dfs -checksum /sales
hdfs dfs -touchz /ft
hdfs dfs -getmerge /tcs /sales
hdfs dfsadmin -report
hdfs fsck /sales
hdfs fsck /sales -delete
hdfs dfs -chown pond /sales




