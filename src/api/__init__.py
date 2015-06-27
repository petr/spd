"""
This module contains the full api workflow od the project sex partners

It has the following methods

* Upload an image to server and returns task id
* Method for processing this task


#/image_put

curl -F "image=@fixtures/members-301f4eab458270d4ad75856b9c7962de.jpg" http://127.0.0.1:8000/api/image_put/


#/task/<id>/
curl http://127.0.0.1:8000/api/tasks/1234/

Response: 
{
    "status": "processing"
}

Response:
{
    "error": "invalid_task"
}
"""
