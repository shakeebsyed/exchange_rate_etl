#!/bin/bash

#Currency Exchange rate ETL automation Script

PROJECT_DIR="/home/$USER/Projects/exchange-rate-etl"
VENV_DIR="$PROJECT_DIR/venv"
LOG_FILE="$PROJECT_DIR/log.txt"


#Activating Virtual Env

#source = "$VENV_DIR/bin/activate"

cd "$PROJECT_DIR" || exit


#Running ETL Process and logging output

echo "========================================================================" >> "$LOG_FILE"
echo "ETL Run: $(date)" >> "$LOG_FILE"


python3 main.py >> "$LOG_FILE" 2>&1


if [ $? -eq 0 ]; then
    echo "ETL completed successfully at $(date)" >> "$LOG_FILE"
else
    echo "ETL failed at $(date)" >> "$LOG_FILE"
fi

echo "" >> "$LOG_FILE"
