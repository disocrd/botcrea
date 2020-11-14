elif message.content == "?도움말":
    embed=discord.Embed(colour=0x3AFF01)
    embed.add_field(name="Kaiabot help", value="카야봇 도움말\n자세한내용은 공식 디스코드 참조", inline=False)
    embed.add_field(name="게임", value="""
    ```
    >송금 @mention\n금액\n>도박 금액\n>가입
    ```""", inline=True)
    embed.add_field(name="정보", value="""
    ```
    >프로필\n>서버\n>정보
    ```""", inline=True)
    embed.add_field(name="관리", value="""
    ```
    >삭제 삭제할 양\n>킥 @mention\n>밴 @mention
    ```""", inline=True)
    embed.add_field(name="관리", value="""
    ```
    >삭제 삭제할 양\n>킥 @mention\n>밴 @mention
    ```""", inline=False)
    embed.set_footer(text=f"{message.author}님에게 요청됨")
    await message.channel.send(embed=embed)
