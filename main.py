from discord.ext import commands
import dotenv
import os

dotenv.load_dotenv()


class AssignBot(commands.Bot):
    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)
        self.assign_users = {}

    async def on_ready(self):
        print("Bot is now ready.")

    def open_issue(self, channel_id):
        if self.assign_users.get(channel_id) is not None:
            raise ValueError("Already opened.")
        self.assign_users[channel_id] = []

    def close_issue(self, channel_id):
        if self.assign_users.get(channel_id) is None:
            raise ValueError("not opened.")
        del self.assign_users[channel_id]

    def assign(self, channel_id, user_id):
        if self.assign_users.get(channel_id) is None:
            raise ValueError("not opened.", 0)
        elif user_id in self.assign_users[channel_id]:
            raise ValueError("already assigned.", 1)

        if len(self.assign_users[channel_id]) >= 2:
            raise DeprecationWarning("three or more users have been assigned to the issue.")
        self.assign_users[channel_id].append(user_id)


bot = AssignBot(command_prefix="a.", description="チャンネルにissueを開き、そのissueにassignできます。\n3人以上がassignしようとすると警告を表示します。")

@bot.command(name="open")
async def _open(ctx):
    """issueを開きます。"""
    try:
        bot.open_issue(ctx.channel.id)
    except ValueError:
        return await ctx.send("すでにオープンされています。", delete_after=5)
    await ctx.message.add_reaction("\U0001f44d")

@bot.command()
async def assign(ctx):
    """開かれているissueにassignします。"""
    try:
        bot.assign(ctx.channel.id, ctx.author.id)
    except ValueError as e:
        if e.args[1] == 0:
            return await ctx.send("issueがオープンされていません。", delete_after=5)
        elif e.args[1] == 1:
            return await ctx.send("すでにassignしています。")
    except DeprecationWarning:
        return await ctx.send("すでに2人assignしているため、assignできませんでした。", delete_after=5)
    await ctx.message.add_reaction("\U0001f44d")

@bot.command()
async def close(ctx):
    """issueをcloseします。"""
    try:
        bot.close_issue(ctx.channel.id)
    except ValueError:
        return await ctx.send("issueがオープンされていません。", delete_after=5)
    await ctx.message.add_reaction("\U0001f44d")

if __name__ == "__main__":
    bot.run(os.environ["DISCORD_TOKEN"])
