import discord

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready(): # "파이썬을 개발할때 디스코드 봇이 준비가 되었는지 유무를 판단한다"
    print("개발자 디스코드 : ! KNS Deve1l#7411")
    print(client.user.name)
    print("=================")
    await client.change_presence(activity=discord.Game(name="KNS SERVER 감시"))

@client.event
async def on_member_join(member): # " 사람이 서버에 들어오면 입퇴장-로그에 "안녕하다는 문구가 뜬다" "
    guild = client.get_guild(812338526666227743)
    channel = guild.get_channel(812351402441310227)
    await channel.send(f"**{member.mention}**님 저희 **{guild.name}**에 오신것을 환영합니다! ! :partying_face:")
    await member.send(f"안녕하세요! **{member.mention}**님 **{guild.name}**에 오신것을 환영합니다! :partying_face: \n #**규칙안내**를 읽어주신 후, **#자기소개**에 양식을 써주시기 바랍니다. \n 양식은 [이름/나이/성별] 입니다.  (이름빼고 나머지 필수)")

@client.event
async def on_member_remove(member): # " 사람이 서버를 나가면 입퇴장-로그에 "안녕히가라는 문구가 뜬다" "
    guild = client.get_guild(812338526666227743)
    channel = guild.get_channel(812351402441310227)
    await channel.send(f"**{member.mention}**님 지금까지 저희 **{guild.name}**에 많은 관심과 사랑을 가져주셔서 감사했습니다:) :sob:")

@client.event
async def on_message(message):
    if message.content.startswith("!삭제"): # " !삭제 1 " 1개의 메세지를 삭제한다.
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메세지를 삭제하였습니다!")

    if message.content.startswith("!공지사항"): # " !공지사항  채널아이디  공지할 내용 "엔터를 누르면 문구가 공지사항 채널로 나감
        ch = client.get_channel(int(message.content[6:24]))
        await ch.send(message.content[25:])
        await message.delete()
        
client.run("ODEyMzk0Mzg0NDEzOTQ5OTYy.YDAHOg.s_iUJbhMgT7E6gQb_dvWHzgLUew")