
port=2222
path=`pwd -P`
period=2000
first_time=2
scheme='cubic'
id=0
down='wired12'
up='wired12'
latency=20
finish_time=50
qsize=50
max_it=1


log="orca-$scheme-$down-$up-$latency-${period}-$qsize"




echo "$path/orca-server-mahimahi $port $path ${period} ${first_time} $scheme $id $down $up $latency $log $finish_time $qsize $max_it"

$path/orca-server-mahimahi $port $path ${period} ${first_time} $scheme $id $down $up $latency $log $finish_time $qsize $max_it >a.txt
