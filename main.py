from discord_webhook import DiscordWebhook, DiscordEmbed
from time import sleep
from os import system
def clr():
  system("clear")


amount = 5


def msgsend():
  fs = open('varfuncsend.pyvar', 'r')
  contentsoffile = fs.read()
  webhook = DiscordWebhook(url=urlcred)
  embed = DiscordEmbed(title='RAIDED BY FINS RAID UTILITY', description=contentsoffile, color='FF0000')
  embed.set_footer(text='RAIDED!!', icon_url='URL of icon')
  webhook.add_embed(embed)
  response = webhook.execute()


print("WARNING:\nANYTHING YOU DO WITH THIS IS NOT MY FAULT!!!")
sleep(5)
clr()

# raid creds
urlcred = input("\n\nWhat is the webhook URL?\n")


clr()
print("Would you like a custom message? (Y/N)")
confirmation1 = input("\n")
if confirmation1 == "Y":
  clr()
  print("Continuing...")
  custommsg = input("What would you like the message to be?\n\n")
elif confirmation1 == "N":
  clr()
  custommsg = "RAIDED!! DONT SHARE WEBHOOK URLS LOLOLOL"
else:
  quit()

# Writing
fs = open('varfuncsend.pydict', 'w')
predict = {
  url: urlcred,
  content: content
}
fs.write()
# raid time >:)
clr()
print("Settings up\n\n")



print("Now raiding...")
times = 0
while True:
  times = times + 1
  if times == amount:
    print("Raid done...")
    quit()
  msgsend()
  
