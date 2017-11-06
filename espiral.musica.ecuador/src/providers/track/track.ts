import { Injectable } from '@angular/core';
import { Headers, Http, RequestOptions } from '@angular/http';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/toPromise';


/*
  Generated class for the TrackProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class TrackService {

  url: string = 'http://localhost:1337/parse/classes/Track';
  private headers: Headers = new Headers();

  constructor(public http: Http) {
    this.headers.append('Content-Type', 'application/json');
    this.headers.append('X-Parse-Application-Id', '123');
    console.log('Hello ArtistProvider Provider');
  }


  getTracksAlbum(albumId: string): Promise<any[]> {
    let params = {
      "album":
      {
        "__type": "Pointer",
        "className": "Album",
        "objectId": albumId
      }
    };

   
    let urlTrack = this.url + "/?where=" + JSON.stringify(params);
  
    return this.http.get(urlTrack, { headers: this.headers })
      .toPromise()
      .then(response => response.json().results)
      .catch(this.handleError);
  }


  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }

}
