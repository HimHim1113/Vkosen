from discord.ext import commands # Bot Commands Frameworkのインポート
import random

# コグとして用いるクラスを定義。
class GatyaCog(commands.Cog):

    # TestCogクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        random.seed()
        self.bot = bot

    # コマンドの作成。コマンドはcommandデコレータで必ず修飾する。
    @commands.command()
    async def gatya(self, ctx):
        '''V高専がチャを回す'''
        rarity = ['N  ', 'R  ', 'SR', 'UR']
        gat = []
        gat.append(['秋風御礼', '浅浪沫', '雨下青猫', 'あんかるむ', '絵村千咲', '音無りんこ', '神爪しお', '神爪緑', '夏眠', '如月璃音', '北川茜', '西行響希', '空辺飛狐', '敷島佑斗', '辞典', '霜暮黒夢', '春眠', '単位パン', '千早旅兎', '九十九零', '鉄城大和', '冬眠', '泡影布目', 'モブヶ崎モブ夫', '山吹勇麻', '雪野冬磨'])
<<<<<<< HEAD
        gat.append(['【フェットチーネ】秋風御礼', '【素材】浅浪沫', '【ﾐ"ｯ】雨下青猫', '【未実装】あんかるむ', '【未実装】絵村千咲', '【未実装】音無りんこ', '【未実装】神爪しお', '【未実装】神爪緑', '【トッポ】夏眠', '【サーバー購入】如月璃音', '【未実装】北川茜', '【bot開発】西行響希', '【飛行中】空辺飛狐', '【未実装】敷島佑斗', '【炎上】辞典', '【未実装】霜暮黒夢', '【求婚】春眠', '【未実装】単位パン', '【未実装】千早旅兎', '【歌ってみた】九十九零', '【パソコン修理】鉄城大和', '【未実装】冬眠', '【男の娘】泡影布目', '【モブ】モブヶ崎モブ夫', '【配信中】山吹勇麻', '【二度寝】雪野冬磨'])
=======
        gat.append(['【フェットチーネ】秋風御礼', '【素材】浅浪沫', '【ﾐ"ｯ】雨下青猫', '【未実装】あんかるむ', '【未実装】絵村千咲', '【未実装】音無りんこ', '【未実装】神爪しお', '【未実装】神爪緑', '【トッポ】夏眠', '【サーバー購入】如月璃音', '【未実装】北川茜', '【bot開発】西行響希', '【飛行中】空辺飛狐', '【未実装】敷島佑斗', '【炎上】辞典', '【未実装】霜暮黒夢', '【未実装】春眠', '【未実装】単位パン', '【未実装】千早旅兎', '【歌ってみた】九十九零', '【パソコン修理】鉄城大和', '【未実装】冬眠', '【男の娘】泡影布目', '【モブ】モブヶ崎モブ夫', '【配信中】山吹勇麻', '【二度寝】雪野冬磨'])
>>>>>>> 432d3faa1027a87108dc46ea46cf431e25af2d43
        gat.append(['【未実装】秋風御礼', '【神】浅浪沫', '【未実装】雨下青猫', '【未実装】あんかるむ', '【未実装】絵村千咲', '【未実装】音無りんこ', '【未実装】神爪しお', '【未実装】神爪緑', '【未実装】夏眠', '【未実装】如月璃音', '【未実装】北川茜', '【未実装】西行響希', '【未実装】空辺飛狐', '【未実装】敷島佑斗', '【未実装】辞典', '【未実装】霜暮黒夢', '【未実装】春眠', '【未実装】単位パン', '【未実装】千早旅兎', '【未実装】九十九零', '【自衛隊員】鉄城大和', '【未実装】冬眠', '【未実装】泡影布目', '【未実装】モブヶ崎モブ夫', '【未実装】山吹勇麻', '【未実装】雪野冬磨'])
        gat.append(['chokudai', '高専花子', '七瀬真冬', '留年を告げる高専機構'])
        string = 'ガチャ結果\n'
        for i in range(10):
            rare = random.randrange(1000)
            if(rare < 600): rare = 0
            elif(rare < 900): rare = 1
            elif(rare < 995): rare = 2
            else: rare = 3
            if i == 10 - 1:
                if rare < 2: rare = 2
            res = random.randrange(len(gat[rare]))
            string += f'{rarity[rare]}：{gat[rare][res]}\n'
        await ctx.send(string)

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(GatyaCog(bot))
