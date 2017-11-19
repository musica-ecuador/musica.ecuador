import { Injectable,EventEmitter } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/add/operator/map';

 
@Injectable()
export class YoutubeService {
  youtube: any = {
    ready: false,
    player: null,
    playerId: null,
    videoId: null,
    videoTitle: null,
    playerHeight: '100%',
    playerWidth: '100%'
  }

  constructor () {
      this.setupPlayer();
  }

  bindPlayer(elementId): void {
    this.youtube.playerId = elementId;
  };

  createPlayer(): void {
    return new window['YT'].Player(this.youtube.playerId, {
      height: this.youtube.playerHeight,
      width: this.youtube.playerWidth,
      playerVars: {
        rel: 0,
        showinfo: 0
      }
    });
  }

  loadPlayer(): void {
    if (this.youtube.ready && this.youtube.playerId) {
      if (this.youtube.player) {
      this.youtube.player.destroy();
      }
      this.youtube.player = this.createPlayer();
    }
  }

  setupPlayer () {
    // in production mode, the youtube iframe api script tag is loaded
    // before the bundle.js, so the 'onYouTubeIfarmeAPIReady' has
    // already been triggered
    // TODO: handle this in build or in nicer in code
    console.log ("Running Setup Player");
    window['onYouTubeIframeAPIReady'] = () => {
      if (window['YT']) {
         console.log('Youtube API is ready. onYouTubeIframeAPIReady');
         this.youtube.ready = true;
         this.bindPlayer('placeholder');
         this.loadPlayer();
      }
    };
    if (window['YT'] && window['YT'].Player) {
            console.log('Youtube API is ready window[YT]');
         this.youtube.ready = true;
         this.bindPlayer('placeholder');
         this.loadPlayer();
    }
  }

  launchPlayer(id, title):void {
    console.log('launchPlayer...');
    this.youtube.player.loadVideoById(id);
    this.youtube.videoId = id;
    this.youtube.videoTitle = title;
    return this.youtube;
  }
}