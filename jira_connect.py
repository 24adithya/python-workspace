from jira import JIRA
import certifi

print(certifi.where())
  
# Specify a server key. It should be your
# domain name link. yourdomainname.atlassian.net

print('connecting to atlassian..')

jiraOptions = {'server': "https://narayanadithya.atlassian.net/"}
# jiraOptions = {'server': "https://narayanadithyajira.atlassian.net/"}

# Get a JIRA client instance, pass,
# Authentication parameters
# and the Server name.
# emailID = your emailID
# token = token you receive after registration

# using token
jira = JIRA(options=jiraOptions, basic_auth=(
    "narayanadithya@outlook.com", "JMP4XxXiIUWhlTNHiEER2BAA"))
print(jira)

# using username and password

print('connected to Adithya Narayan\'s atlassian account!')