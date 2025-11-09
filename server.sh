#!/bin/bash

PID_FILE=".server.pid"

start_server() {
    if [ -f "$PID_FILE" ]; then
        echo "El servidor ya está corriendo (PID: $(cat $PID_FILE))"
        exit 1
    fi
    
    echo "🚀 Iniciando Dog Breed AI Server..."
    echo ""
    
    source .venv/bin/activate
    uvicorn main:app --reload --host 0.0.0.0 --port 8000 &
    echo $! > $PID_FILE
    
    sleep 2
    echo ""
    echo "Servidor corriendo en:"
    echo "   http://localhost:8000         - Página de inicio"
    echo "   http://localhost:8000/breeds  - Catálogo de razas"
    echo "   http://localhost:8000/docs    - API Docs"
    echo ""
    echo "Para detener el servidor: ./server.sh stop"
    echo ""
}

stop_server() {
    if [ ! -f "$PID_FILE" ]; then
        echo "El servidor no está corriendo"
        exit 1
    fi
    
    PID=$(cat $PID_FILE)
    echo "Deteniendo servidor (PID: $PID)..."
    
    kill $PID 2>/dev/null
    rm -f $PID_FILE
    
    echo "Servidor detenido"
}

case "$1" in
    start)
        start_server
        ;;
    stop)
        stop_server
        ;;
    restart)
        stop_server
        sleep 1
        start_server
        ;;
    *)
        echo "Uso: ./server.sh {start|stop|restart}"
        exit 1
        ;;
esac
