#!/usr/bin/env python
# QuestGiver/bots/autoreply.py

import tweepy
import logging
from config import create_api
from questmaker import Request
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

quests = Request()

def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering to {tweet.user.name}")

            #if not tweet.user.following:
            #    tweet.user.follow()

            api.update_status(
            #    status="Please reach us via DM",
                status=quests.generate_new_quest(),
                in_reply_to_status_id=tweet.id,
            )
    return new_since_id

def main():
    api = create_api()
    since_id = 1
    
    while True:
        since_id = check_mentions(api, ["quest", "task"], since_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()