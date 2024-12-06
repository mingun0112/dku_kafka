sudo apt update
sudo apt install openjdk-11-jdk


# curl -O https://dlcdn.apache.org/kafka/3.9.0/kafka_2.13-3.9.0.tgz

# tar -xvzf kafka_2.13-3.9.0.tgz

# cd kafka_2.13-3.9.0


# tmux 세션 생성
tmux new-session -d -s kafka-server  # Kafka 서버를 위한 세션
tmux new-session -d -s zookeeper    # Zookeeper 서버를 위한 세션

# Zookeeper 서버 실행 (zookeeper-server-start.sh)
tmux send-keys -t zookeeper "cd ./dku_kafka/kafka_2.13-3.9.0" C-m
tmux send-keys -t zookeeper "bin/zookeeper-server-start.sh config/zookeeper.properties" C-m
# Kafka 서버 실행 (kafka-server-start.sh)
tmux send-keys -t kafka-server "cd ./dku_kafka/kafka_2.13-3.9.0" C-m
tmux send-keys -t kafka-server "bin/kafka-server-start.sh config/server.properties" C-m

# cd ./dku_kafka
# cd kafka_2.13-3.9.0

# bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092