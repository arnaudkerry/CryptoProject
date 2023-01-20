#!\bin\bash

if [ $# -ne 2 ];
then
	echo "2 arguments required missing : nbKey keySize"
	exit 0
fi

if [ $2 != "256" -a $2 != "512" -a $2 != "1024" -a $2 != "2048"] 
then
	echo "Error in keySize"
	exit 0
fi

rm -rf keys
mkdir keys
for i in $(seq 1 $1)
do {
	filetmp='keys/key'$i'.key.tmp'
	file='keys/key'$i'.key'
	openssl genrsa $2 > $filetmp
	sed '/^-----BEGIN PRIVATE KEY-----/d;/^-----END PRIVATE KEY-----/d' $filetmp > $file 2>/dev/null
	rm $filetmp
}& done
wait
echo "TIME : $SECONDS seconds"
