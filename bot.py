import config
import discord
import logging
import random


class WelcomeBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.invites = []
        self.logger = logging.getLogger('discord')
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
        self.handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        self.logger.addHandler(self.handler)

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for new members"))
        guild = self.get_guild(int(config.server))
        self.invites = await guild.invites()

    async def on_invite_create(self, invite):
        self.invites = await invite.guild.invites()

    async def on_invite_delete(self, invite):
        self.invites = await invite.guild.invites()

    async def on_member_join(self, member):
        invites_after_join = await member.guild.invites()
        channel = member.guild.get_channel(int(config.welcome))
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
                emoji = config.bot_emoji if invite.inviter.id == int(config.bot) else str()
                await channel.send(random.choice(welcome_text).format(member.mention, emoji))
                self.invites = await member.guild.invites()
                return

    async def on_member_remove(self, member):
        self.invites = await member.guild.invites()


intents = discord.Intents.default()
intents.members = True
intents.invites = True

client = WelcomeBot(intents=intents)
client.run(config.token)
