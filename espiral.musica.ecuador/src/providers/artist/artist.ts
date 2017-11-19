import { Injectable } from '@angular/core';
import { Headers, Http, RequestOptions } from '@angular/http';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/toPromise';

import {  AppSettings } from "../../app/settings";

/*
  Generated class for the ArtistProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class ArtistService {

  url: string =  AppSettings.PARSE_SERVER +  '/parse/classes/Artist';
  private headers: Headers = new Headers();
 
  constructor(public http: Http) {
    this.headers.append('Content-Type', 'application/json');
    this.headers.append('X-Parse-Application-Id', AppSettings.PARSE_APPLICATION_ID);
    console.log('Hello ArtistProvider Provider');
    console.log('PARSE_APPLICATION_ID:' + AppSettings.PARSE_APPLICATION_ID);
  }

 
  get(id:string): Promise<any> {
    let query = {"objectId":id};
    let where = "where="+JSON.stringify(query);
    let urlFinal = this.url + "?"+where;

    return this.http.get(urlFinal,{headers: this.headers})
    .toPromise()
    .then(response => response.json().results)
    .catch(this.handleError);
  }
  
  findAll(): Promise<any[]> {

    //TODO: Get artist exist field spotify
    let query = {"spotify":{"$exists":"true"}};
    let where = "where="+JSON.stringify(query);
    let urlFinal = this.url + "?limit=500&order=name&"+where;

     return this.http.get(urlFinal,{headers: this.headers})
         .toPromise()
         .then(response => response.json().results)
         .catch(this.handleError);
  }
 
  

  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }

 

}
