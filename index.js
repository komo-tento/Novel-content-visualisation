const { BlockadeLabsSdk } = require('@blockadelabs/sdk');
const express = require('express');
const app = express();
const port = 3000;

app.use(express.static('public'));

let imageUrl = '';

const sdk = new BlockadeLabsSdk({
  api_key: process.env.SKYBOX_API_KEY,
});



const fs = require('fs');

const PROMPT = "./prompt.txt";

fs.readFile(PROMPT, 'utf8', async (err, data) => {
  if (err) {
    console.error('ファイルを読み込めませんでした:', err);
    return;
  }

  // someFunctionをfs.readFileの外に定義する
  async function someFunction(promptData) {
    console.log("kind of style ID[ 2:Fantasy 3:Anime 4:Surreal 5:Digital Painting 6:Radiant Realism 7:Nebula 9:Realism 10:SciFi 11:Dreamlike 13:Advanced(no style) 15:Interiors 16:Sky Dome 17:Dutch Masters 18:Infrared Photography 19:Low Poly Voxels 20:Kids CGI Animation 22:Watercolor 23:Technical Drawing 24:Pen & Ink 25:Manga 26:Modern Interiors 29:Cartoon 30:Storybook 31:Claymation 32:Vibrant Watercolor 33:Holographic 34:Stylized CGI Realism 35:Cyberpunk 36:Low Poly Triangles 37:Netrunner 40:Epic Digital Painting 41:Radiant Painting 42:Enchanted Painting 43:Art Mix 44:1960s Ethereal Fantasy 45:Data mosh 46:Mandala 47:Whimsical World 48:Psychedelic Illustration ]");

    const readline = require('readline').createInterface({
      input: process.stdin,
      output: process.stdout
    });

    readline.question('Which skybox_style_id to choose? ', async (answer) => {
      const STYLE_ID = parseInt(answer);
      readline.close();

      const generation = await sdk.generateSkybox({
        prompt: promptData,
        skybox_style_id: STYLE_ID,
      }).catch(error => {
        console.error('Error generating skybox:', error);
      });

      setTimeout(() => someFunction2(generation), 30000);
    });
  }
  // fs.readFileのコールバック内でsomeFunctionを呼び出す
  someFunction(data);
});

async function someFunction2(generation) {
    if (!generation || !generation.id) {
        console.error('Generation ID is not available.');
        return;
    }
    const imagineResult = await sdk.getImagineById({
        id: generation.id,
    });
    console.log(imagineResult.file_url);
    imageUrl = imagineResult.file_url;
}

app.get('/image-url', (req, res) => {
    res.json({ url: imageUrl });
});

app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});
