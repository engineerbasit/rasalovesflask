### This script is triggered from within docker contrainer
### to start multiple processes in the same container.
### This script is defined in the CMD option in Dockerfile

cd app/


# Start rasa server with nlu model
python -m rasa run --enable-api --cors="*" --port 5005 --debug \
        -p $PORT
python app.py 

