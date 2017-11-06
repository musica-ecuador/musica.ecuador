import { Component,OnInit } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

import { TrackPage } from '../track/track'


import { AlbumService } from '../../providers/album/album'
import { ArtistService } from "../../providers/artist/artist";


/**
 * Generated class for the AlbumPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-album',
  templateUrl: 'album.html',
})
export class AlbumPage implements OnInit  {

  public artistId: string;
  public artistName:string;
  albums: any[];
  artist: any;

  constructor(public navCtrl: NavController, public navParams: NavParams, public albumService:AlbumService,public artistService: ArtistService) {
    this.artistId = this.navParams.get('artistId');
    this.artistName = this.navParams.get('artistName');
    console.log(this.artistId);
  }

  ngOnInit(): void {
    //TODO: Chaining Promises
    this.getArtist();
    this.findAll();    
  }

  getArtist():void{
    this.artistService.get(this.artistId).then(items => {
        if (items.length===1){
          this.artist = items[0];
        }else{
          this.artist = null;
        }
        return this.artist;
      }
    );
  }


  findAll(): void {
     this.albumService.getAlbums(this.artistId)
     .then()
     .then(albums => this.albums = albums);
  }

  showTrack(albumId,albumName){
    this.navCtrl.push(TrackPage,{ albumId:albumId, albumName:albumName });
  }


  ionViewDidLoad() {
    console.log('ionViewDidLoad AlbumPage');
  }

}
