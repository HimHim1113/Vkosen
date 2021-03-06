from discord.ext import commands
from googletrans import Translator

# コグとして用いるクラスを定義。
class TransCog(commands.Cog):

    # TestCogクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    # コマンドの作成。コマンドはcommandデコレータで必ず修飾する。
    @commands.command()
    async def trans(self, ctx, dst, *word): # 関数名=コマンド名
        '''翻訳[翻訳後言語、文]'''
        word = ' '.join(word)
        await ctx.send(f'{Translator().translate(word, dest=dst).text}')

    @commands.command()
    async def retrans(self, ctx, dst, *word): # 関数名=コマンド名
        '''翻訳[中間翻訳言語、文]'''
        word = ' '.join(word)
        src = Translator().detect(word).lang
        word = Translator().translate(word, dest=dst).text
        await ctx.send(f'{Translator().translate(word, dest=src).text}')

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(TransCog(bot))
