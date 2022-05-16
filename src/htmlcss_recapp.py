

    main_html = """
    <html>
      <head>
        <script>
            let log = console.log.bind(console),
              id = val => document.getElementById(val),
              ul = id('ul'),
              gUMbtn = id('gUMbtn'),
              start = id('start'),
              stop = id('stop'),
              stream,
              recorder,
              counter=1,
              chunks,
              media;


            gUMbtn.onclick = e => {
              let mv = id('mediaVideo'),
                  mediaOptions = {
                    video: {
                      tag: 'video',
                      type: 'video/webm',
                      ext: '.mp4',
                      gUM: {video: true, audio: true}
                    },
                    audio: {
                      tag: 'audio',
                      type: 'audio/ogg',
                      ext: '.ogg',
                      gUM: {audio: true}
                    }
                  };
              media = mv.checked ? mediaOptions.video : mediaOptions.audio;
              navigator.mediaDevices.getUserMedia(media.gUM).then(_stream => {
                stream = _stream;
                id('gUMArea').style.display = 'none';
                id('btns').style.display = 'inherit';
                start.removeAttribute('disabled');
                recorder = new MediaRecorder(stream);
                recorder.ondataavailable = e => {
                  chunks.push(e.data);
                  if(recorder.state == 'inactive')  makeLink();
                };
                log('got media successfully');
              }).catch(log);
            }

            start.onclick = e => {
              start.disabled = true;
              stop.removeAttribute('disabled');
              chunks=[];
              recorder.start();
            }


            stop.onclick = e => {
              stop.disabled = true;
              recorder.stop();
              start.removeAttribute('disabled');
            }



            function makeLink(){
              let blob = new Blob(chunks, {type: media.type })
                , url = URL.createObjectURL(blob)
                , li = document.createElement('li')
                , mt = document.createElement(media.tag)
                , hf = document.createElement('a')
              ;
              mt.controls = true;
              mt.src = url;
              hf.href = url;
              hf.download = `${counter++}${media.ext}`;
              hf.innerHTML = `donwload ${hf.download}`;
              li.appendChild(mt);
              li.appendChild(hf);
              ul.appendChild(li);
            }

        </script>
        <title>MediaRecorder API - Sample</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="keywords" content="WebRTC getUserMedia MediaRecorder API">
        <link type="text/css" rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
        <style>
          button{
            margin: 10px 5px;
          }
          li{
            margin: 10px;
          }
          body{
            width: 90%;
            height: 500px;
            max-width: 960px;
            margin: 0px auto;
          }
          #btns{
            display: none;
          }
          h1{
            margin: 100px;
          }
        </style>
      </head>
      <body>
        <h1> MediaRecorder API example</h1>

        <p> For now it is supported only in Firefox(v25+) and Chrome(v47+)</p>
        <div id='gUMArea'>
          <div>
          Record:
            <input type="radio" name="media" value="video" checked id='mediaVideo'>Video
            <input type="radio" name="media" value="audio">audio
          </div>
          <button class="btn btn-default"  id='gUMbtn'>Request Stream</button>
        </div>
        <div id='btns'>
          <button  class="btn btn-default" id='start'>Start</button>
          <button  class="btn btn-default" id='stop'>Stop</button>
        </div>
        <div>
          <ul  class="list-unstyled" id='ul'></ul>
        </div>
        <script src="https://code.jquery.com/jquery-2.2.0.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
      </body>
    </html>
    """

    # Execute your app
    # st.title("Javascript example")
    # components.html(main_html, height=500)  # JavaScript works
