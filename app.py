import webbrowser
import time
import requests
from flask import *
import random as r
port_num = r.randint(1001,10000)
app=Flask(__name__)
print(f"PORT_NUM=={port_num}")

html1 = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    body {
        margin: 0;
        height: 100vh;
        display: flex;
		background-image: url("https://img.freepik.com/free-photo/illustration-cosmic-background-with-orange-neon-laser-lights_181624-19567.jpg?semt=ais_rp_50_assets&w=740&q=80");
		background-size: cover;
		background-repeat: no-repeat;
		background-position: center;
        justify-content: center; /* horizontal center */
        align-items: center;     /* vertical center */
    }
    
    form {
        text-align: center;
    }
    
    input {
        padding: 10px;
        font-size: 16px;
    }
    
    button {
        padding: 10px;
        margin-top: 10px;
    }
    </style>
    </head>
    
    <body>
    
<form method="POST">
    <input type="password" name="user_text" placeholder="Password"><br>
    <button type="submit">Submit</button>
</form>
    
    </body>
    </html>
        """

@app.route("/")
def cover():
    html="""
    <html>
    <body>
        <h1>Table Tennis: More Complex Than Tennis</h1>
        <p style="max-width:800px;">Many people think tennis is the harder sport because it takes place on a big court and requires a lot of running. However, table tennis is, in reality, much more complex and nuanced. It moves faster, depends on tricky ball spins, and demands sharper thinking. Even though it occurs on a small table, it pushes players’ reactions and minds to their absolute limits.</p>

        <p style="max-width:800px;">First, table tennis moves at a much faster pace than tennis. The International Table Tennis Federation (ITTF), the worldwide organization that governs the sport, explains that “a top-level rally can send the ball flying at more than 60 miles per hour across a nine-foot table” (ITTF, 2024). This statistic means that players have less than half a second to react to every shot. In contrast, tennis rallies happen on a much bigger court, so players generally have more time to prepare their movements and strategize their responses. Due to the smaller space and lightning-quick pace, table tennis effectively tests players' reaction time and precision in an unprecedented manner.</p>

        <p style="max-width:800px;">Second, the way spin operates in table tennis makes it significantly more difficult and intricate. A study conducted by researchers at the University of Sheffield, a well-known college in England, found that “even the smallest change in paddle angle can completely alter the ball’s direction or speed” (University of Sheffield, 2019). This means players must rapidly identify and respond to various spin types, such as topspin, backspin, sidespin, and everything in between, all within a fraction of a second. While tennis players also utilize spin, the heavier tennis ball makes the effect easier to predict and manage. In table tennis, these rapid spins create a dynamic that makes each rally unpredictable and skill-intensive, requiring players to possess a fine-tuned sense of awareness.</p>

        <p style="max-width:800px;">Third, table tennis requires not only strong physical abilities but also unwavering mental focus and quick strategic thinking. Sports Psychology Today, a respected magazine that studies how athletes think and react in intense competition, reports that “players must predict their opponent’s moves and respond instantly without time to plan between points” (Sports Psychology Today, 2022). Tennis players can take advantage of breaks between serves or rallies to think about their strategy; however, in table tennis, everything transpires at such a rapid speed that there is no time for extensive pauses to plan. This unique aspect compels players to remain mentally sharp, agile, and ready to adapt at all times.</p>

        <p style="max-width:800px;">Some people argue that tennis is harder due to the large court, which necessitates more endurance for long matches and rallies. Nevertheless, table tennis is, in fact, much more complex, relying extensively on explosive power and quick decision-making rather than just cardio endurance. It requires fast movements, advanced technical skills, and quick reflexes, placing greater pressure on brain coordination and split-second decision-making than tennis does. Therefore, while tennis is focused primarily on endurance, table tennis emphasizes skill and speed in a more pronounced way.</p>

        <p style="max-width:800px;">In conclusion, table tennis is undeniably more complex than tennis because it moves faster, demands precise control of spin, and requires faster mental decisions from the players. The organizations and studies that research table tennis clearly demonstrate just how advanced the sport truly is. So, the next time someone dismisses table tennis by calling it “just ping-pong,” challenge them to play a serious match. They’ll soon realize how fast, smart, and skillful you must be to truly succeed in the competitive world of table tennis.</p>

    </body>
    </html>
    """
    return html
@app.route("/Games",methods=["GET", "POST"])
def games():
    if request.method == "POST":
        user_input = request.form["user_text"]
        if user_input=="SCHOOLRULES":
            html = f"""
            <html>
			<head>
				<h1 style="color:lightblue">Welcome to</h1>
				<t style="color:lightblue">LUNAR</t>
			</head>
            <body style="background-image: url('https://img.freepik.com/free-photo/illustration-cosmic-background-with-orange-neon-laser-lights_181624-19567.jpg?semt=ais_rp_50_assets&w=740&q=80'); background-size: cover;">
                <p style="color: teal;">HOW TO USE:</p>
                <p style="color: teal;">To use this page click on the following:</p>
                <ul>
                    <li><a href="https://complete-python-3-bootcamp-1.onrender.com/BasketballStars"><img src="https://imgs.crazygames.com/games/basketball-stars-2019/cover-1583231506155.png?metadata=none&quality=100&width=1200&height=630&fit=crop"></a></li>
                    <li><a href="https://complete-python-3-bootcamp-1.onrender.com/DriveMad"><img src="https://drivemadgame.cc/uploads/games/main/img_68c3e328e0294.jpg"></a></li>
                    <li><a href="https://complete-python-3-bootcamp-1.onrender.com/RetroBowl"><img src="https://images.igdb.com/igdb/image/upload/t_cover_big_2x/co2mnn.jpg"></a></li>
                    <li><a href="https://complete-python-3-bootcamp-1.onrender.com/F.N.F_indie_cross"><img src="https://i.ytimg.com/vi/aicBBQJ0gHI/maxresdefault.jpg"></a></li>
                    <li><a href="https://complete-python-3-bootcamp-1.onrender.com/Time_Shooter"><img src="https://imgs.crazygames.com/time-shooter-3-swat_16x9/20241113103402/time-shooter-3-swat_16x9-cover?metadata=none&quality=100&width=1200&height=630&fit=crop"></a></li>
                    <li><a href="https://complete-python-3-bootcamp-1.onrender.com/Chicken_Wars"><img src="https://imgs.crazygames.com/chicken-cs_16x9/20241014081245/chicken-cs_16x9-cover?metadata=none&quality=100&width=1200&height=630&fit=crop"></a></li>
                    <li><a href="https://complete-python-3-bootcamp-1.onrender.com/Monkey_Mart"><img src="https://play-lh.googleusercontent.com/rWReIdyvDaYJPeOxn7hbC0b-96ixGpQKM_EndiQa3SUME8TtI_rNUcI4qsw5teK9mqk"></a></li>
                    <li><a href="https://complete-python-3-bootcamp-1.onrender.com/Stickman_Hook"><img src="https://stickhook.io/data/image/game/stick-hook-game1.png"></a></li>
                    <li><a href="https://complete-python-3-bootcamp-1.onrender.com/Minecraft"><img src="https://eaglercraft.com/img/Official_Minecraft_Trailer.webp"></a></li>
                    <li><a href="https://complete-python-3-bootcamp-1.onrender.com/War-of-Knight"><img src="https://citybrawl.com/data/image/war-the-knights-battle-arena-swords-3d.jpg"></a></li>
                    <li><a href="https://complete-python-3-bootcamp-1.onrender.com/CSGO"><img src="https://internet.medialities.org/wp-content/uploads/2024/02/07a83-csgo-operation-10-details-1.jpg?w=1024&h=576"></a></li>
                    <li><a href="https://complete-python-3-bootcamp-1.onrender.com/Robbery"><img src="https://tcf.admeen.org/game/18500/18435/400x246/bank-robbery.jpg"></a></li>
					<li><a href="https://complete-python-3-bootcamp-1.onrender.com/Friday_Night_Funking2"><img src="https://images.gamebanana.com/img/ss/mods/609480204201c.jpg"></a></li>
					<li><a href="https://complete-python-3-bootcamp-1.onrender.com/NMTR"><img src="https://juicybeast.com/press/knightmare_tower/images/kt_screenshot_00.png"></a></li>
					<li><a href="https://complete-python-3-bootcamp-1.onrender.com/FN"><img src="https://www.coolmathgames.com/sites/default/files/FruitNinja_OG-Logo.jpg"></a></li>
                </ul>
            </body>
            </html>"""
            return html
        else:
            pass
    return html1

@app.route("/Proxy", methods=["GET", "POST"])
def Proxy():

    html2 = """
<!DOCTYPE html>
<html>
<body style="background:black;color:white;text-align:center">

<form method="POST">
<input type="password" name="user_text" placeholder="Password"><br><br>
<input type="text" name="url" placeholder="example.com"><br><br>
<button type="submit">Submit</button>
</form>

</body>
</html>
"""

    if request.method == "POST":
        password = request.form.get("user_text")
        url = request.form.get("url")
        if password == "H#C3ER" and url:
            try:
                if not url.startswith("http"):
                    url = "https://" + url
                r = requests.get(url, verify=False, timeout=10)
                return r.text
            except Exception as e:
                return f"Proxy error: {e}"

    return html2

@app.route("/Info")
def info():
    html="""
    <h1>Welcome_To_Info</h1>
    <h3>This website is specifically designed to be for fun and so </h3>
    <h3>All I want to say is LET THE PLAY BEGIN!!!</h3>
    <p>Brought to you by:H#C3R</p>
    """
    return html

@app.route("/why")
def why():
	html="""
	<head>
		<t>Why?:</t>
	</head>
	<body>
		<p>These pages were made originaly to up my skills</p>
		<p>of coding python and HTML. But after a while I figured that</p>
		<p>other people could use cites like these so I made my</p>
		<p>project public.</p>
		<p>Thank you for listining<p>
		<p>Sincerly, H#C3ER
	</body>
	"""
	return html

@app.route("/BasketballStars")
def BasketballStars():
    html = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8" />
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="viewport" content="initial-scale=1, maximum-scale=1, user-scalable=no, shrink-to-fit=no" />
    <link rel="stylesheet" href="https://36043189-480959866522093217.preview.editmysite.com/uploads/b/139890129-743801889220072865/files/assets/css/app.css" type="text/css" />
    <title>Basketball Stars</title>

    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>

<body>
    <div id="content"></div>
    <div id="orientation"></div>
    <div id="loader">Loading ...</div>
    <script type="text/javascript" src="https://imasdk.googleapis.com/js/sdkloader/ima3.js"></script>

    <script type="text/javascript" src="https://36043189-480959866522093217.preview.editmysite.com/uploads/b/139890129-743801889220072865/files/assets/lib/nape.min.js">
        var nape ="nape.min.js";
    </script>

    <script type="text/javascript" src="https://36043189-480959866522093217.preview.editmysite.com/uploads/b/139890129-743801889220072865/files/assets/lib/jquery-3.1.1.min.js"></script>
    <script type="text/javascript" src="https://36043189-480959866522093217.preview.editmysite.com/uploads/b/139890129-743801889220072865/files/assets/lib/easeljs-0.8.2.combined.js"></script>
    <script type="text/javascript" src="https://36043189-480959866522093217.preview.editmysite.com/uploads/b/139890129-743801889220072865/files/assets/lib/bluebird.min.js"></script>
    <script type="text/javascript" src="https://36043189-480959866522093217.preview.editmysite.com/uploads/b/139890129-743801889220072865/files/assets/lib/phaser.min.js"></script>
    <script type="text/javascript" src="https://36043189-480959866522093217.preview.editmysite.com/uploads/b/139890129-743801889220072865/files/assets/lib/phaser-cachebuster.min.js"></script>
    <script type="text/javascript" src="https://36043189-480959866522093217.preview.editmysite.com/uploads/b/139890129-743801889220072865/files/assets/lib/phaser-super-storage.min.js"></script>
    <script type="text/javascript" src="https://36043189-480959866522093217.preview.editmysite.com/uploads/b/139890129-743801889220072865/files/assets/lib/dragonBones.min.js"></script>


    <script type="text/javascript">
        var notIE11 = (typeof (Event) ==='function');

        window.SDK_OPTIONS = {
            gameId: "ycc9yyyfyazoiibce061j1b7jx91tt8a",
            onEvent: function (event) {
                switch (event.name) {
                    case "SDK_GAME_START":
                        // advertisement done, resume game logic and unmute audio
                        var event;
                        if (notIE11) {
                            event = new Event("SDK_GAME_START");
                        } else {
                            event = document.createEvent('Event');
                            event.initEvent('SDK_GAME_START', true, true);
                        }
                        document.getElementById("content").dispatchEvent(event);
                        break;
                    case "SDK_GAME_PAUSE":
                        // pause game logic / mute audio
                        var event;
                        if (notIE11) {
                            event = new Event("SDK_GAME_PAUSE");
                        } else {
                            event = document.createEvent('Event');
                            event.initEvent('SDK_GAME_PAUSE', true, true);
                        }
                        document.getElementById("content").dispatchEvent(event);
                        break;
                    case "SDK_READY":
                        // this event is triggered when your user doesn't want personalised targeting of ads and such
                        console.log("SDK_READY");
                        break;
                }
            },
        };
        (function (a, b, c) {
            var d = a.getElementsByTagName(b)[0];
            a.getElementById(c) || (a = a.createElement(b), a.id = c, a.src ="https://cdn.jsdelivr.net/gh/st39/sdk@main/sdk.js", d.parentNode.insertBefore(a, d))
        })(document, "script", "gamemonetize-sdk"); 
    </script>
<script type="text/javascript" src="https://36043189-480959866522093217.preview.editmysite.com/uploads/b/139890129-743801889220072865/files/bs.min.js"></script></body>
<script src="https://cdn.jsdelivr.net/gh/st39/sdk@main/api.js"></script>
</html>


"""
    return html
@app.route("/DriveMad")
def DriveMad():
    html="""<!DOCTYPE html>
<html lang="en-us">


<head>
  <base href="https://cdn.jsdelivr.net/gh/genizy/dmad-poki@49b5ab6b987f5f3be58f9dae59c92e8fc1aab9b0/">
  <script>
  window.assgdd = {
    "ancestorOrigins": {
        "0": "https://games.poki.com",
        "1": "https://poki.com"
    },
    "href": "https://f9564e4e-ef25-4e4b-ba67-cb11a1576bbd.poki-gdn.com/cc1bc57a-e355-4696-97c2-097bf6188606/index.html?country=US&url_referrer=https%3A%2F%2Fpoki.com%2F&site_id=3&iso_lang=en&poki_url=https%3A%2F%2Fpoki.com%2Fen%2Fg%2Fdrive-mad&hoist=yes&nonPersonalized=n&cloudsavegames=n&familyFriendly=n&categories=78%2C93%2C96%2C103%2C377%2C390%2C400%2C893%2C929%2C1126%2C1139%2C1140%2C1141%2C1143%2C1147%2C1163%2C1185%2C1190%2C1193%2C1197&special_condition=landing&game_id=f9564e4e-ef25-4e4b-ba67-cb11a1576bbd&game_version_id=cc1bc57a-e355-4696-97c2-097bf6188606&inspector=0",
    "origin": "https://f9564e4e-ef25-4e4b-ba67-cb11a1576bbd.poki-gdn.com",
    "protocol": "https:",
    "host": "f9564e4e-ef25-4e4b-ba67-cb11a1576bbd.poki-gdn.com",
    "hostname": "f9564e4e-ef25-4e4b-ba67-cb11a1576bbd.poki-gdn.com",
    "port": "",
    "pathname": "/cc1bc57a-e355-4696-97c2-097bf6188606/index.html",
    "search": "?country=US&url_referrer=https%3A%2F%2Fpoki.com%2F&site_id=3&iso_lang=en&poki_url=https%3A%2F%2Fpoki.com%2Fen%2Fg%2Fdrive-mad&hoist=yes&nonPersonalized=n&cloudsavegames=n&familyFriendly=n&categories=78%2C93%2C96%2C103%2C377%2C390%2C400%2C893%2C929%2C1126%2C1139%2C1140%2C1141%2C1143%2C1147%2C1163%2C1185%2C1190%2C1193%2C1197&special_condition=landing&game_id=f9564e4e-ef25-4e4b-ba67-cb11a1576bbd&game_version_id=cc1bc57a-e355-4696-97c2-097bf6188606&inspector=0",
    "hash": ""
}
  </script>
  <meta charset="utf-8">
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">


  <title>Drive Mad</title>
  <meta name="description" content="">
  <meta name="google" content="notranslate">


  <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
  <link rel="stylesheet" href="webapp/fancade.css">
  <link rel="icon" href="webapp/favicon.ico">


  <!-- POKI SDK -->
  <script src="poki-sdk.js" ></script>
</head>


<body id="body">


  <!-- Modal dialog div -->
  <div id="modal_parent">
    <div id="modal_content">
      <span id="modal_close_button">&times;</span>
      <div id="store_link_modal_content" class="modal_inner"></div>
      <div id="share_file_modal_content" class="modal_inner"></div>
    </div>
  </div>


  <!--
      Game canvas and overlay. Emscripten makes some assumptions about how the canvas is positioned in order
      to translate document to game coordinates
    -->
  <div id="canvas_border" class="emscripten_border">
    <div id="play_content" class="middle center">
      <div class="edge">
        <div class="box">
          <div class="black">
            <img src="webapp/cover.jpg" class="cover">
            <p class="title">Drive Mad</p>
            <p class="author">Fancade</p>
          </div>
        </div>
      </div>
      <div id="progress_or_play">
        <progress id="progress" class="loading" value="0" max="100"></progress>
      </div>
      <p class="description"></p>
    </div>
    <canvas class="emscripten" id="canvas" tabindex=-1>
    </canvas>
    <div id="gradient"></div>
    <div id="webview_content"></div>
  </div>


  <!-- Manual JS, Called from WASM -->
  <script type="text/javascript" src="webapp/source_min.js"></script>


  <!-- Auto generated JS -->
  <script type="text/javascript" src="webapp/index.js"></script>
</body>


</html>
"""
    return html
@app.route("/RetroBowl")
def RetroBowl():
    html="""<!DOCTYPE html>


<!-- Ultimate Game Stash file--> 
<!-- For the regularly updating doc go to https://docs.google.com/document/d/1_FmH3BlSBQI7FGgAQL59-ZPe8eCxs35wel6JUyVaG8Q/ -->



<html lang="en">
  <head> 
    <base href="https://cdn.jsdelivr.net/gh/selenite-cc/selenite-old@9c743188888af0986c8c7b293dbac8f9e421a4ee/retrobowl/">
 <link rel="icon" type="image/x-icon" href="retrobowl.ico" />
 <script src="/js/all.js"></script>

    <!-- Generated by GameMaker:Studio http://www.yoyogames.com/gamemaker/studio -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta http-equiv="pragma" content="no-cache" />
    <meta name="apple-mobile-web-app-capable" content="yes" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0"
    />
    <meta
      name="apple-mobile-web-app-status-bar-style"
      content="black-translucent"
    />
    <meta charset="utf-8" />

    <!-- Set the title bar of the page -->
    <title>Retro Bowl</title>

    <!-- Set the background colour of the document -->
    <style>
      body {
        background: #000;
        color: #cccccc;
        margin: 0px;
        padding: 0px;
        border: 0px;
      }
      canvas {
        image-rendering: optimizeSpeed;
        -webkit-interpolation-mode: nearest-neighbor;
        -ms-touch-action: none;
        margin: 0px;
        padding: 0px;
        border: 0px;
      }
      :-webkit-full-screen #canvas {
        width: 100%;
        height: 100%;
      }
      div.gm4html5_div_class {
        margin: 0px;
        padding: 0px;
        border: 0px;
      }
      /* START - Login Dialog Box */
      div.gm4html5_login {
        padding: 20px;
        position: absolute;
        border: solid 2px #000000;
        background-color: #404040;
        color: #00ff00;
        border-radius: 15px;
        box-shadow: #101010 20px 20px 40px;
      }
      div.gm4html5_cancel_button {
        float: right;
      }
      div.gm4html5_login_button {
        float: left;
      }
      div.gm4html5_login_header {
        text-align: center;
      }
      /* END - Login Dialog Box */
      :-webkit-full-screen {
        width: 100%;
        height: 100%;
      }
    </style>
  </head>

  <body>
    <div class="gm4html5_div_class" id="gm4html5_div_id">
      <img
        src="html5game/splash.png"
        id="GM4HTML5_loadingscreen"
        alt="GameMaker:HTML5 loading screen"
        style="display: none"
      />
      <!-- Create the canvas element the game draws to -->
      <canvas id="canvas" width="960" height="540">
        <p>Your browser doesn't support HTML5 canvas.</p>
      </canvas>
    </div>

    <!-- Run the game code -->
    <script
      type="text/javascript"
      src="html5game/RetroBowl.js?WAEAC=1633155445"
    ></script>
    <script>
      window.onload = GameMaker_Init;
    </script>
  <script src="/html/settings/js/index.js"></script> 
   </body>
</html>

"""
    return html
@app.route("/F.N.F_indie_cross")
def indie_cross():
    html="""<!DOCTYPE html>


<!-- Ultimate Game Stash file--> 
<!-- For the regularly updating doc go to https://docs.google.com/document/d/1_FmH3BlSBQI7FGgAQL59-ZPe8eCxs35wel6JUyVaG8Q/ -->


<html lang="en">in

<head>

  <meta charset="utf-8">

  <title>Indie Cross</title>

  <meta id="viewport" name="viewport"
    content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <meta name="apple-mobile-web-app-capable" content="yes">
  <base href="https://cdn.jsdelivr.net/gh/waycrosspublicmedia/fnfmods/indie/">

  <link rel="shortcut icon" type="image/png" href="./favicon.png">

  <script type="text/javascript" src="./indie.js"></script>

  <script>
    window.addEventListener("touchmove", function (event) { event.preventDefault(); }, { capture: false, passive: false });
    if (typeof window.devicePixelRatio != 'undefined' && window.devicePixelRatio > 2) {
      var meta = document.getElementById("viewport");
      meta.setAttribute('content', 'width=device-width, initial-scale=' + (2 / window.devicePixelRatio) + ', user-scalable=no');
    }
    window.addEventListener("keydown", function (e) { if (["Tab", "Space", "ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"].indexOf(e.code) > -1) { e.preventDefault(); } }, false);
  </script>

  <style>
    html,
    body {
      margin: 0;
      padding: 0;
      height: 100%;
      overflow: hidden;
    }

    #openfl-content {
      background: #000000;
      width: 100%;
      height: 100%;
    }

    @font-face {
      font-family: 'Pixel Arial 11 Bold';
      src: url('assets/fonts/pixel.eot?#iefix') format('embedded-opentype'),
        url('assets/fonts/pixel.woff') format('woff'),
        url('assets/fonts/pixel.otf') format('truetype');
      font-weight: normal;
      font-style: normal;
    }

    @font-face {
      font-family: 'VCR OSD Mono';
      src: url('assets/fonts/vcr.eot?#iefix') format('embedded-opentype'),
        url('assets/fonts/vcr.woff') format('woff'),
        url('assets/fonts/vcr.ttf') format('truetype'),
        url('assets/fonts/vcr.svg#VCR%20OSD%20Mono') format('svg');
      font-weight: normal;
      font-style: normal;
    }

    @font-face {
      font-family: 'Nokia Cellphone FC Small';
      src: url('flixel/fonts/nokiafc22.eot?#iefix') format('embedded-opentype'),
        url('flixel/fonts/nokiafc22.woff') format('woff'),
        url('flixel/fonts/nokiafc22.ttf') format('truetype'),
        url('flixel/fonts/nokiafc22.svg#Nokia%20Cellphone%20FC%20Small') format('svg');
      font-weight: normal;
      font-style: normal;
    }

    @font-face {
      font-family: 'Monsterrat';
      src: url('flixel/fonts/monsterrat.eot?#iefix') format('embedded-opentype'),
        url('flixel/fonts/monsterrat.woff') format('woff'),
        url('flixel/fonts/monsterrat.ttf') format('truetype'),
        url('flixel/fonts/monsterrat.svg#Monsterrat') format('svg');
      font-weight: normal;
      font-style: normal;
    }
  </style>

</head>

<body>
  <noscript>This webpage makes extensive use of JavaScript. Please enable JavaScript in your web browser to view this page.</noscript>
  <div id="openfl-content"></div>
  <script type="text/javascript">
    lime.embed("indie", "openfl-content", 1280, 720, { parameters: {} });
  </script>
</body>

</html>
"""
    return html

@app.route("/Polytrack")
def polytrack():
    html="""<!DOCTYPE html>


<!-- Ultimate Game Stash file-->
<!-- For the regularly updating doc go to https://docs.google.com/document/d/1_FmH3BlSBQI7FGgAQL59-ZPe8eCxs35wel6JUyVaG8Q/ -->





<html>

<head>
  <base href="https://cdn.jsdelivr.net/gh/genizy/polytrack@main/">
  <script>
    window.jkdfgnjkndfg = document.querySelector('base').href;
    fetch("simulation_worker.bundle.js").then(res => res.text()).then(text => {
      const blob = new Blob([text.replaceAll("replacethisplease", window.jkdfgnjkndfg)], { type: 'application/javascript' });
      window.simulationworker = URL.createObjectURL(blob);
    });
    const ogworker = window.Worker;
    window.Worker = function (scripturl, options) {
      if (typeof scripturl === 'string' && scripturl.toLowerCase() === "simulation_worker.bundle.js") {
        scripturl = window.simulationworker;
      }
      return new ogworker(scripturl, options);
    };
    window.Worker.prototype = ogworker.prototype;

    const ogfetch = window.fetch;
    window.fetch = async function (input, init) {
      if (typeof input === "string") {
        input = input.replace("vps.kodub.com:43273", "vpskodub.tmena1565.workers.dev");
      } else if (input instanceof Request) {
        const newUrl = input.url.replace("vps.kodub.com:43273", "vpskodub.tmena1565.workers.dev");
        input = new Request(newUrl, input);
      }
      return ogfetch(input, init);
    };

    const ogxml = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function (method, url, ...rest) {
      if (typeof url === "string") {
        url = url.replace("vps.kodub.com:43273", "vpskodub.tmena1565.workers.dev");
      }
      return ogxml.call(this, method, url, ...rest);
    };
  </script>
  <link rel="manifest" href="manifest.json" />
  <meta name="viewport"
    content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1, user-scalable=no">
</head>

<body>
  <canvas id="screen"></canvas>
  <div id="ui"></div>
  <div id="transition-layer"></div>

  <script type="module" src="main.bundle.js" defer></script>
</body>

</html>

"""
    return html

@app.route("/Time_Shooter")
def time_Shooter():
    html = """

<Module>


<!-- Ultimate Game Stash file--> 
<!-- For the regularly updating doc go to https://docs.google.com/document/d/1_FmH3BlSBQI7FGgAQL59-ZPe8eCxs35wel6JUyVaG8Q/ -->


</style><style type="text/css">#button {
  display:none;
}
.imgb_vis {
  animation: imgb-animation 7s linear;
}
@keyframes imgb-animation {
  10% {
    transform: translateX(0);
  }
  20% {
    transform: translateX(100px);
  }
  90% {
    transform: translateX(100px);
  }
  100% {
    transform: translateX(0);
  }
}</style></head><body class="dark" dir="ltr">
    <div class="unity-desktop" id="unity-container">
      <canvas id="unity-canvas" style="background: url(&quot;https://cdn.jsdelivr.net/gh/mistirk/google@eebffdf79a14f6e01e153d5cd4bed23c432874fb/version/time-s3/ts3.jpg&quot;) center center / cover;"></canvas>
    </div>
    <div id="loading-cover" style="">
      <div id="unity-loading-bar">
        <div id="unity-logo"><img src="https://cdn.jsdelivr.net/gh/mistirk/google@eebffdf79a14f6e01e153d5cd4bed23c432874fb/version/time-s3/logo.png"></div>
        <div id="unity-progress-bar-empty" style="">
          <div id="unity-progress-bar-full" style="width: 30%;"></div>
        </div>
        <div class="spinner" style="display: none;"></div>
      </div>
    </div>
    <div id="unity-fullscreen-button" style="display: none;"></div>
    <script>
      const hideFullScreenButton = "1";
      const buildUrl = "https://cdn.jsdelivr.net/gh/mistirk/google@eebffdf79a14f6e01e153d5cd4bed23c432874fb/version/time-s3";
      const loaderUrl = buildUrl + "/ts3.loader.js";
      const config = {
        dataUrl: buildUrl + "/ts3.data",
        frameworkUrl: buildUrl + "/ts3.framework.js",
        codeUrl: buildUrl + "/ts3.wasm",
        streamingAssetsUrl: "StreamingAssets",
        companyName: "GoGoMan",
        productName: "Time Shooter SWAT",
        productVersion: "0.03",
      };

      const container = document.querySelector("#unity-container");
      const canvas = document.querySelector("#unity-canvas");
      const loadingCover = document.querySelector("#loading-cover");
      const progressBarEmpty = document.querySelector("#unity-progress-bar-empty");
      const progressBarFull = document.querySelector("#unity-progress-bar-full");
      const fullscreenButton = document.querySelector("#unity-fullscreen-button");
      const spinner = document.querySelector('.spinner');

      const canFullscreen = (function() {
        for (const key of [
            'exitFullscreen',
            'webkitExitFullscreen',
            'webkitCancelFullScreen',
            'mozCancelFullScreen',
            'msExitFullscreen',
          ]) {
          if (key in document) {
            return true;
          }
        }
        return false;
      }());

      if (/iPhone|iPad|iPod|Android/i.test(navigator.userAgent)) {
        container.className = "unity-mobile";
        config.devicePixelRatio = 1;
      }
      canvas.style.background = "url('" + buildUrl + "/ts3.jpg') center / cover";
      loadingCover.style.display = "";

      const script = document.createElement("script");
      script.src = loaderUrl;
      script.onload = () => {
        createUnityInstance(canvas, config, (progress) => {
          spinner.style.display = "none";
          progressBarEmpty.style.display = "";
          progressBarFull.style.width = `${100 * progress}%`;
        }).then((unityInstance) => {
          loadingCover.style.display = "none";
          if (canFullscreen) {
            if (!hideFullScreenButton) {
              fullscreenButton.style.display = "";
            }
            fullscreenButton.onclick = () => {
              unityInstance.SetFullscreen(1);
            };
          }
        }).catch((message) => {
          alert(message);
        });
      };
      document.body.appendChild(script);
    </script><script src="https://cdn.jsdelivr.net/gh/mistirk/google@eebffdf79a14f6e01e153d5cd4bed23c432874fb/version/time-s3/ts3.loader.js"></script>
	<script src=""></script>
  

<script src="blob:https://images-opensocial.googleusercontent.com/9bedc84f-f80b-4566-a8cb-b9cec3dd5acb"></script></body></html>
</script><link href="https://cdn.jsdelivr.net/gh/mistirk/google@eebffdf79a14f6e01e153d5cd4bed23c432874fb/version/time-s3/style.css" rel="stylesheet">
    <meta charset="utf-8">
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type">
    <meta content="width=device-width, initial-scale=1.0, user-scalable=no" name="viewport">
    <title>Time Shooter 3 SWAT</title>
    
  <script>

"""
    return html

@app.route("/Chicken_Wars")
def CW():
    html="""
<!-- Ultimate Game Stash file--> 
<!-- For the regularly updating doc go to https://docs.google.com/document/d/1_FmH3BlSBQI7FGgAQL59-ZPe8eCxs35wel6JUyVaG8Q/ -->


</script><script>gadgets.Prefs.setMessages_({});gadgets.Prefs.setDefaultPrefs_({});gadgets.io.preloaded_=[];</script><style>html{box-sizing:border-box}*,*:before,*:after{box-sizing:inherit}html,body{height:100%}canvas{display:block}body{margin:0}#unity-container{width:100%;height:100%;position:relative}#unity-canvas{width:100%;height:100%;background:#231F20}#loading-cover{position:absolute;top:0;left:0;width:100%;height:100%;display:flex;justify-content:center;align-items:center}#unity-loading-bar{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;align-items:center}#unity-logo{text-align:center}#unity-logo img{max-width:80%;max-height:80%}#unity-progress-bar-empty{width:40%;height:24px;margin:10px 20px 20px 10px;text-align:left;border:1px solid white;padding:2px}#unity-progress-bar-full{width:0;height:100%;background:white}.light #unity-progress-bar-empty{border-color:black}.light #unity-progress-bar-full{background:black}.spinner,.spinner:after{border-radius:50%;width:5em;height:5em}.spinner{margin:10px;font-size:10px;position:relative;text-indent:-9999em;border-top:1.1em solid rgba(255,255,255,0.2);border-right:1.1em solid rgba(255,255,255,0.2);border-bottom:1.1em solid rgba(255,255,255,0.2);border-left:1.1em solid #ffffff;transform:translateZ(0);animation:spinner-spin 1.1s infinite linear}@keyframes spinner-spin{0%{transform:rotate(0deg)} 100%{transform:rotate(360deg)}}</style><style> body{overflow:hidden;-webkit-touch-callout:none;-webkit-user-select:none;-khtml-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-tap-highlight-color:rgba(0,0,0,0)}</style>
<meta charset="utf-8">
<meta content="text/html; charset=utf-8" http-equiv="Content-Type">
<meta content="width=device-width, initial-scale=1.0, user-scalable=no" name="viewport">


<script>
/* mp-start */

var _params = gadgets.util.getUrlParameters();
if (_params['exp_rpc_js'] != 1) {
  var url = _params['parent'] + '/ig/ifpc_relay';
  gadgets.rpc.setRelayUrl('..', url, true);
}
/* mp-end */
</script><style type="text/css" id="operaUserStyle">
  display:none;
}
.imgb_vis {
  animation: imgb-animation 7s linear;
}
@keyframes imgb-animation {
  10% {
    transform: translateX(0);
  }
  20% {
    transform: translateX(100px);
  }
  90% {
    transform: translateX(100px);
  }
  100% {
    transform: translateX(0);
  }
}</style><meta http-equiv="origin-trial" content="A9AxgGSwmnfgzzkyJHILUr3H8nJ/3D+57oAsL4DBt4USlng4jZ0weq+fZtHC/Qwwn6gd4QSa5DzT3OBif+kXVA0AAAB4eyJvcmlnaW4iOiJodHRwczovL2ltYXNkay5nb29nbGVhcGlzLmNvbTo0NDMiLCJmZWF0dXJlIjoiUHJpdmFjeVNhbmRib3hBZHNBUElzIiwiZXhwaXJ5IjoxNjk1MTY3OTk5LCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="AlK2UR5SkAlj8jjdEc9p3F3xuFYlF6LYjAML3EOqw1g26eCwWPjdmecULvBH5MVPoqKYrOfPhYVL71xAXI1IBQoAAAB8eyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3NTgwNjcxOTksImlzU3ViZG9tYWluIjp0cnVlfQ=="></head><body class="dark" dir="ltr">
<div class="unity-desktop" id="unity-container">
<canvas id="unity-canvas" style="cursor: default;" width="1117" height="926"></canvas>
</div>
<div id="loading-cover" style="display: none;">
<div id="unity-loading-bar">
<div id="unity-progress-bar-empty" style="">
<div id="unity-progress-bar-full" style="width: 100%;"></div>
</div>
<div class="spinner" style="display: none;"></div>
</div>
</div>
<script>
const hideFullScreenButton="";const buildUrl="https://cdn.jsdelivr.net/gh/SternyFahizh/RabbitMQ@cd18b31ab1e3aecd797970d11f94fd4eb921813d/ruby/ch-3";const loaderUrl=buildUrl+"/load.js";const config={dataUrl:buildUrl+"/ce.data.js",frameworkUrl:buildUrl+"/ce.framework.js",codeUrl:buildUrl+"/ce.wasm.js",streamingAssetsUrl:"",};const container=document.querySelector("#unity-container");const canvas=document.querySelector("#unity-canvas");const loadingCover=document.querySelector("#loading-cover");const progressBarEmpty=document.querySelector("#unity-progress-bar-empty");const progressBarFull=document.querySelector("#unity-progress-bar-full");const spinner=document.querySelector('.spinner');const canFullscreen=(function(){for(const key of['exitFullscreen','webkitExitFullscreen','webkitCancelFullScreen','mozCancelFullScreen','msExitFullscreen',]){if(key in document){return true}}return false}());if(/iPhone|iPad|iPod|Android/i.test(navigator.userAgent)){container.className="unity-mobile"}loadingCover.style.display="";canvas.addEventListener("touchstart",()=>{window.focus()});canvas.addEventListener("pointerdown",()=>{window.focus()});let player;let leaderboard;let myGameInstance=null;let payments=null;let promptCanShow=false;let reviewCanShow=false;let initSDK=true;let initGame=true;let photoSizeForInit;let scopesForInit;let nowFullAdOpen=false;let letGameReadyApi=true;let ysdk=null;const script=document.createElement("script");script.src=loaderUrl;script.onload=()=>{createUnityInstance(canvas,config,(progress)=>{spinner.style.display="none";progressBarEmpty.style.display="";progressBarFull.style.width=`${100*progress}%`}).then((unityInstance)=>{myGameInstance=unityInstance;loadingCover.style.display="none"}).catch((message)=>{})};var playerData='noData';var environmentData='null';var cloudSaves='noData';function InitSDK(photoSize,scopes){console.log('Init GAME');initGame=true;photoSizeForInit=photoSize;scopesForInit=scopes;InitPlayer(photoSize,scopes)}
function InitGame(photoSize,scopes,gameReadyApi){console.log('Init GAME');initGame=true;photoSizeForInit=photoSize;scopesForInit=scopes;if(initSDK==true){if(gameReadyApi==true)GameReadyAPI();InitPlayer(photoSize,scopes)}else{InitYandex();setTimeout(function(){if(!initSDK){console.error('CRASH InitYandex');NotAuthorized()}},1000)}if(nowFullAdOpen==true){myGameInstance.SendMessage('YandexGame','OpenFullAd')}} 
function GameReadyAPI(){if(letGameReadyApi){}}function NotAuthorized(){try{console.log('Authorized failed');let authJson={"playerAuth":"rejected","playerName":"unauthorized","playerId":"unauthorized","playerPhoto":"null"};myGameInstance.SendMessage('YandexGame','SetInitializationSDK',JSON.stringify(authJson))}catch(e){console.error('CRASH Not Authorized: ',e.message)}}function InitPlayer(photoSize,_scopes){NotAuthorized();window.focus()}function OpenAuthDialog(photoSize,scopes){try{ysdk.auth.openAuthDialog().then(()=>{InitPlayer(photoSize,scopes)}).catch(()=>{InitSDK(photoSize,scopes)})}catch(e){console.log('CRASH Open Auth Dialog: ',e.message)}}
function FullAdShow(){try{window.ysdk.adv.showFullscreenAdv({callbacks:{onOpen:()=>{console.log('Open Fullscreen Ad');nowFullAdOpen=true;if(initGame===true)myGameInstance.SendMessage('YandexGame','OpenFullAd')},onClose:(wasShown)=>{nowFullAdOpen=false;if(initGame===true){if(wasShown){myGameInstance.SendMessage('YandexGame','CloseFullAd','true')}else{myGameInstance.SendMessage('YandexGame','CloseFullAd','false')}}window.focus()},onError:(error)=>{console.error('Error Fullscreen Ad',error);myGameInstance.SendMessage('YandexGame','ErrorFullAd');window.focus()}}})}catch(e){console.error('CRASH FullAd Show: ',e.message)}}
function RewardedShow(id){try{window.ysdk.adv.showRewardedVideo({callbacks:{onOpen:()=>{console.log('Opened Video Ad. Id: '+id);myGameInstance.SendMessage('YandexGame','OpenVideo')},onClose:()=>{console.log('Closed Video Ad. Id: '+id);myGameInstance.SendMessage('YandexGame','CloseVideo');window.focus()},onRewarded:()=>{console.log('Reward Video Ad. Id: '+id);myGameInstance.SendMessage('YandexGame','RewardVideo',id)},onError:(e)=>{console.error('Error Video Ad. Id: '+id,e);myGameInstance.SendMessage('YandexGame','ErrorVideo')}}})}catch(err){console.error('CRASH Rewarded Video Ad Show: ',err.message)}}
function StickyAdActivity(show){try{ysdk.adv.getBannerAdvStatus().then(({stickyAdvIsShowing,reason})=>{if(stickyAdvIsShowing){if(!show){ysdk.adv.hideBannerAdv()}}else if(reason){console.log('Sticky ad are not shown. Reason:',reason)}else if(show){ysdk.adv.showBannerAdv()}})}catch(e){console.error('CRASH Sticky Activity: ',e.message)}}
function InitPayments(){try{ysdk.getPayments().then(_payments=>{console.log('Purchases are available');payments=_payments}).catch(e=>{console.log('Purchases are not available',e.message)})}catch(e){console.error('CRASH Init Payments: ',e.message)}}
function BuyPayments(id){try{if(payments!=null){payments.purchase(id).then(()=>{console.log('Purchase Success');ConsumePurchase(id);window.focus()}).catch(e=>{console.error('Purchase Failed',e.message);myGameInstance.SendMessage('YandexGame','OnPurchaseFailed',id);window.focus()})}else{console.log('Payments == null')}}catch(e){console.error('CRASH Buy Payments: ',e.message);window.focus()}}
function GetPayments(){try{if(payments!=null){payments.getCatalog().then(products=>{let productID=[];let title=[];let description=[];let imageURI=[];let priceValue=[];let consumed=[];payments.getPurchases().then(purchases=>{for(let i=0;i<products.length;i++){productID[i]=products[i].id;title[i]=products[i].title;description[i]=products[i].description;imageURI[i]=products[i].imageURI;priceValue[i]=products[i].priceValue;consumed[i]=true;for(i2=0;i2<purchases.length;i2++){if(purchases[i2].productID===productID[i]){consumed[i]=false;break}}}let jsonPayments={"id":productID,"title":title,"description":description,"imageURI":imageURI,"priceValue":priceValue,"consumed":consumed};myGameInstance.SendMessage('YandexGame','PaymentsEntries',JSON.stringify(jsonPayments))})})}else{console.log('Get Payments: payments == null')}}catch(e){console.error('CRASH Get Payments: ',e.message)}}
function ConsumePurchase(id){try{if(payments!=null){payments.getPurchases().then(purchases=>{for(i=0;i<purchases.length;i++){if(purchases[i].productID===id){payments.consumePurchase(purchases[i].purchaseToken);myGameInstance.SendMessage('YandexGame','OnPurchaseSuccess',id)}}})}else console.log('Consume purchase: payments null')}catch(e){console.error('CRASH Consume Purchase: ',e.message)}}
function ConsumePurchases(){try{if(payments!=null){payments.getPurchases().then(purchases=>{console.log('Unprocessed purchases: ',purchases.length);for(i=0;i<purchases.length;i++){payments.consumePurchase(purchases[i].purchaseToken);myGameInstance.SendMessage('YandexGame','OnPurchaseSuccess',purchases[i].productID)}})}else console.log('Consume purchases: payments null')}catch(e){console.error('CRASH Consume purchases: ',e.message)}}
function SaveCloud(jsonData,flush){try{player.setData({saves:[jsonData],},flush)}catch(e){console.error('CRASH Save Cloud: ',e.message)}}function LoadCloud(){try{player.getData(["saves"]).then(data=>{if(data.saves){myGameInstance.SendMessage('YandexGame','SetLoadSaves',JSON.stringify(data.saves))}else{myGameInstance.SendMessage('YandexGame','SetLoadSaves',"noData")}}).catch(()=>{console.error('getData Error!');myGameInstance.SendMessage('YandexGame','SetLoadSaves',"noData")})}catch(e){console.error('CRASH Load saves Cloud: ',e.message);myGameInstance.SendMessage('YandexGame','SetLoadSaves',"noData")}}
            function InitLeaderboard() {
                try {
                    ysdk.getLeaderboards().then(_lb => {
                        leaderboard = _lb
                        myGameInstance.SendMessage('YandexGame', 'InitializedLB');
                    });
                } catch (e) {
                    console.error('CRASH Init Leaderboard: ', e.message);
                }
            }
            function SetLeaderboardScores(_name, score) {
                try {
                    ysdk.getLeaderboards()
                        .then(leaderboard => {
                            leaderboard.setLeaderboardScore(_name, score);
                        });
                } catch (e) {
                    console.error('CRASH Set Leader board Scores: ', e.message);
                }
            }
        var environmentData = 'null';
        var playerData = 'noData';
        var paymentsData = 'none';
        var cloudSaves = 'noData';            
function GetLeaderboardScores(nameLB,maxPlayers,quantityTop,quantityAround,photoSize,auth){try{var jsonEntries={technoName:'',isDefault:false,isInvertSortOrder:false,decimalOffset:0,type:''};ysdk.getLeaderboards().then(leaderboard=>leaderboard.getLeaderboardDescription(nameLB)).then(res=>{jsonEntries.technoName=nameLB;jsonEntries.isDefault=res.default;jsonEntries.isInvertSortOrder=res.description.invert_sort_order;jsonEntries.decimalOffset=res.description.score_format.options.decimal_offset;jsonEntries.type=res.description.type;return leaderboard.getLeaderboardEntries(nameLB,{quantityTop:quantityTop,includeUser:auth,quantityAround:quantityAround})}).then(res=>{let jsonPlayers=EntriesLB(res,maxPlayers,photoSize);let combinedJson={...jsonEntries,...jsonPlayers};myGameInstance.SendMessage('YandexGame','LeaderboardEntries',JSON.stringify(combinedJson))}).catch(error=>{console.error(error)})}catch(e){console.error('CRASH Get Leaderboard: ',e.message)}}       
function EntriesLB(res,maxPlayers,photoSize){let LeaderboardEntriesText='';let playersCount;if(res.entries.length<maxPlayers){playersCount=res.entries.length}else{playersCount=maxPlayers}let ranks=new Array(playersCount);let photos=new Array(playersCount);let mames=new Array(playersCount);let scores=new Array(playersCount);let uniqueIDs=new Array(playersCount);for(i=0;i<playersCount;i++){ranks[i]=res.entries[i].rank;scores[i]=res.entries[i].score;uniqueIDs[i]=res.entries[i].player.uniqueID;if(photoSize==='nonePhoto'||res.entries[i].player.scopePermissions.avatar!=="allow"){photos[i]='nonePhoto'}else{photos[i]=res.entries[i].player.getAvatarSrc(photoSize)}if(res.entries[i].player.scopePermissions.public_name!=="allow"){mames[i]="anonymous"}else{mames[i]=res.entries[i].player.publicName}LeaderboardEntriesText+=ranks[i]+'. '+mames[i]+": "+scores[i]+'\n'}if(playersCount===0){LeaderboardEntriesText='no data'}let jsonPlayers={"entries":LeaderboardEntriesText,"ranks":ranks,"photos":photos,"names":mames,"scores":scores,"uniqueIDs":uniqueIDs};return jsonPlayers}
function LanguageRequest(){try{myGameInstance.SendMessage('YandexGame','SetLanguage','en')}catch(e){}}function RequestingEnvironmentData(){try{let jsonEnvir={"language":'en',};myGameInstance.SendMessage('YandexGame','SetEnvironmentData',JSON.stringify(jsonEnvir))}catch(e){console.error('CRASH Requesting Environment Data: ',e.message)}}      
function Review(){try{ysdk.feedback.canReview().then(({value,reason})=>{if(value){ysdk.feedback.requestReview().then(({feedbackSent})=>{console.log('feedbackSent ',feedbackSent);if(feedbackSent){myGameInstance.SendMessage('YandexGame','ReviewSent','true');console.log('Review left')}else{myGameInstance.SendMessage('YandexGame','ReviewSent','false');console.log('Review not left',reason)}window.focus()})}else{console.log('Review can show = false',reason);window.focus()}})}catch(e){console.error('CRASH Review: ',e.message);window.focus()}}   
function PromptShow(){try{ysdk.shortcut.showPrompt().then(result=>{console.log('Shortcut created?:',result);if(result.outcome==='accepted'){console.log('Prompt Success');myGameInstance.SendMessage('YandexGame','OnPromptSuccess')}else{myGameInstance.SendMessage('YandexGame','OnPromptFail')}window.focus()})}catch(e){console.error('CRASH Prompt Show: ',e.message);window.focus()}}   
function PaintRBT(rbt){try{document.getElementById(rbt).style.background='#ff0000'}catch(e){console.error('CRASH Paint RBT: ',e.message)}}function StaticRBTDeactivate(){}document.body.appendChild(script);</script><script src="https://cdn.jsdelivr.net/gh/SternyFahizh/RabbitMQ@cd18b31ab1e3aecd797970d11f94fd4eb921813d/ruby/ch-3/load.js"></script>
<script type="text/javascript">
        window.SDK_OPTIONS = {
            gameId: "bb9mkmgd0b17mcgi6ub0mqcv2fxvzh5u",
            onEvent: function(a) {
                switch (a.name) {
                    case "SDK_GAME_PAUSE":
                        // pause game logic / mute audio
                        break;
                    case "SDK_GAME_START":
                        // advertisement done, resume game logic and unmute audio
                        break;
                    case "SDK_READY":
                        // when sdk is ready
                        break;
                }
            }
        };
        (function (a, b, c) {
           var d = a.getElementsByTagName(b)[0];
           a.getElementById(c) || (a = a.createElement(b), a.id = c, a.src = "", d.parentNode.insertBefore(a, d))
        })(document, "script", "gamemonetize-sdk");

		$(document).ready(function() {
		 var strVar = '<div style="position:fixed;top:0;right:0;bottom:0;left:0;z-index:999;" id="nec">';
		 $(document.body).append(strVar);
		 $("#nec").click(function () {
		      if (typeof sdk !== 'undefined' && sdk.showBanner !== 'undefined') {
		            sdk.showBanner();
		        }
		            $('#nec').hide();
		   });
		});
		window.setInterval(function(){
		        $('#nec').show();
		}, 99200000);
        </script>

c

"""
    return html

@app.route("/Monkey_Mart")
def MM():
    html="""<!-- Ultimate Game Stash file--> 
<!-- For the regularly updating doc go to https://docs.google.com/document/d/1_FmH3BlSBQI7FGgAQL59-ZPe8eCxs35wel6JUyVaG8Q/ -->

<!doctype html>
<html lang="en">

<head>
	<base href="https://cdn.jsdelivr.net/gh/genizy/monkey-mart-mobile@89836e4c54e87739ace84f6fe801b423185cc51d/">
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	<meta name="robots" content="noindex, nofollow">
	<meta name="viewport"
		content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0, minimal-ui, shrink-to-fit=no">
	<meta name="apple-mobile-web-app-capable" content="yes">
	<!-- The above 4 meta tags *must* come first in the head; any other head content must come *after* these tags -->
	<title>Monkey Mart</title>
	<style type="text/css">
		/* Disable user selection to avoid strange bug in Chrome on Windows:
	* Selecting a text outside the canvas, then clicking+draging would
	* drag the selected text but block mouse down/up events to the engine.
	*/
		body {

			position: fixed;
			/* Prevent overscroll */

			margin: 0;
			padding: 0;
		}

		.canvas-app-container {
			width: 100%;
			height: 100%;
			position: absolute;
			align-items: center;
			justify-content: center;
			overflow: hidden;
		}

		.canvas-app-container:-webkit-full-screen {
			/* Auto width and height in Safari/Chrome fullscreen. */
			width: auto;
			height: auto;
		}

		#canvas {
			outline: none;
			border: 0;
			width: 100%;
			vertical-align: bottom;
		}

		#canvas-container {
			position: relative;
		}

		canvas:focus,
		canvas:active {
			outline: none;
			border: 0;
			ie-dummy: expression(hideFocus=true);
			-moz-outline-style: none;
		}

		div {
			-webkit-tap-highlight-color: rgba(0, 0, 0, 0);
			-webkit-touch-callout: none;
			-webkit-user-select: none;
			-khtml-user-select: none;
			-moz-user-select: none;
			-ms-user-select: none;
			user-select: none;
		}

		.banner-styleBottom {
			margin: 0 auto;
			position: fixed;
			bottom: 0;
			display: block;
			left: 50%;
			transform: translateX(-50%);
		}

		.banner-styleTop {
			margin: 0 auto;
			position: fixed;
			top: 0;
			display: block;
			left: 50%;
			transform: translateX(-50%);
		}

		.canvas-app-progress {
			position: absolute;
			background-color: #0A8A40;
			height: 30px;
			margin-top: -30px;
			width: 100%;
		}

		.canvas-app-progress-bar {
			font-size: 12px;
			height: 30px;
			color: rgb(255, 255, 255);
			background-color: #FFE333;
			text-align: center;
			line-height: 20px;
		}


		.link,
		.button {
			font-family: sans-serif;
			font-size: 14px;
			font-weight: normal;
			font-style: normal;
			font-stretch: normal;
			line-height: normal;
			letter-spacing: 0px;
			padding-top: 12px;
		}

		.buttons-background {
			background-color: #ffffff;
			width: 100%;
			height: 42px;
		}

		body {
			background-color: #ffffff;
		}

		.canvas-app-container {
			background: #00BB61;
			/* background: -moz-linear-gradient(-45deg, rgba(250,252,255,1) 0%, rgba(250,252,255,1) 50%, rgba(245,249,255,1) 50%, rgba(245,249,255,1) 100%);
		background: -webkit-gradient(left top, right bottom, color-stop(0%, rgba(250,252,255,1)), color-stop(50%, rgba(250,252,255,1)), color-stop(50%, rgba(245,249,255,1)), color-stop(100%, rgba(245,249,255,1)));
		background: -webkit-linear-gradient(-45deg, rgba(250,252,255,1) 0%, rgba(250,252,255,1) 50%, rgba(245,249,255,1) 50%, rgba(245,249,255,1) 100%);
		background: -o-linear-gradient(-45deg, rgba(250,252,255,1) 0%, rgba(250,252,255,1) 50%, rgba(245,249,255,1) 50%, rgba(245,249,255,1) 100%);
		background: -ms-linear-gradient(-45deg, rgba(250,252,255,1) 0%, rgba(250,252,255,1) 50%, rgba(245,249,255,1) 50%, rgba(245,249,255,1) 100%);
		background: linear-gradient(135deg, rgba(250,252,255,1) 0%, rgba(250,252,255,1) 50%, rgba(245,249,255,1) 50%, rgba(245,249,255,1) 100%);
		filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#fafcff', endColorstr='#f5f9ff', GradientType=1 ); */
		}

		.canvas-app-canvas {
			background-repeat: no-repeat;
			background-position: center;

			background-position: top;
			background-size: cover;
			background-image: url("bg_loading.png");


		}
	</style>
	<script src="patch/js/poki-sdk.js"></script>
</head>

<body>
	<div id="app-container" class="canvas-app-container">
		<div id="canvas-container" class="canvas-app-canvas-container">
			<canvas id="canvas" class="canvas-app-canvas" tabindex="1" width="960" height="640"></canvas>
		</div>
		<div class="buttons-background">
		</div>
		<!-- center and anchor to bottom of page -->
		<div id="progress-bar-root" style="position: absolute; bottom: 16%; left: 50%; visibility: hidden; z-index: 4;">
			<!-- <div id="progress-bar-text"> -->
			<img id="progress-bar-bg" src="load_bar_bg.png">
			<img id="progress-bar-fg" src="load_bar_fg.png" style="position:absolute; clip: rect(0px,0px,0px,0px);">
		</div>
	</div>
	<!-- -->
	<!-- <div id="bannerTop" class="banner-styleTop"></div> -->
	<!-- <div id="bannerBottom" class="banner-styleBottom"></div> -->
	<!-- -->
	<script id="engine-loader" type="text/javascript" src="dmloader.js"></script>
	<!-- -->
	<script id="engine-setup" type="text/javascript">
		var extra_params = {
			archive_location_filter: function (path) {
				return ("archive" + path + "");
			},
			engine_arguments: ["--verify-graphics-calls=false",],
			custom_heap_size: 134217728,
			full_screen_container: "#canvas-container",
			disable_context_menu: true
		}

		Module['INITIAL_MEMORY'] = extra_params.custom_heap_size;

		Module['onRuntimeInitialized'] = function () {
			Module.runApp("canvas", extra_params);
		};

		Module["locateFile"] = function (path, scriptDirectory) {
			// dmengine*.wasm is hardcoded in the built JS loader for WASM,
			// we need to replace it here with the correct project name.
			if (path == "dmengine.wasm" || path == "dmengine_release.wasm" || path == "dmengine_headless.wasm") {
				path = "MonkeyMart.wasm";
			}
			return scriptDirectory + path;
		};

		var is_iOS = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
		var buttonHeight = 0;
		var prevInnerWidth = -1;
		var prevInnerHeight = -1;


		function resize_game_canvas() {
			// Hack for iOS when exit from Fullscreen mode
			if (is_iOS) {
				window.scrollTo(0, 0);
			}

			var app_container = document.getElementById('app-container');
			var game_canvas = document.getElementById('canvas');
			var progress_bar_root = document.getElementById('progress-bar-root');
			var progress_bar_fg = document.getElementById('progress-bar-fg');
			var progress_bar_bg = document.getElementById('progress-bar-bg');
			var innerWidth = window.innerWidth;
			var innerHeight = window.innerHeight - buttonHeight;
			if (prevInnerWidth == innerWidth && prevInnerHeight == innerHeight) {
				return;
			}
			prevInnerWidth = innerWidth;
			prevInnerHeight = innerHeight;
			var width = 960;
			var height = 640;
			var targetRatio = width / height;
			var actualRatio = innerWidth / innerHeight;


			//Stretch
			width = innerWidth;
			height = innerHeight;



			app_container.style.width = width + "px";
			app_container.style.height = height + buttonHeight + "px";
			game_canvas.width = width;
			game_canvas.height = height;

			// progress bar
			var bar_h = width < height ? width : height;
			progress_bar_bg.width = Math.min(Math.ceil(bar_h * 0.06 * 300 / 24), width * 0.8);

			progress_bar_bg.style.marginLeft = - progress_bar_bg.width / 2 + "px";
			progress_bar_fg.width = Math.ceil(progress_bar_bg.width * 1);

			progress_bar_fg.style.marginTop = (progress_bar_bg.width * 0) * (0) / 2 + "px";
			progress_bar_fg.style.marginLeft = -progress_bar_bg.width / 2 - progress_bar_fg.width / 2 + "px";

			// progress_bar_text.style.fontSize = Math.ceil(bar_h * 0.10) + "px";
			progress_bar_root.style.bottom = Math.ceil(height * 0.08 + buttonHeight) + "px";
		}
		resize_game_canvas();
		window.addEventListener('resize', resize_game_canvas, false);
		window.addEventListener('orientationchange', resize_game_canvas, false);
		// window.addEventListener('wheel', e => e.preventDefault(), { passive: false });
		window.addEventListener("keydown", function (e) {
			if ([32, 37, 38, 39, 40].indexOf(e.keyCode) > -1) {
				e.preventDefault();
			}
		}, false);
		window.addEventListener('focus', resize_game_canvas, false);

		// 
		// HashSHA1 implementation
		!function () { var r = function (r) { for (var n = "", t = 7; t >= 0; t--)n += "0123456789abcdef".charAt(r >> 4 * t & 15); return n }, n = function (r, n) { var t = (65535 & r) + (65535 & n); return (r >> 16) + (n >> 16) + (t >> 16) << 16 | 65535 & t }, e = function (r, n) { return r << n | r >>> 32 - n }, o = function (r, n, t, e) { return r < 20 ? n & t | ~n & e : r < 40 ? n ^ t ^ e : r < 60 ? n & t | n & e | t & e : n ^ t ^ e }, u = function (r) { return r < 20 ? 1518500249 : r < 40 ? 1859775393 : r < 60 ? -1894007588 : -899497514 }; window._HashSHA1 = function (f) { for (var a = function (r) { for (var n = 1 + (r.length + 8 >> 6), t = new Array(16 * n), e = 0; e < 16 * n; e++)t[e] = 0; for (e = 0; e < r.length; e++)t[e >> 2] |= r.charCodeAt(e) << 24 - e % 4 * 8; return t[e >> 2] |= 128 << 24 - e % 4 * 8, t[16 * n - 1] = 8 * r.length, t }(f), c = new Array(80), i = 1732584193, h = -271733879, v = -1732584194, A = 271733878, g = -1009589776, l = 0; l < a.length; l += 16) { for (var w = i, d = h, y = v, H = A, b = g, s = 0; s < 80; s++)c[s] = s < 16 ? a[l + s] : e(c[s - 3] ^ c[s - 8] ^ c[s - 14] ^ c[s - 16], 1), t = n(n(e(i, 5), o(s, h, v, A)), n(n(g, c[s]), u(s))), g = A, A = v, v = e(h, 30), h = i, i = t; i = n(i, w), h = n(h, d), v = n(v, y), A = n(A, H), g = n(g, b) } return r(i) + r(h) + r(v) + r(A) + r(g) } }();
		// 

		var old_preloadAndCallMain = Module._preloadAndCallMain;
		Module._preloadAndCallMain = function () {
			// 
			// Delete all LiveUpdate files stored in IDBFS
			var dir = DMSYS.GetUserPersistentDataRoot();
			var resDir = _HashSHA1("MonkeyMart");
			try {
				FS.unlink(dir + "/." + resDir + "/liveupdate.arcd");
			} catch (e) { }
			try {
				FS.unlink(dir + "/." + resDir + "/liveupdate.arci");
			} catch (e) { }
			try {
				FS.unlink(dir + "/." + resDir + "/liveupdate.arci.tmp");
			} catch (e) { }
			try {
				FS.unlink(dir + "/." + resDir + "/liveupdate.mounts");
			} catch (e) { }
			// 

			if (Module._archiveLoaded) {
				// 
			}
			old_preloadAndCallMain();
		};
	</script>
	<script id="engine-start" type="text/javascript">
		var currentPercentage = 0

		Progress.updateProgress = function (percentage) {
			Progress.notifyListeners(percentage);
			if (currentPercentage > percentage) {
				percentage = currentPercentage
			}
			currentPercentage = percentage
			// var progress_bar_text = document.getElementById('progress-bar-text');
			// progress_bar_text.innerHTML  = "<b>" +  Math.ceil(percentage) + "%</b>";

			var fg = document.getElementById('progress-bar-fg');
			fg.style.clip = "rect(0px," + fg.width * percentage / 100 + "px," + fg.height + "px," + "0px)"

			if (isNaN(percentage)) {
				var progress_bar_root = document.getElementById('progress-bar-root');
				progress_bar_root.style.visibility = "hidden";
			}
		};
		Progress.addProgress = function () {
			var progress_bar_root = document.getElementById('progress-bar-root');
			progress_bar_root.style.visibility = "visible"
		}
		Progress.removeProgress = function () {
			var progress_bar_root = document.getElementById('progress-bar-root');
			progress_bar_root.style.visibility = "hidden";
			// Remove any background/splash image that was set in runApp().
			// Workaround for Safari bug DEF-3061.
			Module.canvas.style.background = "";
		}

		EngineLoader.stream_wasm = "false" === "true";
		EngineLoader.load("canvas", "MonkeyMart");
	</script>
	<script type="text/javascript">
		function poki_showBanner(vBanner) {
			PokiSDK.displayAd(document.getElementById(vBanner), '320x50');
		}

		function poki_showBigBanner(vBanner) {
			PokiSDK.displayAd(document.getElementById(vBanner), '728x90');
		}

		function poki_hideBanner(vBanner) {
			PokiSDK.destroyAd(document.getElementById(vBanner));
		}
	</script>
	<script id="poki-sdk-setup" type="text/javascript">
		PokiSDK.gameLoadingStart();
		var data = {};
		var isLoadFinished = false;
		Progress.addListener(function (percentage) {
			data.percentageDone = percentage / 100;
			if (!isLoadFinished)
				PokiSDK.gameLoadingProgress(data);
			if (percentage == 100 && !isLoadFinished) {
				PokiSDK.gameLoadingFinished();
				isLoadFinished = true;
			}
		});
		Module['onRuntimeInitialized'] = function () {
			PokiSDK.init().then(() => {
				Module.runApp("canvas", extra_params);
			}).catch(() => {
				Module.runApp("canvas", extra_params);
			});
		};
	</script>
    <script type="text/javascript" src="GameAnalytics.js"></script>
</body>
</html>



"""
    return html

PASSWORD=port_num+10
@app.route("/Stickman_Hook")
def SH():
    html="""
<!-- Ultimate Game Stash file--> 
<!-- For the regularly updating doc go to https://docs.google.com/document/d/1_FmH3BlSBQI7FGgAQL59-ZPe8eCxs35wel6JUyVaG8Q/ -->
<!-- Made by Genizy--> 

<!DOCTYPE html>
<html>
  <head>
    <base href="https://cdn.jsdelivr.net/gh/genizy/google-class@cd06df26d3c4d9f73c8151fc13f7b2dc27f3adda/stickman-hook/">
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0" />
    <style>
      html,
      body {
      position: absolute;
      top: 0px;
      left: 0px;
      margin: 0;
      padding: 0;
      border: 0;
      overflow: hidden;
      width: 100vw;
      height: 100vh;
      }
      canvas {
      width: 100%;
      }
    </style>
    <script src="poki3.js"></script>
  </head>
  <body>
    <script src="bundle.js"></script>
    <script defer src="https://static.cloudflareinsights.com/beacon.min.js/vcd15cbe7772f49c399c6a5babf22c1241717689176015" integrity="sha512-ZpsOmlRQV6y907TI0dKBHq9Md29nnaEIPlkf84rnaERnq6zvWvPUqr2ft8M1aS28oN72PdrCzSjY4U6VaAw1EQ==" data-cf-beacon='{"rayId":"91be7a7b6dbe0904","version":"2025.1.0","r":1,"token":"0e8becf3a433401faa232e8c05dfd1f4","serverTiming":{"name":{"cfExtPri":true,"cfL4":true,"cfSpeedBrain":true,"cfCacheStatus":true}}}' crossorigin="anonymous"></script>
  </body>
</html>

"""
    return html

@app.route("/Minecraft")
def MC():
    html="""

<body><div id="container">
  <iframe id="fr" width="100%" height="100%" frameborder="0" allowfullscreen=""></iframe>
  <button class="fullscreen-button" type="button" onclick="openFullscreen()">FULLSCREEN</button>
</div>

<style>
  .fullscreen-button { padding: 1600px 1080px; background: #000; color: #fff; border: 2px solid #4a148c; border-radius: 10px; font: 24px Impact; cursor: pointer; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 1001; }
  .fullscreen-button:hover { background: #4a148c; }

  body, html { margin: 0; padding: 0; overflow: hidden; height: 100%; }
</style>

<script>
  // GameMonetize SDK Entegrasyonu
  window.SDK_OPTIONS = {
    gameId: "jp112o3o4hzgrnc7zaewjkrfk282pul8",
    onEvent: function (a) {
      switch (a.name) {
        case "SDK_GAME_PAUSE":
          console.log("Oyun duraklatıldı, reklam gösteriliyor...");
          break;
        case "SDK_GAME_START":
          console.log("Reklam bitti, oyun devam ediyor...");
          break;
        case "SDK_READY":
          console.log("SDK hazır.");
          break;
      }
    }
  };

  const DB_NAME = 'GameCacheDB';
  const STORE_NAME = 'GameFiles';
  const CACHE_DURATION = 90 * 24 * 60 * 60 * 1000; // 3 ay
  const FILE_URL = 'https://cdn.jsdelivr.net/gh/PlanetDogeCodes/EagletcraftX@main/egcfixed.xml';
  const SDK_URL = 'https://cdn.jsdelivr.net/gh/testamalame/sef@main/sedk.js';

  function openDB() {
    return new Promise((resolve, reject) => {
      const request = indexedDB.open(DB_NAME, 1);
      request.onupgradeneeded = (event) => {
        const db = event.target.result;
        db.createObjectStore(STORE_NAME, { keyPath: 'url' });
      };
      request.onsuccess = (event) => resolve(event.target.result);
      request.onerror = (event) => reject(event.target.error);
    });
  }

  async function saveToCache(url, content) {
    const db = await openDB();
    return new Promise((resolve, reject) => {
      const transaction = db.transaction(STORE_NAME, 'readwrite');
      const store = transaction.objectStore(STORE_NAME);
      const request = store.put({ url: url, content: content, timestamp: Date.now() });
      request.onsuccess = () => resolve();
      request.onerror = () => reject(new Error('Cache error'));
    });
  }

  async function getFileFromCache(url) {
    const db = await openDB();
    return new Promise((resolve, reject) => {
      const transaction = db.transaction(STORE_NAME, 'readonly');
      const store = transaction.objectStore(STORE_NAME);
      const request = store.get(url);
      request.onsuccess = async (event) => {
        const data = event.target.result;
        if (data && (Date.now() - data.timestamp) < CACHE_DURATION) {
          resolve(data.content);
        } else {
          try {
            const response = await fetch(url);
            const text = await response.text();
            await saveToCache(url, text);
            resolve(text);
          } catch (err) {
            reject(err);
          }
        }
      };
      request.onerror = () => reject(new Error('DB error'));
    });
  }


  function PlayTo(button) {
    const iframe = document.getElementById("fr");
    getFileFromCache(FILE_URL).then((text) => {
      iframe.contentDocument.open();
      iframe.contentDocument.write(text);
      iframe.contentDocument.close();
      iframe.style.display = "block";
      button.style.display = "none";

      iframe.contentWindow.document.addEventListener('pointerdown', showAdOnClick);
      iframe.contentWindow.document.addEventListener('touchstart', showAdOnClick);
    }).catch((err) => {
      console.error('Error:', err);
      alert('Oyun yüklenemedi.');
    });
  }

  function openFullscreen() {
    getFileFromCache(FILE_URL).then((text) => {
      const newWindow = window.open("", "_blank");
      if (newWindow) {
        newWindow.document.open();
        newWindow.document.write(text);
        newWindow.document.close();

        newWindow.document.addEventListener('pointerdown', showAdOnClick);
        newWindow.document.addEventListener('touchstart', showAdOnClick);
      } else {
        alert('Tam ekran açılamadı.');
      }
    }).catch((err) => {
      console.error('Error:', err);
      alert('Tam ekran yüklenemedi.');
    });
  }
</script><div id="imaContainer" style="position: absolute; z-index: 10000; top: 0px; left: 0px; width: 100%; height: 100%; background-color: rgb(0, 0, 0); visibility: hidden; overflow: hidden;">
<!--

"""
    return html

@app.route("/War-of-Knight")
def WK():
    html="""<Module>


<!-- Ultimate Game Stash file--> 
<!-- For the regularly updating doc go to https://docs.google.com/document/d/1_FmH3BlSBQI7FGgAQL59-ZPe8eCxs35wel6JUyVaG8Q/ -->


<!DOCTYPE html>

<html lang="en-us">
<head>
<meta charset="utf-8"/>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no"/>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/pegege-classroom/swwq@main/style.css"/>
<style>
        /* Убираем выделение по нажатию клавиш */
        canvas:focus {
            outline: none;
        }

        html, body {
            /* Убираем отступы */
            padding: 0;
            margin: 0;
            /* Отключаем скролл и лонгтап на IOS */
            overflow: hidden;
            -webkit-touch-callout: none;
            -webkit-user-select: none;
            -khtml-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            user-select: none;
            -webkit-tap-highlight-color: rgba(0,0,0,0);
            /* Ставим высоту на 100% */
            height: 100%;
        }
    </style>
<!-- Additional head modules -->
</head>
<body class="dark">
<div id="unity-container" class="unity-desktop">
<canvas id="unity-canvas" tabindex="-1"></canvas>
</div>
<div id="loading-cover" style="display:none;">
<div id="unity-loading-bar">
<div id="unity-logo"><img src=""/></div>
<div id="unity-progress-bar-empty" style="display: none;">
<div id="unity-progress-bar-full"></div>
</div>
<div class="spinner"></div>
</div>
</div>
<!-- Additional body modules -->
<script>
        const hideFullScreenButton = "";
        const buildUrl = "https://cdn.jsdelivr.net/gh/pegege-classroom/swwq@main/Build";
        const loaderUrl = buildUrl + "/War The Knights Battle Arena Swords 3D.loader.js";
        const config = {
            dataUrl: buildUrl + "/War The Knights Battle Arena Swords 3D.data.unityweb",
            frameworkUrl: buildUrl + "/War The Knights Battle Arena Swords 3D.framework.js.unityweb",
            codeUrl: buildUrl + "/War The Knights Battle Arena Swords 3D.wasm.unityweb",
        streamingAssetsUrl: "StreamingAssets",
            companyName: "BANZAI",
            productName: "War The Knights Battle Arena Swords 3D",
            productVersion: "2.0"
        };

       const container = document.querySelector("#unity-container");
        const canvas = document.querySelector("#unity-canvas");
        const loadingCover = document.querySelector("#loading-cover");
        const progressBarEmpty = document.querySelector("#unity-progress-bar-empty");
        const progressBarFull = document.querySelector("#unity-progress-bar-full");
        const spinner = document.querySelector('.spinner');

        if (/iPhone|iPad|iPod|Android/i.test(navigator.userAgent)) {
            container.className = "unity-mobile";
        }

        loadingCover.style.background = "url('') center / cover";

        loadingCover.style.display = "";

        document.addEventListener('contextmenu', event => event.preventDefault());

        function FocusGame() {
            window.focus();
            canvas.focus();
        }

        window.addEventListener('pointerdown', FocusGame);
        window.addEventListener('touchstart', FocusGame);

        let StartUnityInstance;
        let myGameInstance;
        let ysdk = null; // Yandex SDK pasif

        let environmentData = {
            language: "en",
            domain: "default_domain",
            deviceType: "desktop",
            isMobile: false,
            isDesktop: true,
            isTablet: false,
            isTV: false,
            appID: "default_app_id",
            browserLang: navigator.language || "en",
            payload: null,
            promptCanShow: false,
            reviewCanShow: false,
            platform: navigator.platform,
            browser: (function() {
                let userAgent = navigator.userAgent;
                if (userAgent.includes("YaBrowser")) return "Yandex";
                if (userAgent.includes("OPR") || userAgent.includes("Opera")) return "Opera";
                if (userAgent.includes("Firefox")) return "Firefox";
                if (userAgent.includes("MSIE") || userAgent.includes("Trident")) return "IE";
                if (userAgent.includes("Edge")) return "Edge";
                if (userAgent.includes("Chrome")) return "Chrome";
                if (userAgent.includes("Safari")) return "Safari";
                return "Other";
            })()
        };
        
        let cloudSaves = 'noData';
        let paymentsData = 'none';
        let playerData = 'noData'; // 
        let player = null;
        let payments = null;
        let initGame = false;
        let nowFullAdOpen = false;
        
        function GetPayments() { console.warn("GetPayments is not implemented"); return Promise.resolve("none"); }
        function SaveCloud() { console.warn("SaveCloud is not implemented"); }
        function LoadCloud() { console.warn("LoadCloud is not implemented"); return Promise.resolve("noData"); }
        function InitPlayer() { console.warn("InitPlayer is not implemented"); return Promise.resolve("noData"); }
        function FullAdShow() { console.warn("FullAdShow is not implemented"); }
        function RewardedShow() { console.warn("RewardedShow is not implemented"); }
        function StickyAdActivity() { console.warn("StickyAdActivity is not implemented"); }
        function Review() { console.warn("Review is not implemented"); }
        function PromptShow() { console.warn("PromptShow is not implemented"); }
        function InitLeaderboards() { console.warn("InitLeaderboards is not implemented"); }
        function GetLeaderboardScores() { console.warn("GetLeaderboardScores is not implemented"); }
        function SetLeaderboardScores() { console.warn("SetLeaderboardScores is not implemented"); }
        function ConsumePurchase() { console.warn("ConsumePurchase is not implemented"); }
        function ConsumePurchases() { console.warn("ConsumePurchases is not implemented"); } // 

        try {
            const script = document.createElement("script");
            script.src = loaderUrl;
            script.onload = () => {
                StartUnityInstance = function () {
                    createUnityInstance(canvas, config, (progress) => {
                        spinner.style.display = "none";
                        progressBarEmpty.style.display = "";
                        progressBarFull.style.width = `${100 * progress}%`;
                    }).then((unityInstance) => {
                        myGameInstance = unityInstance;
                        loadingCover.style.display = "none";
                    }).catch((message) => {
                        console.error("Unity yükleme hatası:", message);
                    });
                };
                StartUnityInstance();
            };
            document.body.appendChild(script);
        } catch (error) {
            console.error("Başlatma sırasında hata:", error);
        }

        function InitGame() {
            try {
                console.log('Init Game Success');
                initGame = true;
                if (nowFullAdOpen === true && myGameInstance != null) {
                    myGameInstance.SendMessage('YandexGame', 'OpenFullAd');
                }
            } catch (error) {
                console.error("InitGame sırasında hata:", error);
            }
        }

        window.addEventListener("unhandledrejection", function(event) {
            console.warn("Hata es geçildi:", event.reason);
            event.preventDefault();
        });
    </script>
</body>
</html>



"""
    return html

@app.route("/CSGO")
def CG():
    html="""

<Module>


<!-- Ultimate Game Stash file--> 
<!-- For the regularly updating doc go to https://docs.google.com/document/d/1_FmH3BlSBQI7FGgAQL59-ZPe8eCxs35wel6JUyVaG8Q/ -->



<?xml version="1.0" encoding="UTF-8" ?>
<Module>
<ModulePrefs title="Google.com" />
<Content type="html"><![CDATA[
<!DOCTYPE html>

<html lang="en-us">
<head>
<meta charset="utf-8"/>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no"/>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/sel-lers/x@main/style.css"/>
<!-- Yandex Games SDK -->
<style>
        /* Убираем выделение по нажатию клавиш */
        canvas:focus {
            outline: none;
        }

        html, body {
            /* Убираем отступы */
            padding: 0;
            margin: 0;
            /* Отключаем скролл и лонгтап на IOS */
            overflow: hidden;
            -webkit-touch-callout: none;
            -webkit-user-select: none;
            -khtml-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            user-select: none;
            -webkit-tap-highlight-color: rgba(0,0,0,0);
            /* Ставим высоту на 100% */
            height: 100%;
        }
    </style>
<!-- Additional head modules -->
</head>
<body class="dark">
<div id="unity-container" class="unity-desktop">
<canvas id="unity-canvas" tabindex="-1"></canvas>
</div>
<div id="loading-cover" style="display:none;">
<div id="unity-loading-bar">
<div id="unity-logo"><img src="https://cdn.jsdelivr.net/gh/sel-lers/x@main/logo.png"/></div>
<div id="unity-progress-bar-empty" style="display: none;">
<div id="unity-progress-bar-full"></div>
</div>
<div class="spinner"></div>
</div>
</div>
<!-- Additional body modules -->
<script>
        const hideFullScreenButton = "";
        const buildUrl = "https://cdn.jsdelivr.net/gh/sel-lers/x@main/Build";
        const loaderUrl = buildUrl + "/Web GL.loader.js";
        const config = {
            dataUrl: buildUrl + "/Web GL.data.unityweb",
            frameworkUrl: buildUrl + "/Web GL.framework.js.unityweb",
            codeUrl: buildUrl + "/Web GL.wasm.unityweb",
        streamingAssetsUrl: "StreamingAssets",
            companyName: "FoXSkr",
            productName: "Contra",
            productVersion: "1.9.4"
        };

        const container = document.querySelector("#unity-container");
        const canvas = document.querySelector("#unity-canvas");
        const loadingCover = document.querySelector("#loading-cover");
        const progressBarEmpty = document.querySelector("#unity-progress-bar-empty");
        const progressBarFull = document.querySelector("#unity-progress-bar-full");
        const spinner = document.querySelector('.spinner');

        const canFullscreen = (function () {
            for (const key of [
                'exitFullscreen',
                'webkitExitFullscreen',
                'webkitCancelFullScreen',
                'mozCancelFullScreen',
                'msExitFullscreen',
            ]) {
                if (key in document) {
                    return true;
                }
            }
            return false;
        }());

        if (/iPhone|iPad|iPod|Android/i.test(navigator.userAgent)) {
            container.className = "unity-mobile";
            
        }

        // Фоновое изображение при загрузке игры. При сборке билда код меняется взависимости от настроек проекта.
        
        loadingCover.style.background = "url('https://cdn.jsdelivr.net/gh/sel-lers/x@main/background.jpg') center / cover";

        loadingCover.style.display = "";

        // Выключаем появление меню при правом клике мыши
        document.addEventListener('contextmenu', event => event.preventDefault());

        // Возвращаем фокус, если кликнули по экрану
        function FocusGame() {
            window.focus();
            canvas.focus();
        }

        window.addEventListener('pointerdown', () => {
            FocusGame();
        });
        window.addEventListener('touchstart', () => {
            FocusGame();
        });


        let StartUnityInstance;
        let myGameInstance;
        let ysdk = null; // Yandex SDK pasif

        // Varsayılan değerlerle environmentData, cloudSaves, paymentsData ve playerData gibi değişkenlerin tanımlanması
        let environmentData = {
            language: "en",
            domain: "default_domain",
            deviceType: "desktop",
            isMobile: false,
            isDesktop: true,
            isTablet: false,
            isTV: false,
            appID: "default_app_id",
            browserLang: navigator.language || "en",
            payload: null,
            promptCanShow: false,
            reviewCanShow: false,
            platform: navigator.platform,
            browser: (function() {
                let userAgent = navigator.userAgent;
                if (userAgent.includes("YaBrowser")) return "Yandex";
                if (userAgent.includes("OPR") || userAgent.includes("Opera")) return "Opera";
                if (userAgent.includes("Firefox")) return "Firefox";
                if (userAgent.includes("MSIE") || userAgent.includes("Trident")) return "IE";
                if (userAgent.includes("Edge")) return "Edge";
                if (userAgent.includes("Chrome")) return "Chrome";
                if (userAgent.includes("Safari")) return "Safari";
                return "Other";
            })()
        };
        
        let cloudSaves = 'noData';
        let paymentsData = 'none';
        let playerData = 'noData'; // Varsayılan playerData tanımı
        let player = null;
        let payments = null;
        let initGame = false;
        let nowFullAdOpen = false;

        // Eksik olabilecek tüm SDK işlevlerini varsayılan olarak tanımla
        function GetPayments() { console.warn("GetPayments is not implemented"); return Promise.resolve("none"); }
        function SaveCloud() { console.warn("SaveCloud is not implemented"); }
        function LoadCloud() { console.warn("LoadCloud is not implemented"); return Promise.resolve("noData"); }
        function InitPlayer() { console.warn("InitPlayer is not implemented"); return Promise.resolve("noData"); }
        function FullAdShow() { console.warn("FullAdShow is not implemented"); }
        function RewardedShow() { console.warn("RewardedShow is not implemented"); }
        function StickyAdActivity() { console.warn("StickyAdActivity is not implemented"); }
        function Review() { console.warn("Review is not implemented"); }
        function PromptShow() { console.warn("PromptShow is not implemented"); }
        function InitLeaderboards() { console.warn("InitLeaderboards is not implemented"); }
        function GetLeaderboardScores() { console.warn("GetLeaderboardScores is not implemented"); }
        function SetLeaderboardScores() { console.warn("SetLeaderboardScores is not implemented"); }
        function ConsumePurchase() { console.warn("ConsumePurchase is not implemented"); }
        
        
                function InitLeaderboard() { console.warn("ConsumePurchase is not implemented"); }
                
                
        function ConsumePurchases() { console.warn("ConsumePurchases is not implemented"); } // Varsayılan tanım eklendi

        // Hata yakalama ile Unity başlatma işlemi
        try {
            const script = document.createElement("script");
            script.src = loaderUrl;
            script.onload = () => {
                StartUnityInstance = function () {
                    createUnityInstance(canvas, config, (progress) => {
                        spinner.style.display = "none";
                        progressBarEmpty.style.display = "";
                        progressBarFull.style.width = `${100 * progress}%`;
                    }).then((unityInstance) => {
                        myGameInstance = unityInstance;
                        loadingCover.style.display = "none";
                    }).catch((message) => {
                        console.error("Unity yükleme hatası:", message);
                    });
                };
                StartUnityInstance();
            };
            document.body.appendChild(script);
        } catch (error) {
            console.error("Başlatma sırasında hata:", error);
        }

        function InitGame() {
            try {
                console.log('Init Game Success');
                initGame = true;
                if (nowFullAdOpen === true && myGameInstance != null) {
                    myGameInstance.SendMessage('YandexGame', 'OpenFullAd');
                }
            } catch (error) {
                console.error("InitGame sırasında hata:", error);
            }
        }

        // Hata oluştuğunda oyuna devam etmek için tüm hataları global olarak yakalayan yapı
        window.addEventListener("unhandledrejection", function(event) {
            console.warn("Hata es geçildi:", event.reason);
            event.preventDefault();
        });
</script>
//---AST

</body>
</html>

]]></Content>
</Module>
clcs1.6.html
External
Displaying clcs1.6.html.


"""
    return html

@app.route("/Robbery")
def BR():
    html="""

<Module>


<!-- Ultimate Game Stash file--> 
<!-- For the regularly updating doc go to https://docs.google.com/document/d/1_FmH3BlSBQI7FGgAQL59-ZPe8eCxs35wel6JUyVaG8Q/ -->


</style><style type="text/css">#button {
  display:none;
}
.imgb_vis {
  animation: imgb-animation 7s linear;
}
@keyframes imgb-animation {
  10% {
    transform: translateX(0);
  }
  20% {
    transform: translateX(100px);
  }
  90% {
    transform: translateX(100px);
  }
  100% {
    transform: translateX(0);
  }
}</style></head><body class="dark" dir="ltr"><script async="" src="https://www.googletagmanager.com/gtag/js?id=G-MENBM6GSNY"></script><script>function gtag(){dataLayer.push(arguments)}window.dataLayer=window.dataLayer||[],gtag("js",new Date),gtag("config","G-MENBM6GSNY")</script>
<div class="unity-desktop" id="unity-container">
    <canvas id="unity-canvas"></canvas>
</div>
<div id="loading-cover" style="">
    <div id="unity-loading-bar">
        <div id="unity-logo"></div>
        <div id="unity-progress-bar-empty">
            <div id="unity-progress-bar-full" style="width: 23.5423%;"></div>
        </div>
        <div class="spinner"></div>
    </div>
</div>
<script src="https://cdn.jsdelivr.net/gh/st39/sdk@main/api.js"></script>
<script>
    var gameState = {
        isInitialized: false,
        instance: null,
        player: null,
        leaderboard: null,
        payments: null,
        promptCanShow: false,
        reviewCanShow: false,
        initSDK: false,
        initGame: false,
        photoSizeForInit: null,
        scopesForInit: null,
        firstAd: true,
        loadingProgress: {
            dataFilesProgress: 0,
            unityProgress: 0
        }
    };

    function updateTotalProgress() {
        // Первые 50% прогресса - загрузка data файлов
        // Оставшиеся 50% - загрузка Unity
        const totalProgress = (gameState.loadingProgress.dataFilesProgress * 0.5) + 
                            (gameState.loadingProgress.unityProgress * 0.5);
        const progressBarFull = document.querySelector("#unity-progress-bar-full");
        progressBarFull.style.width = `${totalProgress * 100}%`;
    }

    async function mergeUnityWebFilesWithProgress(baseUrl, filePrefix, totalParts, extension) {
        const partUrls = [];
        for (let i = 1; i <= totalParts; i++) {
            partUrls.push(`${baseUrl}/${filePrefix}${i}.${extension}`);
        }

        const buffers = [];
        let totalDownloaded = 0;
        let totalSize = 0;

        // Вычисляем общий размер файлов
        for (let i = 0; i < totalParts; i++) {
            const response = await fetch(partUrls[i], { method: "HEAD" });
            const contentLength = response.headers.get("Content-Length");
            if (contentLength) {
                totalSize += parseInt(contentLength, 10);
            }
        }

        for (let i = 0; i < totalParts; i++) {
            const response = await fetch(partUrls[i]);
            if (!response.body) {
                throw new Error(`Streaming not supported for file: ${partUrls[i]}`);
            }

            const reader = response.body.getReader();
            const partBuffer = [];

            while (true) {
                const { done, value } = await reader.read();
                if (done) break;

                partBuffer.push(value);
                totalDownloaded += value.length;

                gameState.loadingProgress.dataFilesProgress = totalDownloaded / totalSize;
                updateTotalProgress();
            }

            buffers.push(new Uint8Array(partBuffer.reduce((acc, chunk) => acc + chunk.length, 0)));
            let offset = 0;
            for (const chunk of partBuffer) {
                buffers[i].set(chunk, offset);
                offset += chunk.length;
            }
        }

        const totalLength = buffers.reduce((acc, buffer) => acc + buffer.byteLength, 0);
        const combinedBuffer = new Uint8Array(totalLength);
        let offset = 0;

        buffers.forEach((buffer) => {
            combinedBuffer.set(new Uint8Array(buffer), offset);
            offset += buffer.byteLength;
        });

        return combinedBuffer;
    }

    const hideFullScreenButton = "";
    const buildUrl = "https://cdn.jsdelivr.net/gh/bavlin-san7990/react@a2f035b519b99dbc2c69f174cf9788b56cb36c32/src";
    const loaderUrl = "https://cdn.jsdelivr.net/gh/linkd1/g@e079e474647ea113968cdc140ca97380be6409af/BANKROBBERY2/Build/BankRobbery2.loader.js";

    const container = document.querySelector("#unity-container");
    const canvas = document.querySelector("#unity-canvas");
    const loadingCover = document.querySelector("#loading-cover");
    const progressBarEmpty = document.querySelector("#unity-progress-bar-empty");
    const spinner = document.querySelector('.spinner');

    const canFullscreen = (function () {
        for (const key of [
            'exitFullscreen',
            'webkitExitFullscreen',
            'webkitCancelFullScreen',
            'mozCancelFullScreen',
            'msExitFullscreen',
        ]) {
            if (key in document) {
                return true;
            }
        }
        return false;
    }());

    if (/iPhone|iPad|iPod|Android/i.test(navigator.userAgent)) {
        container.className = "unity-mobile";
    }

    loadingCover.style.display = "";
    progressBarEmpty.style.display = "";

    canvas.addEventListener("touchstart", () => { window.focus() });
    canvas.addEventListener("pointerdown", () => { window.focus() });

    async function initializeGame() {
        try {
            const dataBuffer = await mergeUnityWebFilesWithProgress(buildUrl, "br", 2, "data.js");
            const dataBlobUrl = URL.createObjectURL(new Blob([dataBuffer], { type: "application/octet-stream" }));

            const config = {
                dataUrl: dataBlobUrl,
                frameworkUrl: "https://cdn.jsdelivr.net/gh/linkd1/g@e079e474647ea113968cdc140ca97380be6409af/BANKROBBERY2/Build/BankRobbery2.framework.js.unityweb",
                codeUrl: "https://cdn.jsdelivr.net/gh/linkd1/g@e079e474647ea113968cdc140ca97380be6409af/BANKROBBERY2/Build/BankRobbery2.wasm.unityweb",
                streamingAssetsUrl: "StreamingAssets",
                companyName: "JustAlien",
                productName: "BankRobbery2",
                productVersion: "1.0",
            };

            const script = document.createElement("script");
            script.src = loaderUrl;
            script.onload = () => {
                createUnityInstance(canvas, config, (progress) => {
                    // Обновляем прогресс загрузки Unity
                    gameState.loadingProgress.unityProgress = progress;
                    updateTotalProgress();
                }).then((unityInstance) => {
                    gameState.instance = unityInstance;
                    myGameInstance = unityInstance;
                    gameState.isInitialized = true;
                    loadingCover.style.display = "none";
                }).catch((message) => {
                    console.error("Unity initialization error:", message);
                    alert(message);
                });
            };
            document.body.appendChild(script);
        } catch (error) {
            console.error("Game initialization failed:", error);
            alert("Failed to initialize game: " + error.message);
        }
    }

    function waitForGameInitialization() {
        return new Promise((resolve) => {
            const checkInitialization = () => {
                if (gameState.isInitialized) {
                    resolve();
                } else {
                    setTimeout(checkInitialization, 100);
                }
            };
            checkInitialization();
        });
    }

    async function InitSDK(photoSize, scopes) {
        await waitForGameInitialization();
        
        console.log('Init GAME');
        gameState.initGame = true;
        gameState.photoSizeForInit = photoSize;
        gameState.scopesForInit = scopes;

        if (gameState.initSDK == true) {
            ysdk.features.LoadingAPI?.ready();
            InitPlayer(photoSize, scopes);
        }
    }

    function NotAuthorized() {
        try {
            console.log('Authorized failed');
            let authJson = {
                "playerAuth": "rejected",
                "playerName": "unauthorized",
                "playerId": "unauthorized",
                "playerPhoto": "null"
            };
            gameState.instance.SendMessage('YandexGame', 'SetInitializationSDK', JSON.stringify(authJson));
        } catch (e) {
            console.error('CRASH Not Authorized: ', e.message);
        }
    }
    initializeGame().catch(error => {
        console.error("Failed to start game:", error);
    });
    function InitPlayer(photoSize, _scopes) {
        try {
            return ysdk.getPlayer({scopes: _scopes}).then(_player => {

                player = _player;

                let playerName = player.getName();
                let playerPhoto = player.getPhoto(photoSize);

                if (!_scopes) {
                    playerName = "anonymous";
                    playerPhoto = "null";
                }

                if (player.getMode() === 'lite') {

                    console.log('Not Authorized');
                    NotAuthorized();
                } else {
                    let authJson = {
                        "playerAuth": "resolved",
                        "playerName": playerName,
                        "playerId": player.getUniqueID(),
                        "playerPhoto": playerPhoto
                    };
                    myGameInstance.SendMessage('YandexGame', 'SetInitializationSDK', JSON.stringify(authJson));
                    window.focus();
                }
            }).catch(e => {
                console.error('Authorized err: ', e.message);
                NotAuthorized();
            });
        } catch (e) {
            console.error('CRASH init Player: ', e.message);
            window.focus();
        }
    }

    function OpenAuthDialog(photoSize, scopes) {
        try {
            ysdk.auth.openAuthDialog().then(() => {
                InitPlayer(photoSize, scopes);
            }).catch(() => {
                InitSDK(photoSize, scopes);
            });
        } catch (e) {
            console.log('CRASH Open Auth Dialog: ', e.message);
        }
    }

    function FullAdShow() {
       return;
    }

    function RewardedShow(id) {
     
                            console.log('Reward Video Ad. Id: ' + id);
                            myGameInstance.SendMessage('YandexGame', 'RewardVideo', id);
                        
    }

    function StickyAdActivity(show) {
        
                        ysdk.adv.hideBannerAdv();
                  
    }

    function InitPayments() {
        try {
            ysdk.getPayments().then(_payments => {
                console.log('Purchases are available');
                payments = _payments;                
            }).catch(e => {
                console.log('Purchases are not available', e.message);
            })
        } catch (e) {
            console.error('CRASH Init Payments: ', e.message);
        }
    }

    function BuyPayments(id) {
    
                    console.log('Purchase Success');
                    myGameInstance.SendMessage('YandexGame', 'OnPurchaseSuccess', id);
                    window.focus();
        
    }
    
    function GetPayments() {
        try {
            if (payments != null) {
                payments.getCatalog()
                    .then(products => {
                        let productID = [products.length];
                        let title = [products.length];
                        let description = [products.length];
                        let imageURI = [products.length];
                        let priceValue = [products.length];
                        let purchased = [products.length];
    
                        for (i = 0; i < products.length; i++) {
                            productID[i] = products[i].id;
                            title[i] = products[i].title;
                            description[i] = products[i].description;
                            imageURI[i] = products[i].imageURI;
                            priceValue[i] = products[i].priceValue;
                            purchased[i] = 0;
                        }
    
                        payments.getPurchases().then(purchases => {
                            for (i1 = 0; i1 < products.length; i1++) {
                                for (i2 = 0; i2 < purchases.length; i2++) {
                                    if (products[i1].id === purchases[i2].productID){
                                        purchased[i1]++;
                                    }
                                }
                            }
                        })
                            .then(() => {
                                var jsonPayments = {
                                    "id": productID,
                                    "title": title,
                                    "description": description,
                                    "imageURI": imageURI,
                                    "priceValue": priceValue,
                                    "purchased": purchased
                                };
                                myGameInstance.SendMessage('YandexGame', 'PaymentsEntries', JSON.stringify(jsonPayments));
                            })
                    });
            }
            else{
                console.log('Get Payments: payments == null');
            }
        } catch (e) {
            console.error('CRASH Get Payments: ', e.message);
        }
    }

    function DeletePurchase(id) {
        try {
            if (payments != null) {
                payments.getPurchases().then(purchases => {
                    for(i = 0; i < purchases.length; i++){
                        if (purchases[i].productID === id)
                            payments.consumePurchase(purchases[i].purchaseToken);
                    }
                });
            }
            else console.log('Delete Purchase: payments == null');
        } catch (e) {
            console.error('CRASH Delete Purchase: ', e.message);
        }
    }

    function DeleteAllPurchases() {
        try {
            if (payments != null) {
                payments.getPurchases().then(purchases => {
                    for(i = 0; i < purchases.length; i++){
                        payments.consumePurchase(purchases[i].purchaseToken);
                    }
                });
            }
            else console.log('Delete All Purchases: payments == null');
        } catch (e) {
            console.error('CRASH Delete All Purchases: ', e.message);
        }
    }

    function SaveCloud(jsonData, flush) {
        try {
            player.setData({
                saves: [jsonData],
            }, flush);
        } catch (e) {
            console.error('CRASH Save Cloud: ', e.message);
        }
    }

    function LoadCloud() {
        try {
            player.getData(["saves"]).then(data => {
                if (data.saves) {
                    myGameInstance.SendMessage('YandexGame', 'SetLoadSaves', JSON.stringify(data.saves));
                } else {
                    myGameInstance.SendMessage('YandexGame', 'SetLoadSaves', "noData");
                }
            }).catch(() => {
                console.error('getData Error!');
                myGameInstance.SendMessage('YandexGame', 'SetLoadSaves', "noData");
            });
        } catch (e) {
            console.error('CRASH Load saves Cloud: ', e.message);
            myGameInstance.SendMessage('YandexGame', 'SetLoadSaves', "noData");
        }
    }

    function InitLeaderboard() {
        try {
            ysdk.getLeaderboards().then(_lb => {
                leaderboard = _lb
                myGameInstance.SendMessage('YandexGame', 'InitializedLB');
            });
        } catch (e) {
            console.error('CRASH Init Leaderboard: ', e.message);
        }
    }

    function SetLeaderboardScores(_name, score) {
        try {
            ysdk.getLeaderboards()
                .then(leaderboard => {
                    leaderboard.setLeaderboardScore(_name, score);
                });
        } catch (e) {
            console.error('CRASH Set Leader board Scores: ', e.message);
        }
    }

    function GetLeaderboardScores(nameLB, maxPlayers, quantityTop, quantityAround, photoSize, auth) {
        if (auth) {
            try {
                ysdk.getLeaderboards()
                    .then(leaderboard => {
                        leaderboard.getLeaderboardEntries('' + nameLB, {
                            quantityTop: quantityTop,
                            includeUser: true,
                            quantityAround: quantityAround
                        })
                            .then(res => {
                                EntriesLB(res, nameLB, maxPlayers, photoSize);
                            });
                    });
            } catch (e) {
                console.error('CRASH Get Leaderboard Scores: ', e.message);
            }
        } else {
            try {
                ysdk.getLeaderboards()
                    .then(leaderboard => {
                        leaderboard.getLeaderboardEntries('' + nameLB, {quantityTop: quantityTop})
                            .then(res => {
                                EntriesLB(res, nameLB, maxPlayers, photoSize);
                            });
                    });
            } catch (e) {
                console.error('CRASH Get Leaderboard Scores: ', e.message);
            }
        }
    }

    function EntriesLB(res, nameLB, maxPlayers, photoSize) {
        let LeaderboardEntriesText = '';

        let playersCount;
        if (res.entries.length < maxPlayers) {
            playersCount = res.entries.length;
        } else {
            playersCount = maxPlayers;
        }

        let rank = [maxPlayers];
        let photo = [maxPlayers];
        let playersName = [maxPlayers];
        let scorePlayers = [maxPlayers];

        for (i = 0; i < playersCount; i++) {
            rank[i] = res.entries[i].rank;
            scorePlayers[i] = res.entries[i].score;

            if (photoSize === 'nonePhoto' || res.entries[i].player.scopePermissions.avatar !== "allow") {
                photo[i] = 'nonePhoto';
            } else {
                photo[i] = res.entries[i].player.getAvatarSrc(photoSize);
            }

            if (res.entries[i].player.scopePermissions.public_name !== "allow") {
                playersName[i] = "anonymous";
            } else {
                playersName[i] = res.entries[i].player.publicName;
            }

            LeaderboardEntriesText += rank[i] + '. ' + playersName[i] + ": " + scorePlayers[i] + '\n';
        }

        if (playersCount === 0) {
            LeaderboardEntriesText = 'No data';
        }

        let jsonLB = {
            "nameLB": nameLB,
            "entries": LeaderboardEntriesText,
            "rank": rank,
            "photo": photo,
            "playersName": playersName,
            "scorePlayers": scorePlayers
        };
        myGameInstance.SendMessage('YandexGame', 'LeaderboardEntries', JSON.stringify(jsonLB));
    }

    function LanguageRequest() {
        try {
            myGameInstance.SendMessage('YandexGame', 'SetLanguage', ysdk.environment.i18n.lang);
        } catch (e) {
            console.error('CRASH Language Request: ', e.message);
        }
    }

    function RequestingEnvironmentData() {
        try {
            let jsonEnvir = {
                "language": ysdk.environment.i18n.lang,
                "domain": ysdk.environment.i18n.tld,
                "deviceType": ysdk.deviceInfo.type,
                "isMobile": ysdk.deviceInfo.isMobile(),
                "isDesktop": ysdk.deviceInfo.isDesktop(),
                "isTablet": ysdk.deviceInfo.isTablet(),
                "isTV": ysdk.deviceInfo.isTV(),
                "appID": ysdk.environment.app.id,
                "browserLang": ysdk.environment.browser.lang,
                "payload": ysdk.environment.payload,
                "promptCanShow": promptCanShow,
                "reviewCanShow": reviewCanShow
            };
            myGameInstance.SendMessage('YandexGame', 'SetEnvironmentData', JSON.stringify(jsonEnvir));
        } catch (e) {
            console.error('CRASH Requesting Environment Data: ', e.message);
        }
    }

    function Review() {
        try {
            ysdk.feedback.canReview()
                .then(({ value, reason }) => {
                    if (value) {
                        ysdk.feedback.requestReview().then(({feedbackSent}) => {
                            console.log('feedbackSent ', feedbackSent);
                            if (feedbackSent)
                                myGameInstance.SendMessage('YandexGame', 'ReviewSent', 'true');
                            else myGameInstance.SendMessage('YandexGame', 'ReviewSent', 'false');
                            window.focus();
                        })
                    }
                    else {
                        console.log('reviewCanShow = false', reason)
                        window.focus();
                    }
                })
        } catch (e) {
            console.error('CRASH Review: ', e.message);
            window.focus();
        }
    }

    function PromptShow() {
        try {
            ysdk.shortcut.showPrompt()
                .then(result => {
                    console.log('Shortcut created?:', result);
                    if (result.outcome === 'accepted') {
                        console.log('Prompt Success');
                        myGameInstance.SendMessage('YandexGame', 'OnPromptSuccess');
                    }
                    else {
                        myGameInstance.SendMessage('YandexGame', 'OnPromptFail');
                    }
                    window.focus();
                });
        } catch (e) {
            console.error('CRASH Prompt Show: ', e.message);
            window.focus();
        }
    }

    function PaintRBT(rbt) {
        try {
            document.getElementById(rbt).style.background = '#ff0000';
        } catch (e) {
            console.error('CRASH Paint RBT: ', e.message);
        }
    }

    function StaticRBTDeactivate() {
    }

    document.body.appendChild(script);
</script>


</body></html>
</script><link href="https://cdn.jsdelivr.net/gh/linkd1/g@e079e474647ea113968cdc140ca97380be6409af/BANKROBBERY2/TemplateData/style.css" rel="stylesheet">
    <meta charset="utf-8">
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type">
    <meta content="width=device-width, initial-scale=1.0, user-scalable=no" name="viewport">
	<title></title>

    
<script>
/* mp-start */

var _params = gadgets.util.getUrlParameters();
if (_params['exp_rpc_js'] != 1) {
  var url = _params['parent'] + '/ig/ifpc_relay';
  gadgets.rpc.setRelayUrl('..', url, true);
}
/* mp-end */
</script><style type="text/css" id="operaUserStyle">

Drive Mad
<!DOCTYPE html>
<html lang="en-us">

<head>
  <base href="https://cdn.jsdelivr.net/gh/genizy/dmad-poki@49b5ab6b987f5f3be58f9dae59c92e8fc1aab9b0/">
  <script>
  window.assgdd = {
    "ancestorOrigins": {
        "0": "https://games.poki.com",
        "1": "https://poki.com"
    },
    "href": "https://f9564e4e-ef25-4e4b-ba67-cb11a1576bbd.poki-gdn.com/cc1bc57a-e355-4696-97c2-097bf6188606/index.html?country=US&url_referrer=https%3A%2F%2Fpoki.com%2F&site_id=3&iso_lang=en&poki_url=https%3A%2F%2Fpoki.com%2Fen%2Fg%2Fdrive-mad&hoist=yes&nonPersonalized=n&cloudsavegames=n&familyFriendly=n&categories=78%2C93%2C96%2C103%2C377%2C390%2C400%2C893%2C929%2C1126%2C1139%2C1140%2C1141%2C1143%2C1147%2C1163%2C1185%2C1190%2C1193%2C1197&special_condition=landing&game_id=f9564e4e-ef25-4e4b-ba67-cb11a1576bbd&game_version_id=cc1bc57a-e355-4696-97c2-097bf6188606&inspector=0",
    "origin": "https://f9564e4e-ef25-4e4b-ba67-cb11a1576bbd.poki-gdn.com",
    "protocol": "https:",
    "host": "f9564e4e-ef25-4e4b-ba67-cb11a1576bbd.poki-gdn.com",
    "hostname": "f9564e4e-ef25-4e4b-ba67-cb11a1576bbd.poki-gdn.com",
    "port": "",
    "pathname": "/cc1bc57a-e355-4696-97c2-097bf6188606/index.html",
    "search": "?country=US&url_referrer=https%3A%2F%2Fpoki.com%2F&site_id=3&iso_lang=en&poki_url=https%3A%2F%2Fpoki.com%2Fen%2Fg%2Fdrive-mad&hoist=yes&nonPersonalized=n&cloudsavegames=n&familyFriendly=n&categories=78%2C93%2C96%2C103%2C377%2C390%2C400%2C893%2C929%2C1126%2C1139%2C1140%2C1141%2C1143%2C1147%2C1163%2C1185%2C1190%2C1193%2C1197&special_condition=landing&game_id=f9564e4e-ef25-4e4b-ba67-cb11a1576bbd&game_version_id=cc1bc57a-e355-4696-97c2-097bf6188606&inspector=0",
    "hash": ""
}
  </script>
  <meta charset="utf-8">
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">

  <title>Drive Mad</title>
  <meta name="description" content="">
  <meta name="google" content="notranslate">

  <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
  <link rel="stylesheet" href="webapp/fancade.css">
  <link rel="icon" href="webapp/favicon.ico">

  <!-- POKI SDK -->
  <script src="poki-sdk.js" ></script>
</head>

<body id="body">

  <!-- Modal dialog div -->
  <div id="modal_parent">
    <div id="modal_content">
      <span id="modal_close_button">&times;</span>
      <div id="store_link_modal_content" class="modal_inner"></div>
      <div id="share_file_modal_content" class="modal_inner"></div>
    </div>
  </div>

  <!-- 
      Game canvas and overlay. Emscripten makes some assumptions about how the canvas is positioned in order
      to translate document to game coordinates
    -->
  <div id="canvas_border" class="emscripten_border">
    <div id="play_content" class="middle center">
      <div class="edge">
        <div class="box">
          <div class="black">
            <img src="webapp/cover.jpg" class="cover">
            <p class="title">Drive Mad</p>
            <p class="author">Fancade</p>
          </div>
        </div>
      </div>
      <div id="progress_or_play">
        <progress id="progress" class="loading" value="0" max="100"></progress>
      </div>
      <p class="description"></p>
    </div>
    <canvas class="emscripten" id="canvas" tabindex=-1>
    </canvas>
    <div id="gradient"></div>
    <div id="webview_content"></div>
  </div>

  <!-- Manual JS, Called from WASM -->
  <script type="text/javascript" src="webapp/source_min.js"></script>

  <!-- Auto generated JS -->
  <script type="text/javascript" src="webapp/index.js"></script>
</body>

</html>




"""
    return html

@app.route("/Friday_Night_Funking2")
def FNF2():
	html="""
<!DOCTYPE html>
<html lang="en">
<head>
<base href="https://cdn.jsdelivr.net/gh/genizy/fridayfunk/"/>
<meta charset="utf-8"/>
<title>Friday Night Funkin'</title>
<meta id="viewport" name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
<meta name="apple-mobile-web-app-capable" content="yes"/>
<link rel="shortcut icon" type="image/png" href="https://cdn.jsdelivr.net/gh/genizy/fridayfunk/favicon.png"/>
<script type="text/javascript" src="https://cdn.jsdelivr.net/gh/genizy/fridayfunk/Funkin.js"></script>
<script>
window.addEventListener ("touchmove", function (event) { event.preventDefault (); }, { capture: false, passive: false });
if (typeof window.devicePixelRatio != 'undefined' && window.devicePixelRatio > 2) {
var meta = document.getElementById ("viewport");
meta.setAttribute ('content', 'width=device-width, initial-scale=' + (2 / window.devicePixelRatio) + ', user-scalable=no');
}
</script>
<style>
html,body { margin: 0; padding: 0; height: 100%; overflow: hidden; }
#openfl-content { background: #000000; width: 100%; height: 100%; }
@font-face {
font-family: '5by7';
src: url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/5by7.eot?#iefix') format('embedded-opentype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/5by7.woff') format('woff'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/5by7.ttf') format('truetype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/5by7.svg#5by7') format('svg');
font-weight: normal;
font-style: normal;
}
@font-face {
font-family: '5by7 Bold';
src: url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/5by7_b.eot?#iefix') format('embedded-opentype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/5by7_b.woff') format('woff'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/5by7_b.ttf') format('truetype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/5by7_b.svg#5by7%20Bold') format('svg');
font-weight: normal;
font-style: normal;
}
@font-face {
font-family: 'DS-Digital';
src: url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/DS-DIGI.eot?#iefix') format('embedded-opentype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/DS-DIGI.TTF') format('truetype');
font-weight: normal;
font-style: normal;
}
@font-face {
font-family: 'DS-Digital Bold';
src: url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/DS-DIGIB.eot?#iefix') format('embedded-opentype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/DS-DIGIB.TTF') format('truetype');
font-weight: normal;
font-style: normal;
}
@font-face {
font-family: 'DS-Digital Italic';
src: url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/DS-DIGII.eot?#iefix') format('embedded-opentype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/DS-DIGII.TTF') format('truetype');
font-weight: normal;
font-style: normal;
}
@font-face {
font-family: 'DS-Digital Bold Italic';
src: url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/DS-DIGIT.eot?#iefix') format('embedded-opentype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/DS-DIGIT.TTF') format('truetype');
font-weight: normal;
font-style: normal;
}
@font-face {
font-family: 'Inconsolata Black';
src: url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-Black.eot?#iefix') format('embedded-opentype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-Black.woff') format('woff'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-Black.ttf') format('truetype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-Black.svg#Inconsolata%20Black') format('svg');
font-weight: normal;
font-style: normal;
}
@font-face {
font-family: 'Inconsolata Bold';
src: url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-Bold.eot?#iefix') format('embedded-opentype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-Bold.woff') format('woff'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-Bold.ttf') format('truetype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-Bold.svg#Inconsolata%20Bold') format('svg');
font-weight: normal;
font-style: normal;
}
@font-face {
font-family: 'Inconsolata ExtraBold';
src: url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-ExtraBold.eot?#iefix') format('embedded-opentype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-ExtraBold.woff') format('woff'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-ExtraBold.ttf') format('truetype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-ExtraBold.svg#Inconsolata%20ExtraBold') format('svg');
font-weight: normal;
font-style: normal;
}
@font-face {
font-family: 'Inconsolata ExtraLight';
src: url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-ExtraLight.eot?#iefix') format('embedded-opentype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-ExtraLight.woff') format('woff'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-ExtraLight.ttf') format('truetype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-ExtraLight.svg#Inconsolata%20ExtraLight') format('svg');
font-weight: normal;
font-style: normal;
}
@font-face {
font-family: 'Inconsolata Medium';
src: url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-Medium.eot?#iefix') format('embedded-opentype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-Medium.woff') format('woff'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-Medium.ttf') format('truetype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-Medium.svg#Inconsolata%20Medium') format('svg');
font-weight: normal;
font-style: normal;
}
@font-face {
font-family: 'Inconsolata Regular';
src: url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-Regular.eot?#iefix') format('embedded-opentype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-Regular.woff') format('woff'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-Regular.ttf') format('truetype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-Regular.svg#Inconsolata%20Regular') format('svg');
font-weight: normal;
font-style: normal;
}
@font-face {
font-family: 'Inconsolata SemiBold';
src: url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-SemiBold.eot?#iefix') format('embedded-opentype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-SemiBold.woff') format('woff'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-SemiBold.ttf') format('truetype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Inconsolata-SemiBold.svg#Inconsolata%20SemiBold') format('svg');
font-weight: normal;
font-style: normal;
}
@font-face {
font-family: 'Pixel Arial 11 Bold';
src: url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/pixel.eot?#iefix') format('embedded-opentype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/pixel.woff') format('woff'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/pixel.otf') format('truetype');
font-weight: normal;
font-style: normal;
}
@font-face {
font-family: 'Quantico-Bold';
src: url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Quantico-Bold.eot?#iefix') format('embedded-opentype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Quantico-Bold.woff') format('woff'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Quantico-Bold.ttf') format('truetype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Quantico-Bold.svg#Quantico-Bold') format('svg');
font-weight: normal;
font-style: normal;
}
@font-face {
font-family: 'Quantico-BoldItalic';
src: url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Quantico-BoldItalic.eot?#iefix') format('embedded-opentype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Quantico-BoldItalic.woff') format('woff'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Quantico-BoldItalic.ttf') format('truetype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Quantico-BoldItalic.svg#Quantico-BoldItalic') format('svg');
font-weight: normal;
font-style: normal;
}
@font-face {
font-family: 'Quantico-Italic';
src: url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Quantico-Italic.eot?#iefix') format('embedded-opentype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Quantico-Italic.woff') format('woff'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Quantico-Italic.ttf') format('truetype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Quantico-Italic.svg#Quantico-Italic') format('svg');
font-weight: normal;
font-style: normal;
}
@font-face {
font-family: 'Quantico';
src: url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Quantico-Regular.eot?#iefix') format('embedded-opentype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Quantico-Regular.woff') format('woff'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Quantico-Regular.ttf') format('truetype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/Quantico-Regular.svg#Quantico') format('svg');
font-weight: normal;
font-style: normal;
}
@font-face {
font-family: 'VCR OSD Mono';
src: url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/vcr.eot?#iefix') format('embedded-opentype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/vcr.woff') format('woff'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/vcr.ttf') format('truetype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/assets/fonts/vcr.svg#VCR%20OSD%20Mono') format('svg');
font-weight: normal;
font-style: normal;
}
@font-face {
font-family: 'Nokia Cellphone FC Small';
src: url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/flixel/fonts/nokiafc22.eot?#iefix') format('embedded-opentype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/flixel/fonts/nokiafc22.woff') format('woff'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/flixel/fonts/nokiafc22.ttf') format('truetype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/flixel/fonts/nokiafc22.svg#Nokia%20Cellphone%20FC%20Small') format('svg');
font-weight: normal;
font-style: normal;
}
@font-face {
font-family: 'Monsterrat';
src: url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/flixel/fonts/monsterrat.eot?#iefix') format('embedded-opentype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/flixel/fonts/monsterrat.woff') format('woff'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/flixel/fonts/monsterrat.ttf') format('truetype'),
url('https://cdn.jsdelivr.net/gh/genizy/fridayfunk/flixel/fonts/monsterrat.svg#Monsterrat') format('svg');
font-weight: normal;
font-style: normal;
}

</style>
</head>
<body>
<noscript>This webpage makes extensive use of JavaScript. Please enable JavaScript in your web browser to view this page.</noscript>
<div id="openfl-content"></div>
<script type="text/javascript">
lime.embed ("Funkin", "openfl-content", 1280, 720, { parameters: {} });
</script>
</body>
</html>



"""

	return html

@app.route("/NMTR")
def NMTR():
	html="""
<Module>


<!-- Ultimate Game Stash file--> 
<!-- For the regularly updating doc go to https://docs.google.com/document/d/1_FmH3BlSBQI7FGgAQL59-ZPe8eCxs35wel6JUyVaG8Q/ -->



<Module>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
  <title>really cool flash game</title>
  <style>
    html, body {
      margin: 0;
      padding: 0;
      background: black;
      overflow: hidden;
      height: 100%;
      width: 100%;
    }
    #flash-container {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background: black;
      overflow: hidden;
    }
    .black-box {
      position: fixed;
      background: black;
      z-index: 10;
    }
    #box-top {
      top: 0;
      left: 0;
      width: 100%;
      height: 0;
"""
	return html

@app.route("/FN")
def FN():
	html="""

<!DOCTYPE html>


<!-- Ultimate Game Stash file--> 
<!-- For the regularly updating doc go to https://docs.google.com/document/d/1_FmH3BlSBQI7FGgAQL59-ZPe8eCxs35wel6JUyVaG8Q/ --> 


<html lang="en">

<head>
  <base href="https://cdn.jsdelivr.net/gh/genizy/UGS-Assets@main/fruit%20ninja/">
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover" />
  <meta http-equiv="X-UA-Compatible" content="ie=edge" />

  <meta name="theme-color" content="#000000" />

  <link rel="manifest" href="./manifest.json" />

  <script src=poki-sdk.js></script>

  <meta name="mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-capable" content="yes" />
  <meta name="application-name" content="Fruit Ninja" />
  <meta name="apple-mobile-web-app-title" content="Fruit Ninja" />
  <meta name="msapplication-starturl" content="./" />
  <!-- <script type="text/javascript" src="https://storms.com/lib/h5Sdk/v1/h5Sdk.js"></script> -->

  <title>Fruit Ninja</title>
  <style>
    @font-face {
      font-family: gangofchinese;
      src: url('assets/font/gangofchinese.ttf');
    }

    html,
    body {
      height: 100%;
      width: 100% !important;
      margin: 0;
      background-color: #000000 !important;
    }

    .fontLoader {
      position: absolute;
      left: -1000px;
      visibility: hidden;
    }

    #phaser-canvas {
      margin: 0 auto;
      background-color: #000000;
    }

    body,
    #content {
      height: 100vh !important;
      max-height: 100vh !important;
    }

    #divAds,
    #tempads {
      display: none;
    }

    /* canvas{
          width: 100%;
          height: 100%;
          display: grid !important;
          grid-area: 1/1;
          margin-top: 0 !important;
          margin-bottom: 0 !important;
          padding: 0 !important;
          max-width: 100% !important;
          max-height: 100vh !important;
      } */

    #enable3d-three-canvas,
    #enable3d-phaser-canvas {
      min-width: 100%;
      max-width: 100%;
      max-width: -webkit-fill-available;
      max-width: -moz-available;
      max-width: -webkit-fill-available;
      max-width: fill-available;
      margin: 0 auto;
    }

    /* @media screen and (max-width: 768px) {
        #enable3d-three-canvas, #enable3d-phaser-canvas {
          min-width: auto !important;
          max-width: auto;
          width: 960px;
          height: auto;
          margin: 0 auto;
        }
      } */

    @media (min-aspect-ratio: 1.85) {

      #enable3d-three-canvas,
      #enable3d-phaser-canvas {
        width: 960px;
        min-width: 640px;
      }
    }

    @media (min-aspect-ratio: 8/4) {

      #enable3d-three-canvas,
      #enable3d-phaser-canvas {
        min-width: 640px;
        /* background-color: aquamarine; */
      }
    }
  </style>

  <noscript>Please enable javascript to continue using this application.</noscript>

  <!-- <script async
        data-ad-client="ca-pub-6934234812187351"
        data-ad-frequency-hint= "30s"
        src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">
    </script>
    <script>window.adsbygoogle = window.adsbygoogle || [];
        const adBreak =  adConfig = function(o) {adsbygoogle.push(o);}
    </script> -->
  <!-- installs the serviceWorker -->
  <!-- <script>
      if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
          navigator.serviceWorker.register('./sw.js')
        })
      }
    </script> -->
</head>

<body>
  <div class="fontLoader" style="font-family: gangofchinese;">-</div>
  <div class="fontLoader" style="font-family: gangofchinese;">-</div>
  <div id="content">
    <div id="phaser-canvas"></div>
  </div>
  <!-- <div id="phaser-game"></div> -->
  <style id="injectStyles">
    html,
    body {
      background: none !important;
    }
  </style>
  <script type="text/javascript" src="vendors.bundle.js"></script>
  <script type="text/javascript" src="main.bundle.js"></script>
</body>

</html>
clfruitninja.html
External
Displaying clfruitninja.html.

"""
	return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port_num)
