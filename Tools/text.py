import discord
from discord.ext import commands
from discord import ui
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)

class PollView(ui.View):
    def __init__(self, options):
        super().__init__()
        self.options = options
        self.votes = {option: 0 for option in options}
        self.respondents = {option: [] for option in options}
        self.user_votes = {}
        
        for i, option in enumerate(options):
            button = ui.Button(label=f"Option {i + 1}", style=discord.ButtonStyle.primary)
            button.callback = self.create_callback(option)
            self.add_item(button)

    def create_callback(self, option):
        async def callback(interaction: discord.Interaction):
            user = interaction.user

            if user.id not in self.user_votes:
                self.user_votes[user.id] = []

            if option in self.user_votes[user.id]:
                return

            self.votes[option] += 1
            self.respondents[option].append(user.name)
            self.user_votes[user.id].append(option)
            await interaction.response.defer()

        return callback

@client.event
async def on_ready():
    print('Python is ready.')

@client.command(name="poll")
async def create_poll(ctx, question: str, delay: int, *options: str):
    if len(options) < 2:
        await ctx.send("You need to provide at least two options for the poll.")
        return
    if len(options) > 10:
        await ctx.send("You can only provide up to 10 options.")
        return

    embed = discord.Embed(
        title="📊 Poll",
        description=question,
        color=discord.Color.blurple()
    )

    for i, option in enumerate(options):
        embed.add_field(name=f"Option {i + 1}: {option}", value="", inline=False)

    embed_message = await ctx.send(embed=embed)

    view = PollView(options)
    await embed_message.edit(view=view)

    await asyncio.sleep(delay)

    results_embed = discord.Embed(
        title="📊 Poll Results",
        description=f"Results for: {question}",
        color=discord.Color.green()
    )

    for i, option in enumerate(options):
        vote_count = view.votes[option]
        voters = ", ".join(view.respondents[option]) if view.respondents[option] else "No voters"
        results_embed.add_field(name=f"Option {i + 1}: {option}", value=f"Votes: {vote_count}\nVoters: {voters}", inline=False)

    await ctx.send(embed=results_embed)

client.run("")
