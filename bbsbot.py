# -*- coding:utf-8 -*-
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import asyncio

import random
from random import randint
import requests
from bs4 import BeautifulSoup

def cidades():
    cidades = ['Barueri', 'Belo Horizonte', 'Brasília', 'Campinas', 'Campo Grande', 'Cuiabá', 'Curitiba', 'Diadema', 'Fortaleza', 'Franca', 'Goiânia', 'Guarulhos', 'Jundiaí', 'Manaus', 'Olinda', 'Osasco', 'Recife', 'Ribeirão Preto', 'Rio Branco', 'Rio de Janeiro', 'Santo André', 'Santos', 'São Bernardo do Campo', 'São José dos Campos', 'São Paulo', 'Uberlândia']
    text = ''
    x = 0
    key = ''
    for c in cidades:
        if x == 12:
            key = ' +'
        
        text = text + '#' + str(x) + ' - ' + c + key + '\n'
        x+=1
        key=''

    
    return text.split('+')

def categorias():
    categorias = ['Sem álcool', 'Cervejas', 'Destilados', 'Vinhos', 'Petiscos', 'Outros']
    text = ''
    x = 0
    for c in categorias:
        text = text + '#' + str(x) + ' - ' + c + '\n'
        x+=1

    return text

def catalogo():
    #url = 'https://catalogoambev.com.br/site'
    #catalogoambev = requests.get(url)
    #soup = BeautifulSoup(catalogoambev.text, 'html.parser')

    #name_list = soup.find(class_='listing')
    #name_list_items = name_list.find_all('a')

    catalogo = []
    #for name in name_list_items:
        #print(name.get('title'))
        #catalogo.append(name.get('title'))
 
    catalogo.append(['Fusion', 'https://catalogoambev.com.br/images/uploads/logotipos/f6a10d0982152a0325e350f271f769e8.png', '10.00'])
    catalogo.append(['Guaraná Antarctica', 'https://catalogoambev.com.br/images/uploads/logotipos/bf1ec961a44647366641db570997ab1d.png', '5.00'])
    catalogo.append(['Pepsi', 'https://catalogoambev.com.br/images/uploads/logotipos/5a9197e0d01cea04a9411ef4d47dc44d.png', '5.00'])
    catalogo.append(['H2OH', 'https://catalogoambev.com.br/images/uploads/logotipos/93eade765ff23b3075e4ae4daf675d6f.png','4.50'])
    catalogo.append(['Outros', '', 'Vários'])

    return catalogo

def frases():
    frases = []
    
    frases.append('"O sucesso nasce do querer, da determinação e persistência em se chegar a um objetivo. Mesmo não atingindo o alvo, quem busca e vence obstáculos, no mínimo fará coisas admiráveis” – José de Alencar')
    frases.append('"Se você quer ser bem-sucedido precisa de dedicação total, buscar seu último limite e dar o melhor de si mesmo” – Ayrton Senna')
    frases.append('"Não crie limites para si mesmo. Você deve ir tão longe quanto sua mente permitir. O que você mais quer pode ser conquistado” – Mary Kay Ash')
    frases.append('"Nenhum obstáculo será grande se a sua vontade de vencer for maior” – Autor desconhecido')
    frases.append('"Dificuldades preparam pessoas comuns para destinos extraordinários” C.S Lewis')
    frases.append('"Nenhum homem será um grande líder se quiser fazer tudo sozinho ou se quiser levar todo o crédito por fazer isso” – Andrew Carnegie')
    frases.append('"Bom mesmo é ir à luta com determinação, abraçar a vida com paixão, perder com classe e vencer com ousadia, porque o mundo pertence a quem se atreve e a vida é muito curta, para ser insignificante” — Charlie Chaplin')
    frases.append('"Pessoas vencedoras não são aquelas que não falham, são aquelas que não desistem”  – Autor desconhecido')
    frases.append('"Só existem dois dias do ano em que você não pode fazer nada: um se chama ontem e outro amanhã” – Dalai Lama')
    frases.append('"A vida é um constante recomeço. Não se dê por derrotado e siga adiante. As pedras que hoje atrapalham sua caminhada amanhã enfeitarão a sua estrada”  – Autor desconhecido')
    frases.append('"Ouse ir além, ouse fazer diferente e o poder lhe será dado!” – José Roberto Marques')
    frases.append('"Ouse, arrisque, não desista jamais e saiba valorizar quem te ama, esses sim merecem seu respeito. Quanto ao resto, bom, ninguém nunca precisou de restos para ser feliz” – Clarice Lispector')

    return frases[randint(0,11)]

def cadastro(user, check: False):
    cadastros = [
        ['9998', 'a@a.com', 'Espero que tenha gostado da última compra. :v:  '],
        ['4960', 'a@a.com', 'Você ainda não fez nenhuma compra comigo. :slight_smile:']
    ]

    for cad in cadastros:
        if cad[0] == user.split('#')[1]:
            return True if check else cad[2]

    return False if check else 'Você ainda não tem cadastro, vamos fazer? Use o comando (`.cad`) :thinking:'
    

description = '''Este bot é dedicado a produto da Ambev. :slight_smile:'''

def command_prefix(bot, message):
    if message.guild is None:
        return '.'
    else:
        return '.'

bot = commands.Bot(command_prefix=command_prefix, description=description, case_insensitive=False)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    #Game
    activity = discord.Activity(type=discord.ActivityType.listening, name="Be Back In a Second")#, type=1
    await bot.change_presence(activity=activity)#status=discord.Status.idle, 

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        msg = 'Pode me chamar aqui com (`.ajuda`) ou no privado com (`ajuda`)!'
        await message.channel.send(msg)

    if message.guild is None and message.content.startswith('ajuda'):        
        await ajuda(message.channel)
		
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
  
  msg = "Bem vindo :partying_face: :partying_face:  {}\nEspero que esteja bem! Vou te add nos meus contatinhos, ok? :wink:\nQuando quiser refrescar a garganta é só me chamar aqui com (`.ajuda`) ou no privado com (`ajuda`)!\nSerá um prazer te servir! Abraços virtuais.".format(member.mention)
  for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send(msg)

        if str(channel) == "geral":
            await channel.send(msg)
  
@bot.event
async def on_member_remove(member):
   
   msg = "Adeus {}...poxa nem tomou uma gelada comigo! :sob: :sob: ".format(member.mention)
   for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send(msg)

        if str(channel) == "geral":
            await channel.send(msg)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send('Não entendi :disappointed_relieved:, tente digitar `.ajuda` :smiley:.')
    raise error

bot.remove_command('help')
@bot.command(description='Ajuda')
async def ajuda(ctx, *choices: str):
    msg = await ctx.send(frases())
    #await ctx.send('Ops! :grimacing: Me empolguei, segue a lista de comandos:')
    #await ctx.send('comandos: bbs + agua, heineken, veneno, lindo, game, hacka ')
    #await ctx.send('comandos: dm, lista, add, total, pagar')
    embed = discord.Embed(title="Ops! :grimacing:", description="Me empolguei, segue a lista de comandos::", color=0xeee657)
    embed.add_field(name=".cad", value="Vou te convidar para fazer o cadastro no sistema.", inline=False)
    embed.add_field(name=".cid", value="Cidades que atendemos", inline=False)	
    embed.add_field(name=".dm", value="Vou te chamar no privado.", inline=False)
    embed.add_field(name=".bbs", value="Convite especial.", inline=False) 
    embed.add_field(name=".l", value="Listagem de itens.", inline=True)
    embed.add_field(name=".add #id", value="Adiciona uma item no carrinho (.add #10).", inline=True)
    embed.add_field(name=".t", value="Total da compra.", inline=False)
    embed.add_field(name=".p", value="Finaliza a sua compra. ", inline=True)
    embed.add_field(name=".r", value="Rastreia o seu último pedido. ", inline=False)
    embed.add_field(name=".ajuda", value="Vou enviar essas mensagens novamente.", inline=False) 
    embed.add_field(name=".cls", value="Vou apagar nossas mensagens.", inline=True)
    embed.add_field(name=".cheat", value="Shiii... segredinhos.", inline=True) 
    await ctx.send(embed=embed)

    user = await bot.fetch_user(ctx.message.author.id)   
    await ctx.send(cadastro(str(ctx.message.author), False))

@bot.command(pass_context=True)
async def rand(ctx, timeout: int=5):
    response = [
    "Galera, bora refrescar a garganta? Usa o comando .l", 
    "Hey, bora refrescar a garganta? Usa o comando .l"
    ]
    # ,
    # "Psiu, você mesmo, bora refrescar a garganta? Usa o comando .l",
    # "Opppaaa, sextou, bora refrescar a garganta? Usa o comando .l"
    #response = []
    server = ctx.message.guild
    users = []
    for member in server.members:
        if member.name == 'BBS' or member.name == 'bot2' or member.name == 'Rythm' or member.name == 'Groovy':
            pass
        else:    
            users.append(member)
            response.append("{0.mention}, bora refrescar a garganta? Usa o comando .l".format(member))
 
    for u in users:
        response.append("{0.mention}, falou que hoje o energetico é por conta dele. :eyes:".format(u))
        response.append("{0.mention},".format(u) + " {0.mention} falou que hoje o energetico é por sua conta. :eyes:".format(users[randint(0, len(users)-1)]))
    
    # channel = ctx.message.channel 
    # for r in response:
    #     await channel.send(r)
    

    channel = ctx.message.channel 
    while True:
        await channel.send(response[randint(0,len(response)-1)])#response[randint(0,11)] random.choice(response)
        await asyncio.sleep(timeout*60/4) 

@bot.group()
async def cat(ctx):
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="Categorias", description="...", color=0xeee657)
        #embed = discord.Embed(title="Faça seu pedido", description=".add #<id>") #,color=Hex code
        #embed.add_field(name="Exemplo: ", value="Eu gostaria de adicionar o item #10 (`.add #10`)")
        embed.add_field(name=categorias(), value='Para ver os itens da categoria utilize `.cat id`', inline=False)
        await ctx.send(embed=embed)

@cat.command(name='0')
async def _bot(ctx):
    await ctx.send('Ainda em construção...')

@bot.command()
async def cid(ctx, city=None):
    if city is None:
        embed = discord.Embed(title="Cidades que atendemos", description="Segue a lista:", color=0xeee657)
        embed.add_field(name=cidades()[0], value="Não achou sua cidade? Nos informe, por gentileza! `.cid <nome da cidade>`", inline=False)
        embed.add_field(name=cidades()[1], value="Não achou sua cidade? Nos informe, por gentileza! `.cid <nome da cidade>`", inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Já enviamos a sua sugestão de cidade ({0}) para o Zé, blz?".format(city))	

@bot.command()
async def cls(ctx, msglimit=3):    
    deleted = await ctx.channel.purge(limit=msglimit)
    await ctx.send('Vou limpar minha bagunça!', delete_after=3.0)

@bot.command(pass_context=True)
async def dm(ctx):
    user = await bot.fetch_user(ctx.message.author.id)
    await user.send('Hey, tudo bem?')
    await user.send('Bora refrescar a garganta?')
    await user.send('Use o comando: ´.l´')
    await user.send('https://tenor.com/view/spongebob-squidward-soda-gif-13997581')
    await ctx.send("Oi {0.author.mention}, te mandei uma mensagem no privado.".format(ctx.message))

@bot.command(pass_context=True)
async def cad(ctx):
    if cadastro(str(ctx.message.author), True):
        await ctx.send('Você já é cadastrado, pode fazer seu pedido! Pode começar pelo `.l`')    
    else:
        await ctx.send('{0.author.mention}, vou te pedir uns dados no privado, ok?!'.format(ctx.message))
        user = await bot.fetch_user(ctx.message.author.id)
        await user.send('Hey, tudo bem? Vamos fazer seu cadastro?')
        await user.send('Me informe seu email:')
		
@bot.command(name='cheat')
async def _bot(ctx):    
    await ctx.send('Cheat é uma gíria utilizada por gamers para designar códigos e truques especiais durante o jogo.')
    await ctx.send('Sim, eu tenho alguns comandos secretos:')
    await ctx.send('Pode usar: .bot, .email, insta, .fusion, .heineken, .skol')
    await ctx.send('.bbs +: boa (tarde/noite), bom dia, heineken, lindo, game, hacka')

@bot.command(name='bot')
async def _bot(ctx):
    await ctx.send('Sim, eu sou um bot muito legal. \nVocê sabia que eu nasci dentro de um hacka? \nFui criado por 4 seres humanos: Jonatha Carlos, Olívia Boretti, Sebastião Neto e Uandisson Miranda.')
    await ctx.send('Visite nosso site: https://jonathacnb.github.io/bbsambev.github.io/')

@bot.command(name='email')
async def _bot(ctx):
    await ctx.send('Uhuul... tá na mão `@gmail.com`, ahhhh elogios, críticas e susgestões são bem vindos! ')

@bot.command(name='insta')
async def _bot(ctx):
    await ctx.send('Me segue lá @bbsbot.')

@bot.command(name='fusion')
async def _bot(ctx):
    await ctx.send('Melhor não há!')

@bot.command(name='heineken')
async def _bot(ctx):
    await ctx.send('Tá de brincadeira né? Vamos de Beck\'s!')

@bot.command(name='skol')
async def _bot(ctx):
    await ctx.send('A cerveja que desce redondo!')

@bot.group()
async def bbs(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("Oi {0.author.mention}, tudo bem?".format(ctx.message))
        await ctx.send('Bora refrescar a garganta?')
        await ctx.send('Use o comando: `.l`')
        await ctx.send('https://tenor.com/view/spongebob-squidward-soda-gif-13997581')
   
@bot.command(name='boa')
async def _bot(ctx, msg: str):
    user = await bot.fetch_user(ctx.message.author.id)
    await ctx.send('Oi {0.author.mention}, muito obrigado e pra vc tbm! Que tal deixar minha '.format(ctx.message) + msg + ' ainda melhor com um pedido?')

@bot.command(name='bom')
async def _bot(ctx, msg: str):
    user = await bot.fetch_user(ctx.message.author.id)
    await ctx.send('Oi {0.author.mention}, muito obrigado e pra vc tbm! Que tal deixar meu '.format(ctx.message) + msg + ' ainda melhor com um pedido?')

@bbs.command(name='heineken')
async def _bot(ctx):
    await ctx.send('Sim, temos Beck\'s.')

@bbs.command(name='lindo')
async def _bot(ctx):
    await ctx.send('São os seus olhos! Vamos fazer um pedido hoje?')

@bbs.command(name='game')
async def _bot(ctx):
    await ctx.send('Gosto de Call of Duty.')

@bbs.command(name='hacka')
async def _bot(ctx):
    await ctx.send('Desculpa, mas já tenho time!')

@bot.command(name='l')
async def _bot(ctx):
    lista = catalogo()
    
    x = 0
    for prd in lista:

        embed=discord.Embed(title="Id: #"+ str(x), description="Produto: " + prd[0], color=0x0429e7)
        embed.add_field(name="R$ ", value=prd[2], inline=False)
        embed.set_thumbnail(url=prd[1])
        await ctx.send(embed=embed)
        x+=1
    
    embed = discord.Embed(title="Faça seu pedido", description=".add <id>") #,color=Hex code
    embed.add_field(name="Exemplo: ", value="Eu gostaria de adicionar o item #10 (`.add 10`)")
    await ctx.send(embed=embed)

@bot.command(name='add')
async def _bot(ctx, choices: str):
    await ctx.send('Item: {0} adicionado com sucesso!'.format(choices))

@bot.command(name='t')
async def _bot(ctx):    
    await ctx.send('(+) Itens: R$ {0}'.format('5,00') + '\n(+) Frete: R$ {0}'.format('2,00') + '\n(=) Total: R$ 7,00' )

@bot.command(name='p')
async def _bot(ctx):
    await ctx.send('Pedido realizado com sucesso: Total: R$ 7,00')
    await ctx.send('Já pedi para meu amigo Zé Delivery fazer sua entrega, blz? :iphone: :map: ')

@bot.command(name='r')
async def _bot(ctx):
    await ctx.send('Zé, tu tá por onde meu amigo? :iphone: :map: ')
    await ctx.send('Opa, o Zé, me falou que já está na esquina da sua rua, em 2 min chega aí. :partying_face: :punch:')




bot.run()
