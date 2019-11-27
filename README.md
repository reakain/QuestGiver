# Quest Giver
A twitter bot to provide quests for eager adventurers!

This python3 program uses tweepy and nltk to create procedural quest dialogue and post it to twitter for all who tweet at it.

## Build Docker Image
 1. Run the command in the shell from the project directory:

     ```docker build . -t quest-giver-bot```

 2. Test your build from powershell with
   
     ```docker run -it -e CONSUMER_KEY="key val here" -e CONSUMER_SECRET="key val here" -e ACCESS_TOKEN="key val here" -e ACCESS_TOKEN_SECRET="key val here" quest-giver-bot```
