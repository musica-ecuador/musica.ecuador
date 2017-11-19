import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

/**
 * Generated class for the YoutubePage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-youtube',
  templateUrl: 'youtube.html',
})
export class YoutubePage {

  videos:any[] = [
    { title:'Soda Stereo - De Musica Ligera',video:'https://www.youtube.com/embed/OX-us7PEfkc?autoplay=1'},
    { title:'Soda Stereo - Signos',video:"https://www.youtube.com/embed/vNKUDiA2YQE"}
  ];

  

  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad YoutubePage');
    console.log(this.videos);
  }

}
