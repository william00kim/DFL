#!/bin/bash

build_DFL() {
    docker build -f Dockerfile -t "llm_server:1.0" ./
    docker compose -f compose.yaml up -d llm_server
    docker exec -d llm_server ollama serve
    sleep 5
    docker exec -it llm_server ollama pull gemma3:27b
    docker exec -it llm_server ollama pull exaone3.5:32b
}

start_DFL() {
    echo "Up DFL container"
    docker exec -d llm_server bash "conda activate dockerforllm", "uvicorn main:app --reload --host 172.20.0.2 --port 8888"
    # docker compose -f compose.yaml up -d llm_server
}

start_ollama_for_log() {
  docker compose -f compose.yaml up ollama_server
}

stop_DFL() {
    docker compose down llm_server
}

attach_ollama() {
    docker attach llm_server
}

attach_llm() {
    docker attach llm_server
}

if [ $# -eq 0 ]; then
  # No arguments
  echo "Must provide a valid task, e.g. deploy|update."
  echo "See 'deploy.sh help' for more options."
  exit 1;
else
  for arg in "$@"
  do
    case "$arg" in
      build)
        build_DFL
        ;;
      start)
        # (Re)start existing deployment
        start_DFL
        ;;
      attach_ollama)
        attach_ollama
        ;;
      attach_llm)
        attach_llm
        ;;
      test)
        start_ollama_for_log
        ;;
      stop)
        stop_DFL
        ;;
      restart)
        # Stop and remove currently running containers before starting
        stop_DFL
        start_DFL
        ;;
      *)
        echo "Error: Unsupported command " $1  # print to stderr
        exit 1
        ;;
    esac
  done
fi