sudo apt update -y
sudo apt install openjdk-11-jdk
echo "Updating system packages..."
sudo apt install tmux
echo "Installing Python and pip..."
sudo apt install python3 python3-pip -y



pip3 install -r requirements.txt
#cd dku_kafka

curl -O https://dlcdn.apache.org/kafka/3.9.0/kafka_2.13-3.9.0.tgz

tar -xvzf kafka_2.13-3.9.0.tgz

cd kafka_2.13-3.9.0

echo "kafka 실행중"

tmux new-session -d -s kafka-server  
tmux new-session -d -s zookeeper    

tmux send-keys -t zookeeper "cd ./dku_kafka/kafka_2.13-3.9.0" C-m
tmux send-keys -t zookeeper "bin/zookeeper-server-start.sh config/zookeeper.properties" C-m

tmux send-keys -t kafka-server "cd ./dku_kafka/kafka_2.13-3.9.0" C-m
tmux send-keys -t kafka-server "bin/kafka-server-start.sh config/server.properties" C-m
sleep 5

# cd ./dku_kafka
# cd kafka_2.13-3.9.0

# bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092
cd ..

tmux new-session -d -s kafka 

tmux split-window -h
tmux select-pane -t 0
tmux split-window -v
tmux select-pane -t 2
tmux split-window -v
tmux split-window -v

tmux select-pane -t 2
tmux send-keys "python3 consumer_order.py" C-m

tmux select-pane -t 3
tmux send-keys "python3 consumer_inventory.py" C-m

tmux select-pane -t 4
tmux send-keys "python3 consumer_payment.py" C-m

tmux select-pane -t 0
tmux send-keys "python3 producer_1.py" C-m
tmux select-pane -t 1
tmux send-keys "python3 producer_2.py" C-m

tmux attach -t kafka
