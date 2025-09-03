function agent() {
    if pgrep -f "agent-main.py" > /dev/null; then
        echo "Agent is already running. Please stop it first or use 'fg' if suspended."
    else
        echo "Starting the agent..."
        python3 /home/rudra/Desktop/Terminal-Agent/agent-main.py
        echo "Agent stopped."
    fi
}

function stopagent() {
    pid=$(pgrep -f "agent-main.py")
    if [ -n "$pid" ]; then
        echo "Stopping the agent..."
        kill "$pid"
        echo "Agent stopped."
    else
        echo "Agent is not running."
    fi
}
