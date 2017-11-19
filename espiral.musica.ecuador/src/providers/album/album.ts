import { Injectable } from '@angular/core';
import { Headers, Http, RequestOptions } from '@angular/http';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/toPromise';

/*
  Generated class for the AlbumProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/

import {  AppSettings } from "../../app/settings";

@Injectable()
export class AlbumService {

  url: string = AppSettings.PARSE_SERVER + '/parse/classes/Album';
  private headers: Headers = new Headers();

  constructor(public http: Http) {
    this.headers.append('Content-Type', 'application/json');
    this.headers.append('X-Parse-Application-Id', AppSettings.PARSE_APPLICATION_ID);
  }


  getAlbums(artistId: string): Promise<any[]> {

    let query = {
      "artists":
      {
        "__type": "Pointer",
        "className": "Artist",
        "objectId": artistId
      }
    };
    let where = "where=" + JSON.stringify(query);
    let urlFinal = this.url + "?" + where;
    console.log(urlFinal);

    return this.http.get(urlFinal, { headers: this.headers })
      .toPromise()
      .then(response => response.json().results)
      .catch(this.handleError);
  }


  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }


}
