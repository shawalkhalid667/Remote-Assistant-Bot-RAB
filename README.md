# Remote Assistant Bot (RAB)
##### _CS5704 - Software Engineering Project_
###### _Created By: [Pratik Nalage](https://github.com/PratikNalage), [Sumukh Bapat](https://github.com/sumukh23), [Shawal Khalid](https://github.com/shawalkhalid667), [Shunyu Yao](https://github.com/DavidYao1518)_

## Project Description

Remote Assistant Bot is a platform to foster collaboration between remote software engineers. It is generic enough to extend to other categories of remote workers. RAB is a QnA platform that solves queries of newly joined software engineers by connecting them to a senior software engineers. RAB tries to learn and understand the questions and their responses. RAB acts as a single point of contact for all software engineers to resolve their queries and eventually boost productivity.


## Features

- Provide response to the user's query from it's database
- Connect new software engineers to senior software engineers for new queries
- Logging the conversation and understanding it to reduce the dependency on senior software engineers in the future.
- Periodic training for understanding similar questions
- Small talk and greetings module
- Entertain software engineers by telling a joke
- Import/Export model for training/deploying


## Requirements

RAB requires [Diagloflow](https://dialogflow.cloud.google.com/) to run.
Download and set up [Ngrok](https://ngrok.com/)


#### DialogFlow Setup
1. Create a Google Cloud Account 
2. Open a new project in DialogFlow account
3. Zip the RemoteAssistantBot Folder and import to DialogFlow
4. Goto project's settings and download [keys.json](https://cloud.google.com/dialogflow/es/docs/quick/setup)
5. Replace the current keys.json file with the newly downloaded file
6. Enable Webhook in DialogFlow setting's and enter the URL created by Ngrok in the Webhook Fulfillment section
7. Save and test changes

#### Backend Server Setup

Backend Server is written in Flask and it uses a SQLite3 database. You need to install the following python packages.

```sh
pip install grpcio cryptography google-cloud google-cloud-dialogflow flask sqlite3
```

#### Deploying to Production
1. Turn off Debugging in the Flask app
2. Goto DialogFlow and enable integration of Web or any other platform you'd like
3. Host the Backend Server on either your local machine or AWS or GCP


#### Port Clashes for MacOS Monterey
If you're using an M1 mac, the default port 5000 of the Flask application might crash with the AirPlay server. In that case you need to change the port to 5001 or any other free port.
```sh
./ngrok http 5001
flask run -p 5001
```


## Sample Use Case
1. Send a query to the chatbot
2. Chatbot will check if the query is present in the database. If yes, it'll answer directly, else the chatbot will forward the query to the senior person in/outsite the team.
3. When the senior person answers the question, the chatbot will store it query and it's response

#### Example:

User's query -> What actions can I take if I see a long running query on the database

RAB's response -> You can follow these steps to solve the issue -
https://en.wikipedia.org/wiki/Main_Page/longrunningqueries

You can try this use case on the below Demo link


## Demo
The front-end DiaglogFlow setup is hosted on https://www.pratiknalage.com/techbot


## Unit Tests
1. Navigate to the intents folder - https://github.com/PratikNalage/RemoteAssistantBot/tree/main/RemoteAssistantBot/intents
2. Parse the JSON
3. Use the test from *usersays_en.json as input
4. Validate against message field from *response.json as output

#### Why we haven't included unit test cases?
The unpaid version of DialogFlow (DialogFlow ES) is limited and doesn't support unit test cases out of the box. Nevertheless, we have enabled validation in diaglowFlow that validates the intents and entities post training the model. So validation testing is covered but unit testing is not. However, if we upgrade the CX version, we can write a unit test as above.


## Study Materials
DiaglowFlow - https://cloud.google.com/dialogflow/docs

Flask - https://flask.palletsprojects.com/en/2.1.x/

Project Proposal - https://github.com/PratikNalage/RemoteAssistantBot/blob/main/docs/Techbot-proposal.pdf

Final Proposal - https://github.com/PratikNalage/RemoteAssistantBot/blob/main/docs/Techbot-report.pdf


## Project Tracking
We used Kanban Board and Gantt Chart to track the overall progress. Here's the link to the [board](https://docs.google.com/spreadsheets/d/1n9NjL94_rJ7Lya5gjzQ_U1tNRg3a55yb5krC0SPcepo/edit?usp=sharing)


## License

MIT
