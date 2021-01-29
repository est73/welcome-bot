import config
import discord
import random


class WelcomeBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.invites = []

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        guild = await self.fetch_guild(config.server)
        self.invites = await guild.invites()

    async def on_invite_create(self, invite):
        self.invites = await invite.guild.invites()

    async def on_invite_delete(self, invite):
        self.invites = await invite.guild.invites()

    async def on_member_join(self, member):
        invites_after_join = await member.guild.invites()
        welcome_text = [
            "{0} joined the party. {1}",
            "{0} is here. {1}",
            "Welcome, {0}. We hope you brought pizza. {1}",
            "A wild {0} appeared. {1}",
            "{0} just landed. {1}",
            "{0} just slid into the server. {1}",
            "{0} just showed up! {1}",
            "Welcome {0}. Say hi! {1}",
            "{0} hopped into the server. {1}",
            "Everyone welcome {0}! {1}",
            "Glad you're here, {0}. {1}",
            "Good to see you, {0}. {1}",
            "Yay you made it, {0}! {1}",
        ]

        def find_invite(invites, code):
            for inv in invites:
                if inv.code == code:
                    return inv

        for invite in self.invites:
            if invite.uses < find_invite(invites_after_join, invite.code).uses:
                channel = await self.fetch_channel(config.welcome)
                emoji = config.bot_emoji if invite.inviter.id == int(config.bot) else str()
                await channel.send(random.choice(welcome_text).format(member.mention, emoji))
                self.invites = await member.guild.invites()

    async def on_member_remove(self, member):
        self.invites = await member.guild.invites()


intents = discord.Intents.default()
intents.members = True
intents.invites = True

client = WelcomeBot(intents=intents)
client.run(config.token)
