import { Component,OnInit } from '@angular/core';
import {  NavController, NavParams } from 'ionic-angular';
import { LoadingController } from 'ionic-angular';

import { AlbumPage } from "../album/album"
import { ArtistService } from "../../providers/artist/artist";

/**
 * Generated class for the ArtistPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

//@IonicPage()
@Component({
  selector: 'page-artist',
  templateUrl: 'artist.html',
})
export class ArtistPage implements OnInit  {
  
  loading:any;

  artists: any[];
  private artistsInterna: any[];

  constructor(public navCtrl: NavController,
     public navParams: NavParams,
     public loadingCtrl: LoadingController,
     public artistService: ArtistService) {


  }

  ngOnInit(): void {

    this.loading = this.loadingCtrl.create({
      content: 'Por favor espere...'
    });

    
    this.findAll();    
  }

  findAll(): void {
    this.loading.present();

     this.artistService.findAll().then(artists => 
      {
        this.artists = artists;
        this.artistsInterna = this.artists;
        
        this.loading.dismissAll();
      }
    );
  }

  showAlbum(artistId,artistName){
    console.log(artistId);
    this.navCtrl.push(AlbumPage,{ artistId:artistId, artistName:artistName });
  }

  
  openSpotify(url){
    //TODO: switter plataform, (Mobile o Browser)
    window.open(url);
  }


  filter(ev) {
    // Reset items back to all of the items
    this.artists = this.artistsInterna;

    // set val to the value of the ev target
    var val = ev.target.value;

    // if the value is an empty string don't filter the items
    if (val && val.trim() != '') {
      this.artists = this.artists.filter((item) => {

        return (item.name.toLowerCase().indexOf(val.toLowerCase()) > -1);
      })
    }
  }
  

  ionViewDidLoad() {
    console.log('Artista Pagina, Cargada');
  }

}
