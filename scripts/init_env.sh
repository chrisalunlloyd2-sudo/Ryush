# Ryush Intent Resolver
run() {
    local user_intent="$*"
    python3 ~/Ryush/scripts/intent_mapper.py "$user_intent"
}
export -f run
