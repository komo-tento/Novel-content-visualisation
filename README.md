# Novel-content-visualisation
小説の文章の一節から360度画像を生成するためのシステムです

このシステムの作成にあたり、GPT-4のAPIとblockadelabsのSkyboxAIのAPIを使用しています。

そのため前もって.zshrcファイルに下記内容でAPIキーを記入してください。

```bash
# OpenAI APIキーの設定
export GPT_4_KEY="your-openai-api-key"
# SkyboxAI APIキーの設定
export SKYBOX_API_KEY="your-skybox-api-key"
```
の後、以下のコマンドを実行して .zshrc の内容を反映してください。
```bash
source ~/.zshrc
```

まず最初にpromptgen.pyを実行してください。

```bash
Python promptgen.py
```

その際にpromptgen.pyの下記部分のパスを画像作成したい小説のテキストファイルのパスに書き換えてください。
```bash
with open('your_book_path',mode='r',encoding='shift-jis') as f:
```

promptgen.pyを実行すると段落ごとに数字が割り振られた小説の内容とともに、『画像生成したい文章の番号を入力してください：』という文章が出力されるため、画像を生成したい段落番号を入力してください。

その後選択した文章をGPTが画像生成に適したプロンプトへ変換し、prompt.txtというファイル名で一律に保存されます。


prompt.txtのファイルが保存されたのを確認したら、index.jsを実行してください。
```bash
node index.js
```
実行するとServer listening at http://localhost:~という文章と下記画像のような文章が表示されます。
<img width="731" alt="スクリーンショット 2025-03-02 7 03 07" src="https://github.com/user-attachments/assets/db4ed016-6e8f-41cd-b48b-ff560a370890" />

画像内で数字とともに表示されているのはSkyboxAIで生成できる画風になります。

自分が生成したいと思う小説に合わせて画風の番号を選択してください。

画風を選択してしばらく待つと、http://localhost:~のリンク先に生成された360度画像がA-Frameを用いて球体状に展開されるはずです。
