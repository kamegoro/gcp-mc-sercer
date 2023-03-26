import discord
import time
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

TOKEN = os.getenv('TOKEN')
SERVICE_ACCOUNT_ID= os.getenv('SERVICE_ACCOUNT_ID')
GCP_PROJECT_NAME = os.getenv('GCP_PROJECT_NAME')
MINECRAFT_INSTANCE_NAME = os.getenv('MINECRAFT_INSTANCE_NAME')
MINECRAFT_INSTANCE_ZONE = os.getenv('MINECRAFT_INSTANCE_ZONE')

client = discord.Client()
compute = build('compute', 'v1')

#サーバー起動処理
def server_start():
    res = compute.instances().start(project=GCP_PROJECT_NAME, zone=MINECRAFT_INSTANCE_ZONE, instance=MINECRAFT_INSTANCE_NAME).execute()
    return
#サーバー停止処理
def server_stop():
    compute.instances().suspend(project=GCP_PROJECT_NAME, zone=MINECRAFT_INSTANCE_ZONE, instance=MINECRAFT_INSTANCE_NAME).execute()
    return
#サーバー情報取得
def server_status():
    res = compute.instances().get(project=GCP_PROJECT_NAME, zone=MINECRAFT_INSTANCE_ZONE, instance=MINECRAFT_INSTANCE_NAME).execute()
    return [res['status'], res['networkInterfaces'][0]['accessConfigs'][0]['natIP']]
@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == '/start minecraft':
        await message.channel.send('サーバーを開始します...')
        server_start()
        time.sleep(30)
        result = server_status()
        if result[0] == 'RUNNING':
            await message.channel.send('サーバーは起動済みです\nIP: ' + str(result[1]))
            return

        time.sleep(30)
        result = server_status()
        if result[0] == 'RUNNING':
            await message.channel.send('サーバーは起動済みです')
            return

    if message.content == '/stop minecraft':
        await message.channel.send('サーバーを停止します...')
        server_stop()
        time.sleep(30)
        status = server_status()[0]
        if status in { 'TERMINATED', 'STOPPING', 'SUSPENDED', 'SUSPENDING' }:
            await message.channel.send('サーバーを停止しました')
            return

        time.sleep(30)
        status = server_status()[0]
        if status in { 'TERMINATED', 'STOPPING', 'SUSPENDED', 'SUSPENDING' }:
            await message.channel.send('サーバーを停止しました')
            return

    if message.content == '/status minecraft':
        await message.channel.send('サーバーの状態を確認中です...')
        result = server_status()
        if result[0] == 'RUNNING':
            await message.channel.send('サーバーは起動済みです\nIP: ' + str(result[1]))
        if result[0] == 'STAGING':
            await message.channel.send('サーバーを起動中です。しばらくお待ちください')
        if result[0] in { 'TERMINATED', 'STOPPING', 'SUSPENDED', 'SUSPENDING' }:
            await message.channel.send('サーバーは停止しています')

client.run(TOKEN)