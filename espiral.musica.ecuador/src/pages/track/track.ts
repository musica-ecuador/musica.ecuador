import { Component,OnInit,ViewChild,ElementRef, Renderer2, AfterViewInit } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

import { LoadingController } from 'ionic-angular';



import { TrackService } from '../../providers/track/track'

/**
 * Generated class for the TrackPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-track',
  templateUrl: 'track.html',
})
export class TrackPage implements OnInit,AfterViewInit   {

  private loading:any;

  @ViewChild('playeraudio') player_audio: ElementRef;

  
  public albumId: string;
  public albumName:string;
  tracks: any[];

  public playing: boolean = false;
  public trackIndex: number  = 0;
  public trackCount : number  = 0;
  public trackPlaying : any;
  
 
  constructor(public navCtrl: NavController,
     public navParams: NavParams, 
     public loadingCtrl: LoadingController, 
     private renderer: Renderer2, 
     public trackService:TrackService) {
    this.albumId = this.navParams.get('albumId');
    this.albumName = this.navParams.get('albumName');
  }


  ngOnInit(): void {
    this.loading = this.loadingCtrl.create({
      content: 'Por favor espere...'
    });

    this.loading.present();

    this.findAll();    
  }
  
  ngAfterViewInit() {
    console.log("ngAfterViewInit");
    console.log(this.player_audio);
    console.log(this.player_audio.nativeElement.value);
    
    this.renderer.listen(this.player_audio.nativeElement, 'ended', () => this.OnEnded());
    this.renderer.listen(this.player_audio.nativeElement, 'play', () => this.OnPlay());
    this.renderer.listen(this.player_audio.nativeElement, 'pause', () => this.OnPause());

  }

  findAll(): void {
     this.trackService.getTracksAlbum(this.albumId).then(tracks => {
       this.tracks = tracks;
       this.trackCount = this.tracks.length;

       console.log(this.player_audio);
      
       /*
       this.player_audio.nativeElement.onended = this.OnEnded;
       this.player_audio.nativeElement.onplay = this.OnPlay 
       this.player_audio.nativeElement.onpause = this.OnPause;
      */

       if (this.tracks.length>0){
        this.trackIndex = 0;
        this.trackPlaying = this.tracks[this.trackIndex];
        this.player_audio.nativeElement.src = this.trackPlaying.preview;
        
       }else{
        this.trackIndex = -1;
        this.trackPlaying = null;
        this.player_audio.nativeElement.src = "#";
       }

       this.loading.dismissAll();
    });
  }
  
  playTrack(url,index){
    this.trackIndex = index;
    this.trackPlaying = this.tracks[this.trackIndex];

    this.player_audio.nativeElement.src = url;
    this.player_audio.nativeElement.play();

    this.playing = true;
  }

  loadTrack = function (id) {
    this.trackIndex = id;
    this.player_audio.nativeElement.src  = this.tracks[id].preview;
  }

  OnEnded(){
    console.log("The audio has ended"); 

    if ((this.trackIndex + 1) < this.trackCount) {
      this.trackIndex++;
      this.loadTrack(this.trackIndex);

      var playPromise = this.player_audio.nativeElement.play();
       
      //TODO: Use in promise
      this.trackPlaying = this.tracks[this.trackIndex];
      this.playing = true;

      // In browsers that don’t yet support this functionality,
      // playPromise won’t be defined.
      if (playPromise !== undefined) {
        playPromise.then(function() {
          
          
          // Automatic playback started!
          console.log("Automatic playback started!..."); 
        }).catch(function(error) {
          console.log("Error play audio : " + error); 
          // Automatic playback failed.
          // Show a UI element to let the user manually start playback.
        });
      }

    } else {
      
      this.player_audio.nativeElement.pause();
      
      this.trackIndex = 0;
      this.loadTrack(this.trackIndex);

      this.trackPlaying = this.tracks[this.trackIndex];
      this.playing = true;

    }
  }

  OnPlay(){
    console.log("The audio has started to play"); 
  }

  OnPause(){
    console.log("The audio has been paused"); 
    this.playing = false;
  }

   
  
 

}
