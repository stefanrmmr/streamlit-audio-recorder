# audio-react-recorder

> Audio / Voice Recorder w/ Audio Wave for React using the [Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)

[![NPM](https://img.shields.io/npm/v/audio-react-recorder.svg)](https://www.npmjs.com/package/audio-react-recorder) [![JavaScript Style Guide](https://img.shields.io/badge/code_style-standard-brightgreen.svg)](https://standardjs.com)

## Install

```bash
npm install --save audio-react-recorder
```

## DEMO

[AudioReactRecorder demo](https://doppelgunner.github.io/audio-react-recorder/)

## Usage

```jsx
import React, { Component } from 'react'

import AudioReactRecorder, { RecordState } from 'audio-react-recorder'

class App extends Component {
  constructor(props) {
    super(props)

    this.state = {
      recordState: null
    }
  }

  start = () => {
    this.setState({
      recordState: RecordState.START
    })
  }

  stop = () => {
    this.setState({
      recordState: RecordState.STOP
    })
  }

  //audioData contains blob and blobUrl
  onStop = (audioData) => {
    console.log('audioData', audioData)
  }

  render() {
    const { recordState } = this.state

    return (
      <div>
        <AudioReactRecorder state={recordState} onStop={this.onStop} />

        <button onClick={this.start}>Start</button>
        <button onClick={this.stop}>Stop</button>
      </div>
    )
  }
}
```

## Supported props

| Property name   | Type          | Default            | Description                                          |
| --------------- | ------------- | ------------------ | ---------------------------------------------------- |
| state           | string        | RecordState.NONE   | RecordState.(NONE,START,STOP,PAUSE)                  |
| type            | string        | audio/wav          | MIME type of the audio file                          |
| backgroundColor | string        | rgb(200, 200, 200) | Background color of the audio wave / canvas          |
| foregroundColor | string        | rgb(0, 0, 0)       | Foreground color of the audio wave / canvas          |
| canvasWidth     | number,string | 500                | Canvas width (you can use css to make it responsive) |
| canvasHeight    | number,string | 300                | canvas height                                        |

## License

MIT © [noobieprogrammer](https://github.com/noobieprogrammer)

## Buy me a coffee or just follow me

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=GCJGP8MTETUYU)

- [My Blog](https://noobieprogrammer.blogspot.com/)
- [Twitter](https://twitter.com/noobieprogrmmer)
- [Youtube](https://www.youtube.com/channel/UCpzMkMzGopmft5welUr8QZg)
