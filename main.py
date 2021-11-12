import discord
import os
from discord.ext import commands

import xkcd as x
import requests
from bs4 import BeautifulSoup

from helper import *
import alive
import random
import time


client = commands.Bot(command_prefix="f!")
client.remove_command("help")


@client.event
async def on_ready():
    print('Successfully Logged In As {0.user}.'.format(client))


@client.command(pass_context=True)
async def test(ctx):
  if str(ctx.message.author) != "fɪɹ̠̊ət̼ħɘɭøʂʈ🔥#7739":
    await ctx.send("You don't have permission to use this command.")

  else:
    await ctx.send("There is nothing being tested right now.")


@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(color=discord.Color.dark_gold())

    embed.set_author(name="Help Navigation Center")
    embed.add_field(name="f!advancedhelp", value="Opens the advanced commands center.", inline=False)
    embed.add_field(name="f!modhelp", value="Opens the mod commands center.", inline=False)
    embed.add_field(name="f!texthelp", value="Opens the text based commands center.", inline=False)
    embed.add_field(name="f!whatsnew <query>", value="Sends a snippet of a news article about query.", inline=False)
    embed.add_field(name="f!quote", value="Sends an inspirational quote.", inline=False)
    embed.add_field(name="f!fact", value="Sends a random fun fact.", inline=False)
    embed.add_field(name="f!joke", value="Sends a random programmer joke.", inline=False)
    embed.add_field(name="f!xkcd", value="Sends a random XKCD comic.", inline=False)
    embed.add_field(name="f!xkcd today", value="Sends the latest XKCD comic.", inline=False)
    embed.add_field(name="f!xkcd <n>", value="Sends the nth XKCD comic.\nExample: 'f!xkcd 1000' returns the 1000th XKCD comic.", inline=False)

    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def advancedhelp(ctx):
    embed = discord.Embed(color=discord.Color.dark_gold())

    embed.set_author(name="Advanced Commands")
    embed.add_field(name="f!about", value="Shows information on the bot.", inline=False)
    embed.add_field(name="f!version", value="Shows information on the latest update.", inline=False)
    embed.add_field(name="f!privacy", value="Shows information about how we collect data.", inline=False)
    embed.add_field(name="f!reportbug", value="Allows you to add a complaint on a known bug.", inline=False)
    embed.add_field(name="f!request", value="Allows you to send a request for a new feature.", inline=False)
    embed.add_field(name="f!ping", value="Returns 'Pong!' plus your latency.", inline=False)
    embed.add_field(name="f!whoami", value="Returns your Discord username.", inline=False)

    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def texthelp(ctx):
    embed = discord.Embed(color=discord.Color.dark_gold())

    embed.set_author(name="Text Based Commands")
    embed.add_field(name="f!hello", value="Returns 'Hello There!'", inline=False)
    embed.add_field(name="f!bye", value="Returns 'Goodbye!'", inline=False)
    embed.add_field(name="f!shrug", value="Returns '¯\_(ツ)_/¯'", inline=False)
    embed.add_field(name="f!ping", value="Returns 'Pong!' plus your latency.", inline=False)
    embed.add_field(name="f!pong", value="Returns 'Ping!' plus a ping.", inline=False)
    embed.add_field(name="f!whoami", value="Returns your Discord username.", inline=False)
    embed.add_field(name="f!whyami", value="¯\_(ツ)_/¯", inline=False)
    embed.add_field(name="f!put <message>", value="Prints the message out again.", inline=False)
    embed.add_field(name="f!echo <message>", value="Deletes the original message and echos it out again.", inline=False)
    embed.add_field(name="f!roll <number>", value="Rolls a die. You can specify the highest number. The default is 6.", inline=False)

    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def modhelp(ctx):
    embed = discord.Embed(color=discord.Color.dark_gold())

    embed.set_author(name="Commands For Mods")
    embed.add_field(name="f!kick <@user> <reason>", value="Kicks the user.", inline=False)
    embed.add_field(name="f!ban <@user> <reason>", value="Bans the user.", inline=False)
    embed.add_field(name="f!unban <user>", value="Unbans the user.", inline=False)

    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def secret(ctx):
    embed = discord.Embed(color=discord.Color.dark_gold())

    embed.set_author(name="Secret Commands")
    embed.add_field(name="f!echo <message>", value="Deletes the original message and echos it out again.", inline=False)
    embed.add_field(name="f!whyami", value="¯\_(ツ)_/¯", inline=False)
    embed.add_field(name="f!pong", value="Returns 'Ping!' plus a ping.", inline=False)

    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def version(ctx):
    version, changes = getUpdate()

    embed = discord.Embed(color=discord.Color.dark_red(), description=version)

    embed.set_author(name="Latest Update Information")
    embed.add_field(name="Changelog", value=changes, inline=False)

    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def privacy(ctx):
    embed = discord.Embed(color=discord.Color.dark_red())

    embed.set_author(name="Privacy Concerns")
    embed.add_field(name="What data do we collect?", value="We collect data passed to the echo command.\nWe collect your Discord username, message, and the time the message has been sent.\nWe do this because the original message is always deleted, so we keep a log for moderation purposes.\nWe also do this for the put command, for the same reasons.", inline=False)

    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def about(ctx):
    embed = discord.Embed(color=discord.Color.dark_red())

    embed.set_author(name="About")
    embed.add_field(
        name="About", value="This bot has been fully completed. Its life goal has been fulfilled!",
        inline=False
    )

    await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="IDK"):
  await member.kick(reason=reason)
  await ctx.send(f'User {member} has been kicked.\nReason: {reason}')

@kick.error
async def kick_error(ctx, error):
   if isinstance(error, commands.errors.MissingPermissions):
       await ctx.send("You don't have permission to use this command.")

@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="IDK"):
  await member.ban(reason=reason)
  await ctx.send(f'User {member} has been kicked.\nReason: {reason}')

@ban.error
async def ban_error(ctx, error):
   if isinstance(error, commands.errors.MissingPermissions):
       await ctx.send("You don't have permission to use this command.")

@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    res = member.find("#")

    if res >= 0:
      banned_users = await ctx.guild.bans()
      member_name, member_discriminator = member.split("#")

      for ban_entry in banned_users:
          user = ban_entry.user

          if (user.name, user.discriminator) == (member_name, member_discriminator):
              await ctx.guild.unban(user)
              await ctx.send(f'User {user.mention} has been unbanned.')
              return

      await ctx.send(f'Could not find {member} in the ban list.')

    else:
      banned_users = await ctx.guild.bans()
      member_name = member

      for ban_entry in banned_users:
          user = ban_entry.user

          if (user.name) == (member_name):
              await ctx.guild.unban(user)
              await ctx.send(f'User {user.mention} has been unbanned.')
              return

      await ctx.send(f'Could not find {member} in the ban list.')



@unban.error
async def unban_error(ctx, error):
   if isinstance(error, commands.errors.MissingPermissions):
       await ctx.send("You don't have permission to use this command.")


@client.command()
async def hello(ctx):
    await ctx.send(f'Hello There!')


@client.command()
async def bye(ctx):
    await ctx.send(f'Goodbye!')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def pong(ctx):
    await ctx.send(f'Ping! {ctx.message.author.mention}')


@client.command()
async def shrug(ctx):
    await ctx.send(f'¯\_(ツ)_/¯')


@client.command()
async def roll(ctx, num=6):
    await ctx.send(random.randint(1,num))


@client.command()
async def whoami(ctx):
    await ctx.send("You Are " + str(ctx.message.author))


@client.command()
async def whyami(ctx):
    await ctx.send(f'¯\_(ツ)_/¯')


@client.command()
async def quote(ctx):
    quote, author = getQuote()

    embed = discord.Embed(color=discord.Color.dark_orange())

    embed.set_author(name="An Inspirational Quote")
    embed.add_field(name=f"{quote}", value=f"- {author}", inline=False)

    await ctx.send(embed=embed)


@client.command()
async def whatsnew(ctx, *, query):
    await ctx.send(f'Searching for news about \'{query}\'.')
    title, text, url, img, times, has_error = getNews(query)

    if has_error:
      await ctx.send(f'No news found for \'{query}\'.')

    else:
      embed = discord.Embed(color=discord.Color.dark_orange())

      embed.set_author(name=f"News About '{query}''")
      embed.add_field(name=f"{title}", value=f"{text}", inline=False)
      embed.set_image(url=img)
      embed.set_footer(text = "Read More At: " + url + "\n\n" + "Published At: " + times)

      await ctx.send(embed=embed)


@client.command()
async def joke(ctx):
    embed = discord.Embed(color=discord.Color.dark_orange())

    embed.set_author(name="A Programming Joke")
    embed.add_field(name=f"Joke", value=f"{getJoke()}", inline=False)

    await ctx.send(embed=embed)


@client.command()
async def fact(ctx):
    embed = discord.Embed(color=discord.Color.dark_orange())

    embed.set_author(name="A Fun Fact")
    embed.add_field(name=f"Fact", value=f"{getFact()}", inline=False)

    await ctx.send(embed=embed)


@client.command()
async def echo(ctx, *, arg):
    tracker = open('echo-users.txt', 'a')
    tracker.write(str(ctx.message.author) + f" ({ctx.message.guild}): " + arg + " @ " + time.ctime() + "\n")
    tracker.close()
    
    await ctx.message.delete()
    await ctx.send(arg)


@client.command()
async def put(ctx, *, arg):
    tracker = open('put-users.txt', 'a')
    tracker.write(str(ctx.message.author) + f" ({ctx.message.guild}): " + arg + " @ " + time.ctime() + "\n")
    tracker.close()

    await ctx.send(arg)


@client.command()
async def xkcd(ctx, message=None):
  if message == None:
    comic = x.getRandomComic()

  elif message == "today":
    comic = x.getLatestComic()

  else:
    comic = x.getComic(message)

  embed = discord.Embed(color=discord.Color.dark_magenta())
  embed.set_image(url=comic.getImageLink())
  embed.set_footer(text = comic.getAltText())

  embed.set_author(name = comic.getTitle())

  await ctx.send(embed=embed)


@client.command()
async def reportbug(ctx, *, arg):
    tracker = open('bug-tracker.txt', 'a')
    tracker.write(arg + "\n")
    tracker.close()

    await ctx.send(f"'{arg}' has been reported and will be fixed shortly.")


@client.command()
async def request(ctx, *, arg):
    tracker = open('requests.txt', 'a')
    tracker.write(arg + "\n")
    tracker.close()

    await ctx.send(f"'{arg}' has been requested for and will be considered.")
  
    

alive.keep_alive()
client.run(os.environ['Token'])