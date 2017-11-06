import { Component,OnInit } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

import { AlbumPage } from "../album/album"
import { ArtistService } from "../../providers/artist/artist";

/**
 * Generated class for the ArtistPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-artist',
  templateUrl: 'artist.html',
})
export class ArtistPage implements OnInit  {

  artists: any[];

  constructor(public navCtrl: NavController, public navParams: NavParams,public artistService: ArtistService) {
  }

  ngOnInit(): void {
    this.findAll();  

    
  }

  findAll(): void {
     this.artistService.findAll().then(artists => this.artists = artists);
  }

  showAlbum(artistId,artistName){
    console.log(artistId);
    this.navCtrl.push(AlbumPage,{ artistId:artistId, artistName:artistName });
  }

  
  openSpotify(url){
    //TODO: switter plataform, (Mobile o Browser)
    window.open(url);
  }

  ionViewDidLoad() {
    console.log('Artista Pagina, Cargada');
  }

}
