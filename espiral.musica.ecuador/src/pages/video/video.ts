import { Component,OnInit } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

//import { YoutubeService } from '../../providers/youtube/youtube'

/**
 * Generated class for the VideoPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-video',
  templateUrl: 'video.html',
})
export class VideoPage implements OnInit  {
/*
  constructor(public navCtrl: NavController, public navParams: NavParams, public ytPlayer: YoutubeService) {

  }
*/
  constructor(public navCtrl: NavController, public navParams: NavParams) {
    
      }

  ngOnInit(): void {

    //this.ytPlayer.launchPlayer("M7lc1UVf-VE", "Demo - Player - Youtube");

  }

 

  ionViewDidLoad() {
    console.log('ionViewDidLoad VideoPage');
  }

}
