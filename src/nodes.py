import os
import time
from supabase import create_client, Client
from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.search import GmailSearch

class Nodes():
    def __init__(self):
        self.gmail = GmailToolkit()
        
        self.supabase_url = os.getenv("SUPABASE_URL")
        self.supabase_key = os.getenv("SUPABASE_KEY")
        self.supabase: Client = create_client(self.supabase_url, self.supabase_key)
        
    

    def check_email(self, state):
        print("# Checking for new emails")
        search = GmailSearch(api_resource=self.gmail.api_resource)
        emails = search('after:newer_than:1d')
    
        
        supabase_data = self.supabase.table("emails").select("*").execute()
        unique_emails_dict = {email['ID']: email for email in supabase_data.data}

        for row in supabase_data.data:
            emails.append({
                "id": row["ID"],
                "threadId": row["threadId"],
                "snippet": row["snippet"],
                "sender": row["sender"],
                "cc": row.get("cc", "")
            })

        checked_emails = state['checked_emails_ids'] if state['checked_emails_ids'] else []
        thread = []
        new_emails = []
        print("List of email IDs that have already been checked.")
        print(checked_emails)

        for email in emails:
            is_new_email = (email['id'] not in checked_emails) and (email['threadId'] not in thread)
            is_cc_email = os.environ['MY_EMAIL'] in email.get('cc', '')

            if is_new_email and (os.environ['MY_EMAIL'] not in email['sender'] or is_cc_email):
                if email['id'] not in unique_emails_dict:
                    thread.append(email['threadId'])
                    self.supabase.table("emails").insert({
                        "ID": email['id'],
                        "threadId": email['threadId'],
                        "snippet": email['snippet'],
                        "sender": email["sender"],
                        "cc": email.get("cc", "")
                    }).execute()
                new_emails.append({
                    "id": email['id'],
                    "threadId": email['threadId'],
                    "snippet": email['snippet'],
                    "sender": email["sender"],
                    "cc": email.get("cc", "")
                })

        checked_emails.extend([email['id'] for email in emails])

        print("Original checked emails")
        print(checked_emails)

        return {
            **state,
            "emails": new_emails,
            "checked_emails_ids": checked_emails
        }

    def wait_next_run(self, state):
        print("## Waiting for 180 seconds")
        time.sleep(180)
        return state

    def new_emails(self, state):
        if len(state['emails']) == 0:
            print("## No new emails")
            return "end"
        else:
            print("## New emails")
            return "continue"
