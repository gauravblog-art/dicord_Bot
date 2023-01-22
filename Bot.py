import discord
import responses

async def send_message(message, user_message, is_privet):
    try:
        response=responses.handle_respose(user_message)
        if is_privet== True:
            await message.author.send(response) 
        else:
            await message.channel.send(response)
    except Exception as e:
        print(e)
def run_discord_bot():
    Token="MTA2NTg1MTAzNjA3MTM3ODk0NA.GkN26P.npNz5KjVKN-DrmV5UgL_BPZgyq9WdLcw_imzbY"
    clients=discord.Client(intents=discord.Intents.default())
    @clients.event
    async def on_reeady():

        print(f'{clients.user} is on rining')
    
    @clients.event
    async def on_message(message):
        if message.author == clients.user:
            return 
        
        # username=str(message.author)
        user_messsage=str(message.content)
        # channel=str(message.channel)
        # print(user_messsage)

        if user_messsage[0]=='?':
            user_messsage=user_messsage[1:]
            await send_message(message, user_messsage, is_privet=True)
        else:
            await send_message(message, user_messsage, is_privet=False)
        
    clients.run(Token)
    on_reeady()
